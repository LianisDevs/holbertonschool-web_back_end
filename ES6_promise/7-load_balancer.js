export default async function loadBalancer(chinaDownload, USDownload) {
  const fasterResult = await Promise.race([chinaDownload, USDownload]);
  return fasterResult;
}
