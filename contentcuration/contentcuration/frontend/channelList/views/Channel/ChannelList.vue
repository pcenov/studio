<template>

  <VContainer fluid>
    <VLayout row wrap justify-center>
      <VFlex xs12 sm10 md8 lg6>
        <VLayout>
          <VSpacer />
          <VBtn
            v-if="isEditable && !loading"
            color="primary"
            class="add-channel-button"
            data-test="add-channel"
            @click="newChannel"
          >
            {{ $tr('channel') }}
          </VBtn>
        </VLayout>
      </VFlex>
    </VLayout>

    <VLayout row wrap justify-center>
      <VFlex xs12 sm10 md8 lg6>
        <VLayout row justify-center>
          <VFlex xs12>
            <LoadingText v-if="loading" />
            <p v-else-if="listChannels && !listChannels.length" class="headline mb-0">
              {{ $tr('noChannelsFound') }}
            </p>
            <template v-else>
              <ChannelItem
                v-for="channel in listChannels"
                :key="channel.id"
                :channelId="channel.id"
                allowEdit
                fullWidth
              />
            </template>
          </VFlex>
        </VLayout>
      </VFlex>
    </VLayout>
  </VContainer>

</template>


<script>

  import { mapGetters, mapActions } from 'vuex';
  import sortBy from 'lodash/sortBy';
  import { RouterNames, CHANNEL_PAGE_SIZE } from '../../constants';
  import ChannelItem from './ChannelItem';
  import LoadingText from 'shared/views/LoadingText';
  import { ChannelListTypes } from 'shared/constants';

  function listTypeValidator(value) {
    // The value must match one of the ListTypes
    return Object.values(ChannelListTypes).includes(value);
  }

  export default {
    name: 'ChannelList',
    components: {
      ChannelItem,
      LoadingText,
    },
    props: {
      listType: {
        type: String,
        required: true,
        validator: listTypeValidator,
      },
    },
    data() {
      return {
        loading: false,
      };
    },
    computed: {
      ...mapGetters('channel', ['channels']),
      listChannels() {
        const channels = this.channels;
        if (!channels) {
          return [];
        }
        const sortFields = ['-modified'];
        if (this.listType === ChannelListTypes.PUBLIC) {
          sortFields.unshift('-priority');
        }
        return sortBy(
          this.channels.filter(channel => channel[this.listType] && !channel.deleted),
          sortFields
        );
      },
      isEditable() {
        return this.listType === ChannelListTypes.EDITABLE;
      },
      isStarred() {
        return this.listType === ChannelListTypes.STARRED;
      },
    },
    watch: {
      listType(newListType) {
        this.loadData(newListType);
      },
      $route(to, from) {
        if (to.query.page !== from.query.page) {
          this.loadData(this.listType);
        }
      },
    },
    created() {
      this.loadData(this.listType);
    },
    methods: {
      ...mapActions('channel', ['loadChannelList', 'createChannel']),
      newChannel() {
        this.$analytics.trackClick('channel_list', 'Create channel');
        this.createChannel().then(id => {
          this.$router.push({
            name: RouterNames.CHANNEL_EDIT,
            params: { channelId: id, tab: 'edit' },
            query: { last: this.$route.name },
          });
        });
      },
      loadData(listType) {
        this.loading = true;
        let parameters = {
          listType,
          sortBy: '-modified',
        };

        // Don't paginate bookmarked channel list for more
        // rapid updating when channels are starred/unstarred
        if (!this.isStarred) {
          parameters.page = Number(this.$route.query.page || 1);
          parameters.page_size = CHANNEL_PAGE_SIZE;
        }

        this.loadChannelList({ listType }).then(() => {
          this.loading = false;
        });
      },
    },
    $trs: {
      noChannelsFound: 'No channels found',
      channel: 'New channel',
    },
  };

</script>


<style lang="less" scoped>

  .add-channel-button {
    margin: 0;
  }

</style>
