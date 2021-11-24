def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Gender, obj[4]: Age, obj[5]: Children, obj[6]: Education, obj[7]: Occupation, obj[8]: Bar, obj[9]: Coffeehouse, obj[10]: Restaurant20to50, obj[11]: Direction_same, obj[12]: Distance
	# {"feature": "Coupon", "instances": 8148, "metric_value": 0.4751, "depth": 1}
	if obj[2]>1:
		# {"feature": "Coffeehouse", "instances": 5867, "metric_value": 0.461, "depth": 2}
		if obj[9]>0.0:
			# {"feature": "Distance", "instances": 4415, "metric_value": 0.44, "depth": 3}
			if obj[12]<=2:
				# {"feature": "Passanger", "instances": 3980, "metric_value": 0.4296, "depth": 4}
				if obj[0]<=2:
					# {"feature": "Gender", "instances": 2590, "metric_value": 0.4529, "depth": 5}
					if obj[3]>0:
						# {"feature": "Occupation", "instances": 1404, "metric_value": 0.4705, "depth": 6}
						if obj[7]>1.5272800515844427:
							# {"feature": "Time", "instances": 1149, "metric_value": 0.4764, "depth": 7}
							if obj[1]<=3:
								# {"feature": "Children", "instances": 937, "metric_value": 0.482, "depth": 8}
								if obj[5]<=0:
									# {"feature": "Restaurant20to50", "instances": 490, "metric_value": 0.4898, "depth": 9}
									if obj[10]>0.0:
										# {"feature": "Bar", "instances": 418, "metric_value": 0.4829, "depth": 10}
										if obj[8]>0.0:
											# {"feature": "Education", "instances": 309, "metric_value": 0.4772, "depth": 11}
											if obj[6]<=2:
												# {"feature": "Age", "instances": 232, "metric_value": 0.4783, "depth": 12}
												if obj[4]<=4:
													# {"feature": "Direction_same", "instances": 210, "metric_value": 0.4861, "depth": 13}
													if obj[11]<=0:
														return 'True'
													elif obj[11]>0:
														return 'True'
													else: return 'True'
												elif obj[4]>4:
													# {"feature": "Direction_same", "instances": 22, "metric_value": 0.3955, "depth": 13}
													if obj[11]<=0:
														return 'True'
													elif obj[11]>0:
														return 'True'
													else: return 'True'
												else: return 'True'
											elif obj[6]>2:
												# {"feature": "Direction_same", "instances": 77, "metric_value": 0.4596, "depth": 12}
												if obj[11]<=0:
													# {"feature": "Age", "instances": 40, "metric_value": 0.3947, "depth": 13}
													if obj[4]<=1:
														return 'False'
													elif obj[4]>1:
														return 'False'
													else: return 'False'
												elif obj[11]>0:
													# {"feature": "Age", "instances": 37, "metric_value": 0.456, "depth": 13}
													if obj[4]<=1:
														return 'False'
													elif obj[4]>1:
														return 'True'
													else: return 'True'
												else: return 'False'
											else: return 'False'
										elif obj[8]<=0.0:
											# {"feature": "Education", "instances": 109, "metric_value": 0.4152, "depth": 11}
											if obj[6]<=3:
												# {"feature": "Age", "instances": 92, "metric_value": 0.4548, "depth": 12}
												if obj[4]<=5:
													# {"feature": "Direction_same", "instances": 87, "metric_value": 0.4807, "depth": 13}
													if obj[11]<=0:
														return 'True'
													elif obj[11]>0:
														return 'True'
													else: return 'True'
												elif obj[4]>5:
													return 'True'
												else: return 'True'
											elif obj[6]>3:
												# {"feature": "Direction_same", "instances": 17, "metric_value": 0.1008, "depth": 12}
												if obj[11]<=0:
													return 'True'
												elif obj[11]>0:
													# {"feature": "Age", "instances": 7, "metric_value": 0.2286, "depth": 13}
													if obj[4]>0:
														return 'True'
													elif obj[4]<=0:
														return 'True'
													else: return 'True'
												else: return 'True'
											else: return 'True'
										else: return 'True'
									elif obj[10]<=0.0:
										# {"feature": "Bar", "instances": 72, "metric_value": 0.4709, "depth": 10}
										if obj[8]<=0.0:
											# {"feature": "Direction_same", "instances": 43, "metric_value": 0.4921, "depth": 11}
											if obj[11]<=0:
												# {"feature": "Education", "instances": 26, "metric_value": 0.4872, "depth": 12}
												if obj[6]>0:
													# {"feature": "Age", "instances": 20, "metric_value": 0.5, "depth": 13}
													if obj[4]<=1:
														return 'True'
													elif obj[4]>1:
														return 'False'
													else: return 'False'
												elif obj[6]<=0:
													# {"feature": "Age", "instances": 6, "metric_value": 0.4444, "depth": 13}
													if obj[4]<=4:
														return 'False'
													else: return 'False'
												else: return 'False'
											elif obj[11]>0:
												# {"feature": "Age", "instances": 17, "metric_value": 0.4412, "depth": 12}
												if obj[4]<=4:
													# {"feature": "Education", "instances": 16, "metric_value": 0.4667, "depth": 13}
													if obj[6]<=0:
														return 'True'
													elif obj[6]>0:
														return 'True'
													else: return 'True'
												elif obj[4]>4:
													return 'False'
												else: return 'False'
											else: return 'True'
										elif obj[8]>0.0:
											# {"feature": "Education", "instances": 29, "metric_value": 0.4007, "depth": 11}
											if obj[6]>0:
												# {"feature": "Direction_same", "instances": 21, "metric_value": 0.3152, "depth": 12}
												if obj[11]>0:
													# {"feature": "Age", "instances": 11, "metric_value": 0.1591, "depth": 13}
													if obj[4]<=1:
														return 'False'
													elif obj[4]>1:
														return 'False'
													else: return 'False'
												elif obj[11]<=0:
													# {"feature": "Age", "instances": 10, "metric_value": 0.4762, "depth": 13}
													if obj[4]>1:
														return 'False'
													elif obj[4]<=1:
														return 'False'
													else: return 'False'
												else: return 'False'
											elif obj[6]<=0:
												# {"feature": "Age", "instances": 8, "metric_value": 0.5, "depth": 12}
												if obj[4]<=4:
													# {"feature": "Direction_same", "instances": 8, "metric_value": 0.5, "depth": 13}
													if obj[11]>0:
														return 'False'
													elif obj[11]<=0:
														return 'False'
													else: return 'False'
												else: return 'False'
											else: return 'False'
										else: return 'False'
									else: return 'False'
								elif obj[5]>0:
									# {"feature": "Age", "instances": 447, "metric_value": 0.4651, "depth": 9}
									if obj[4]>2:
										# {"feature": "Bar", "instances": 245, "metric_value": 0.4734, "depth": 10}
										if obj[8]>0.0:
											# {"feature": "Restaurant20to50", "instances": 136, "metric_value": 0.4443, "depth": 11}
											if obj[10]<=1.0:
												# {"feature": "Education", "instances": 98, "metric_value": 0.415, "depth": 12}
												if obj[6]>0:
													# {"feature": "Direction_same", "instances": 63, "metric_value": 0.3764, "depth": 13}
													if obj[11]<=0:
														return 'True'
													elif obj[11]>0:
														return 'True'
													else: return 'True'
												elif obj[6]<=0:
													# {"feature": "Direction_same", "instances": 35, "metric_value": 0.4796, "depth": 13}
													if obj[11]<=0:
														return 'True'
													elif obj[11]>0:
														return 'True'
													else: return 'True'
												else: return 'True'
											elif obj[10]>1.0:
												# {"feature": "Education", "instances": 38, "metric_value": 0.485, "depth": 12}
												if obj[6]<=2:
													# {"feature": "Direction_same", "instances": 24, "metric_value": 0.5, "depth": 13}
													if obj[11]<=0:
														return 'True'
													elif obj[11]>0:
														return 'False'
													else: return 'False'
												elif obj[6]>2:
													# {"feature": "Direction_same", "instances": 14, "metric_value": 0.3937, "depth": 13}
													if obj[11]<=0:
														return 'True'
													elif obj[11]>0:
														return 'False'
													else: return 'False'
												else: return 'True'
											else: return 'True'
										elif obj[8]<=0.0:
											# {"feature": "Education", "instances": 109, "metric_value": 0.442, "depth": 11}
											if obj[6]<=2:
												# {"feature": "Restaurant20to50", "instances": 95, "metric_value": 0.4642, "depth": 12}
												if obj[10]<=1.0:
													# {"feature": "Direction_same", "instances": 52, "metric_value": 0.4968, "depth": 13}
													if obj[11]<=0:
														return 'False'
													elif obj[11]>0:
														return 'True'
													else: return 'True'
												elif obj[10]>1.0:
													# {"feature": "Direction_same", "instances": 43, "metric_value": 0.4208, "depth": 13}
													if obj[11]<=0:
														return 'True'
													elif obj[11]>0:
														return 'True'
													else: return 'True'
												else: return 'True'
											elif obj[6]>2:
												# {"feature": "Direction_same", "instances": 14, "metric_value": 0.127, "depth": 12}
												if obj[11]<=0:
													# {"feature": "Restaurant20to50", "instances": 9, "metric_value": 0.1975, "depth": 13}
													if obj[10]<=2.0:
														return 'False'
													else: return 'False'
												elif obj[11]>0:
													return 'False'
												else: return 'False'
											else: return 'False'
										else: return 'True'
									elif obj[4]<=2:
										# {"feature": "Direction_same", "instances": 202, "metric_value": 0.4356, "depth": 10}
										if obj[11]<=0:
											# {"feature": "Education", "instances": 117, "metric_value": 0.4614, "depth": 11}
											if obj[6]<=2:
												# {"feature": "Restaurant20to50", "instances": 95, "metric_value": 0.4455, "depth": 12}
												if obj[10]>0.0:
													# {"feature": "Bar", "instances": 92, "metric_value": 0.4573, "depth": 13}
													if obj[8]<=2.0:
														return 'True'
													elif obj[8]>2.0:
														return 'False'
													else: return 'False'
												elif obj[10]<=0.0:
													return 'True'
												else: return 'True'
											elif obj[6]>2:
												# {"feature": "Restaurant20to50", "instances": 22, "metric_value": 0.4675, "depth": 12}
												if obj[10]>0.0:
													# {"feature": "Bar", "instances": 21, "metric_value": 0.4762, "depth": 13}
													if obj[8]>0.0:
														return 'False'
													elif obj[8]<=0.0:
														return 'False'
													else: return 'False'
												elif obj[10]<=0.0:
													return 'True'
												else: return 'True'
											else: return 'False'
										elif obj[11]>0:
											# {"feature": "Bar", "instances": 85, "metric_value": 0.373, "depth": 11}
											if obj[8]>0.0:
												# {"feature": "Restaurant20to50", "instances": 46, "metric_value": 0.4193, "depth": 12}
												if obj[10]>0.0:
													# {"feature": "Education", "instances": 42, "metric_value": 0.4223, "depth": 13}
													if obj[6]<=2:
														return 'True'
													elif obj[6]>2:
														return 'False'
													else: return 'False'
												elif obj[10]<=0.0:
													return 'True'
												else: return 'True'
											elif obj[8]<=0.0:
												# {"feature": "Restaurant20to50", "instances": 39, "metric_value": 0.2591, "depth": 12}
												if obj[10]<=2.0:
													# {"feature": "Education", "instances": 38, "metric_value": 0.2314, "depth": 13}
													if obj[6]>0:
														return 'True'
													elif obj[6]<=0:
														return 'True'
													else: return 'True'
												elif obj[10]>2.0:
													return 'False'
												else: return 'False'
											else: return 'True'
										else: return 'True'
									else: return 'True'
								else: return 'True'
							elif obj[1]>3:
								# {"feature": "Age", "instances": 212, "metric_value": 0.4272, "depth": 8}
								if obj[4]<=3:
									# {"feature": "Education", "instances": 139, "metric_value": 0.4453, "depth": 9}
									if obj[6]>0:
										# {"feature": "Bar", "instances": 96, "metric_value": 0.4837, "depth": 10}
										if obj[8]<=2.0:
											# {"feature": "Restaurant20to50", "instances": 91, "metric_value": 0.4888, "depth": 11}
											if obj[10]<=1.0:
												# {"feature": "Children", "instances": 57, "metric_value": 0.4953, "depth": 12}
												if obj[5]>0:
													# {"feature": "Direction_same", "instances": 32, "metric_value": 0.4922, "depth": 13}
													if obj[11]<=0:
														return 'True'
													else: return 'True'
												elif obj[5]<=0:
													# {"feature": "Direction_same", "instances": 25, "metric_value": 0.4992, "depth": 13}
													if obj[11]<=0:
														return 'False'
													else: return 'False'
												else: return 'False'
											elif obj[10]>1.0:
												# {"feature": "Children", "instances": 34, "metric_value": 0.4714, "depth": 12}
												if obj[5]>0:
													# {"feature": "Direction_same", "instances": 20, "metric_value": 0.48, "depth": 13}
													if obj[11]<=0:
														return 'True'
													else: return 'True'
												elif obj[5]<=0:
													# {"feature": "Direction_same", "instances": 14, "metric_value": 0.4592, "depth": 13}
													if obj[11]<=0:
														return 'True'
													else: return 'True'
												else: return 'True'
											else: return 'True'
										elif obj[8]>2.0:
											# {"feature": "Restaurant20to50", "instances": 5, "metric_value": 0.2, "depth": 11}
											if obj[10]<=2.0:
												return 'False'
											elif obj[10]>2.0:
												# {"feature": "Children", "instances": 2, "metric_value": 0.0, "depth": 12}
												if obj[5]<=0:
													return 'False'
												elif obj[5]>0:
													return 'True'
												else: return 'True'
											else: return 'False'
										else: return 'False'
									elif obj[6]<=0:
										# {"feature": "Restaurant20to50", "instances": 43, "metric_value": 0.32, "depth": 10}
										if obj[10]<=1.0:
											# {"feature": "Bar", "instances": 26, "metric_value": 0.3671, "depth": 11}
											if obj[8]<=1.0:
												# {"feature": "Children", "instances": 22, "metric_value": 0.4227, "depth": 12}
												if obj[5]<=0:
													# {"feature": "Direction_same", "instances": 12, "metric_value": 0.375, "depth": 13}
													if obj[11]<=0:
														return 'True'
													else: return 'True'
												elif obj[5]>0:
													# {"feature": "Direction_same", "instances": 10, "metric_value": 0.48, "depth": 13}
													if obj[11]<=0:
														return 'True'
													else: return 'True'
												else: return 'True'
											elif obj[8]>1.0:
												return 'True'
											else: return 'True'
										elif obj[10]>1.0:
											# {"feature": "Bar", "instances": 17, "metric_value": 0.1968, "depth": 11}
											if obj[8]<=1.0:
												# {"feature": "Children", "instances": 13, "metric_value": 0.1282, "depth": 12}
												if obj[5]<=0:
													return 'True'
												elif obj[5]>0:
													# {"feature": "Direction_same", "instances": 6, "metric_value": 0.2778, "depth": 13}
													if obj[11]<=0:
														return 'True'
													else: return 'True'
												else: return 'True'
											elif obj[8]>1.0:
												# {"feature": "Children", "instances": 4, "metric_value": 0.3333, "depth": 12}
												if obj[5]<=0:
													# {"feature": "Direction_same", "instances": 3, "metric_value": 0.4444, "depth": 13}
													if obj[11]<=0:
														return 'True'
													else: return 'True'
												elif obj[5]>0:
													return 'True'
												else: return 'True'
											else: return 'True'
										else: return 'True'
									else: return 'True'
								elif obj[4]>3:
									# {"feature": "Education", "instances": 73, "metric_value": 0.3305, "depth": 9}
									if obj[6]<=3:
										# {"feature": "Restaurant20to50", "instances": 65, "metric_value": 0.3632, "depth": 10}
										if obj[10]<=2.0:
											# {"feature": "Bar", "instances": 61, "metric_value": 0.3798, "depth": 11}
											if obj[8]<=2.0:
												# {"feature": "Children", "instances": 54, "metric_value": 0.3649, "depth": 12}
												if obj[5]>0:
													# {"feature": "Direction_same", "instances": 27, "metric_value": 0.3841, "depth": 13}
													if obj[11]<=0:
														return 'True'
													else: return 'True'
												elif obj[5]<=0:
													# {"feature": "Direction_same", "instances": 27, "metric_value": 0.3457, "depth": 13}
													if obj[11]<=0:
														return 'True'
													else: return 'True'
												else: return 'True'
											elif obj[8]>2.0:
												# {"feature": "Children", "instances": 7, "metric_value": 0.2286, "depth": 12}
												if obj[5]<=0:
													# {"feature": "Direction_same", "instances": 5, "metric_value": 0.32, "depth": 13}
													if obj[11]<=0:
														return 'True'
													else: return 'True'
												elif obj[5]>0:
													return 'False'
												else: return 'False'
											else: return 'True'
										elif obj[10]>2.0:
											return 'True'
										else: return 'True'
									elif obj[6]>3:
										return 'True'
									else: return 'True'
								else: return 'True'
							else: return 'True'
						elif obj[7]<=1.5272800515844427:
							# {"feature": "Time", "instances": 255, "metric_value": 0.4244, "depth": 7}
							if obj[1]>0:
								# {"feature": "Education", "instances": 180, "metric_value": 0.4477, "depth": 8}
								if obj[6]<=2:
									# {"feature": "Restaurant20to50", "instances": 151, "metric_value": 0.4706, "depth": 9}
									if obj[10]<=2.0:
										# {"feature": "Bar", "instances": 133, "metric_value": 0.476, "depth": 10}
										if obj[8]<=0.0:
											# {"feature": "Age", "instances": 76, "metric_value": 0.4149, "depth": 11}
											if obj[4]>2:
												# {"feature": "Children", "instances": 41, "metric_value": 0.3346, "depth": 12}
												if obj[5]>0:
													# {"feature": "Direction_same", "instances": 39, "metric_value": 0.3201, "depth": 13}
													if obj[11]<=0:
														return 'True'
													elif obj[11]>0:
														return 'True'
													else: return 'True'
												elif obj[5]<=0:
													# {"feature": "Direction_same", "instances": 2, "metric_value": 0.5, "depth": 13}
													if obj[11]<=0:
														return 'False'
													else: return 'False'
												else: return 'False'
											elif obj[4]<=2:
												# {"feature": "Direction_same", "instances": 35, "metric_value": 0.4515, "depth": 12}
												if obj[11]<=0:
													# {"feature": "Children", "instances": 26, "metric_value": 0.4727, "depth": 13}
													if obj[5]>0:
														return 'True'
													elif obj[5]<=0:
														return 'False'
													else: return 'False'
												elif obj[11]>0:
													# {"feature": "Children", "instances": 9, "metric_value": 0.3016, "depth": 13}
													if obj[5]>0:
														return 'False'
													elif obj[5]<=0:
														return 'False'
													else: return 'False'
												else: return 'False'
											else: return 'False'
										elif obj[8]>0.0:
											# {"feature": "Direction_same", "instances": 57, "metric_value": 0.4698, "depth": 11}
											if obj[11]<=0:
												# {"feature": "Children", "instances": 41, "metric_value": 0.4345, "depth": 12}
												if obj[5]<=0:
													# {"feature": "Age", "instances": 29, "metric_value": 0.4939, "depth": 13}
													if obj[4]>1:
														return 'False'
													elif obj[4]<=1:
														return 'True'
													else: return 'True'
												elif obj[5]>0:
													# {"feature": "Age", "instances": 12, "metric_value": 0.2, "depth": 13}
													if obj[4]>1:
														return 'False'
													elif obj[4]<=1:
														return 'False'
													else: return 'False'
												else: return 'False'
											elif obj[11]>0:
												# {"feature": "Age", "instances": 16, "metric_value": 0.4087, "depth": 12}
												if obj[4]<=3:
													# {"feature": "Children", "instances": 9, "metric_value": 0.3444, "depth": 13}
													if obj[5]<=0:
														return 'True'
													elif obj[5]>0:
														return 'True'
													else: return 'True'
												elif obj[4]>3:
													# {"feature": "Children", "instances": 7, "metric_value": 0.4286, "depth": 13}
													if obj[5]<=0:
														return 'True'
													elif obj[5]>0:
														return 'True'
													else: return 'True'
												else: return 'True'
											else: return 'True'
										else: return 'False'
									elif obj[10]>2.0:
										# {"feature": "Age", "instances": 18, "metric_value": 0.3214, "depth": 10}
										if obj[4]<=4:
											# {"feature": "Children", "instances": 13, "metric_value": 0.2051, "depth": 11}
											if obj[5]<=0:
												return 'True'
											elif obj[5]>0:
												# {"feature": "Direction_same", "instances": 6, "metric_value": 0.3333, "depth": 12}
												if obj[11]>0:
													# {"feature": "Bar", "instances": 4, "metric_value": 0.5, "depth": 13}
													if obj[8]<=1.0:
														return 'False'
													else: return 'False'
												elif obj[11]<=0:
													return 'True'
												else: return 'True'
											else: return 'True'
										elif obj[4]>4:
											# {"feature": "Direction_same", "instances": 5, "metric_value": 0.4667, "depth": 11}
											if obj[11]<=0:
												# {"feature": "Children", "instances": 3, "metric_value": 0.4444, "depth": 12}
												if obj[5]<=0:
													# {"feature": "Bar", "instances": 3, "metric_value": 0.4444, "depth": 13}
													if obj[8]<=1.0:
														return 'True'
													else: return 'True'
												else: return 'True'
											elif obj[11]>0:
												# {"feature": "Children", "instances": 2, "metric_value": 0.5, "depth": 12}
												if obj[5]<=0:
													# {"feature": "Bar", "instances": 2, "metric_value": 0.5, "depth": 13}
													if obj[8]<=1.0:
														return 'True'
													else: return 'True'
												else: return 'True'
											else: return 'True'
										else: return 'True'
									else: return 'True'
								elif obj[6]>2:
									# {"feature": "Restaurant20to50", "instances": 29, "metric_value": 0.2436, "depth": 9}
									if obj[10]>0.0:
										# {"feature": "Age", "instances": 22, "metric_value": 0.1364, "depth": 10}
										if obj[4]>0:
											return 'True'
										elif obj[4]<=0:
											# {"feature": "Direction_same", "instances": 8, "metric_value": 0.3571, "depth": 11}
											if obj[11]<=0:
												# {"feature": "Children", "instances": 7, "metric_value": 0.4082, "depth": 12}
												if obj[5]<=1:
													# {"feature": "Bar", "instances": 7, "metric_value": 0.4082, "depth": 13}
													if obj[8]<=0.0:
														return 'True'
													else: return 'True'
												else: return 'True'
											elif obj[11]>0:
												return 'True'
											else: return 'True'
										else: return 'True'
									elif obj[10]<=0.0:
										# {"feature": "Age", "instances": 7, "metric_value": 0.4048, "depth": 10}
										if obj[4]<=1:
											# {"feature": "Direction_same", "instances": 4, "metric_value": 0.3333, "depth": 11}
											if obj[11]>0:
												# {"feature": "Children", "instances": 3, "metric_value": 0.4444, "depth": 12}
												if obj[5]<=1:
													# {"feature": "Bar", "instances": 3, "metric_value": 0.4444, "depth": 13}
													if obj[8]<=1.0:
														return 'True'
													else: return 'True'
												else: return 'True'
											elif obj[11]<=0:
												return 'True'
											else: return 'True'
										elif obj[4]>1:
											# {"feature": "Direction_same", "instances": 3, "metric_value": 0.3333, "depth": 11}
											if obj[11]<=0:
												# {"feature": "Children", "instances": 2, "metric_value": 0.5, "depth": 12}
												if obj[5]<=0:
													# {"feature": "Bar", "instances": 2, "metric_value": 0.5, "depth": 13}
													if obj[8]<=0.0:
														return 'True'
													else: return 'True'
												else: return 'True'
											elif obj[11]>0:
												return 'False'
											else: return 'False'
										else: return 'False'
									else: return 'True'
								else: return 'True'
							elif obj[1]<=0:
								# {"feature": "Direction_same", "instances": 75, "metric_value": 0.3032, "depth": 8}
								if obj[11]<=0:
									# {"feature": "Age", "instances": 49, "metric_value": 0.3718, "depth": 9}
									if obj[4]>1:
										# {"feature": "Education", "instances": 32, "metric_value": 0.2949, "depth": 10}
										if obj[6]>0:
											# {"feature": "Restaurant20to50", "instances": 21, "metric_value": 0.3048, "depth": 11}
											if obj[10]<=2.0:
												# {"feature": "Bar", "instances": 20, "metric_value": 0.3059, "depth": 12}
												if obj[8]<=0.0:
													# {"feature": "Children", "instances": 17, "metric_value": 0.3588, "depth": 13}
													if obj[5]>0:
														return 'True'
													elif obj[5]<=0:
														return 'True'
													else: return 'True'
												elif obj[8]>0.0:
													return 'True'
												else: return 'True'
											elif obj[10]>2.0:
												return 'False'
											else: return 'False'
										elif obj[6]<=0:
											# {"feature": "Bar", "instances": 11, "metric_value": 0.1558, "depth": 11}
											if obj[8]<=0.0:
												# {"feature": "Children", "instances": 7, "metric_value": 0.2449, "depth": 12}
												if obj[5]<=1:
													# {"feature": "Restaurant20to50", "instances": 7, "metric_value": 0.2449, "depth": 13}
													if obj[10]<=1.0:
														return 'True'
													else: return 'True'
												else: return 'True'
											elif obj[8]>0.0:
												return 'True'
											else: return 'True'
										else: return 'True'
									elif obj[4]<=1:
										# {"feature": "Restaurant20to50", "instances": 17, "metric_value": 0.2075, "depth": 10}
										if obj[10]<=1.0:
											# {"feature": "Education", "instances": 9, "metric_value": 0.1667, "depth": 11}
											if obj[6]<=0:
												return 'False'
											elif obj[6]>0:
												# {"feature": "Children", "instances": 4, "metric_value": 0.25, "depth": 12}
												if obj[5]>0:
													# {"feature": "Bar", "instances": 2, "metric_value": 0.5, "depth": 13}
													if obj[8]<=0.0:
														return 'False'
													else: return 'False'
												elif obj[5]<=0:
													return 'False'
												else: return 'False'
											else: return 'False'
										elif obj[10]>1.0:
											# {"feature": "Children", "instances": 8, "metric_value": 0.1667, "depth": 11}
											if obj[5]<=0:
												return 'True'
											elif obj[5]>0:
												# {"feature": "Education", "instances": 3, "metric_value": 0.4444, "depth": 12}
												if obj[6]<=1:
													# {"feature": "Bar", "instances": 3, "metric_value": 0.4444, "depth": 13}
													if obj[8]<=0.0:
														return 'True'
													else: return 'True'
												else: return 'True'
											else: return 'True'
										else: return 'True'
									else: return 'False'
								elif obj[11]>0:
									# {"feature": "Age", "instances": 26, "metric_value": 0.0513, "depth": 9}
									if obj[4]<=6:
										return 'True'
									elif obj[4]>6:
										# {"feature": "Education", "instances": 3, "metric_value": 0.3333, "depth": 10}
										if obj[6]>2:
											# {"feature": "Children", "instances": 2, "metric_value": 0.5, "depth": 11}
											if obj[5]<=0:
												# {"feature": "Bar", "instances": 2, "metric_value": 0.5, "depth": 12}
												if obj[8]<=0.0:
													# {"feature": "Restaurant20to50", "instances": 2, "metric_value": 0.5, "depth": 13}
													if obj[10]<=1.0:
														return 'False'
													else: return 'False'
												else: return 'False'
											else: return 'False'
										elif obj[6]<=2:
											return 'True'
										else: return 'True'
									else: return 'True'
								else: return 'True'
							else: return 'True'
						else: return 'True'
					elif obj[3]<=0:
						# {"feature": "Age", "instances": 1186, "metric_value": 0.4269, "depth": 6}
						if obj[4]<=4:
							# {"feature": "Occupation", "instances": 902, "metric_value": 0.4416, "depth": 7}
							if obj[7]<=19.215025871277074:
								# {"feature": "Bar", "instances": 839, "metric_value": 0.4514, "depth": 8}
								if obj[8]<=1.0:
									# {"feature": "Restaurant20to50", "instances": 442, "metric_value": 0.4284, "depth": 9}
									if obj[10]>0.0:
										# {"feature": "Education", "instances": 389, "metric_value": 0.4434, "depth": 10}
										if obj[6]>0:
											# {"feature": "Time", "instances": 301, "metric_value": 0.427, "depth": 11}
											if obj[1]<=3:
												# {"feature": "Direction_same", "instances": 239, "metric_value": 0.4395, "depth": 12}
												if obj[11]<=0:
													# {"feature": "Children", "instances": 128, "metric_value": 0.4647, "depth": 13}
													if obj[5]<=0:
														return 'True'
													elif obj[5]>0:
														return 'True'
													else: return 'True'
												elif obj[11]>0:
													# {"feature": "Children", "instances": 111, "metric_value": 0.4061, "depth": 13}
													if obj[5]<=0:
														return 'True'
													elif obj[5]>0:
														return 'True'
													else: return 'True'
												else: return 'True'
											elif obj[1]>3:
												# {"feature": "Children", "instances": 62, "metric_value": 0.3511, "depth": 12}
												if obj[5]<=0:
													# {"feature": "Direction_same", "instances": 36, "metric_value": 0.2778, "depth": 13}
													if obj[11]<=0:
														return 'True'
													else: return 'True'
												elif obj[5]>0:
													# {"feature": "Direction_same", "instances": 26, "metric_value": 0.4527, "depth": 13}
													if obj[11]<=0:
														return 'True'
													else: return 'True'
												else: return 'True'
											else: return 'True'
										elif obj[6]<=0:
											# {"feature": "Time", "instances": 88, "metric_value": 0.4569, "depth": 11}
											if obj[1]<=1:
												# {"feature": "Children", "instances": 47, "metric_value": 0.4875, "depth": 12}
												if obj[5]<=0:
													# {"feature": "Direction_same", "instances": 33, "metric_value": 0.4992, "depth": 13}
													if obj[11]>0:
														return 'False'
													elif obj[11]<=0:
														return 'True'
													else: return 'True'
												elif obj[5]>0:
													# {"feature": "Direction_same", "instances": 14, "metric_value": 0.4589, "depth": 13}
													if obj[11]<=0:
														return 'False'
													elif obj[11]>0:
														return 'False'
													else: return 'False'
												else: return 'False'
											elif obj[1]>1:
												# {"feature": "Children", "instances": 41, "metric_value": 0.4131, "depth": 12}
												if obj[5]<=0:
													# {"feature": "Direction_same", "instances": 22, "metric_value": 0.3936, "depth": 13}
													if obj[11]<=0:
														return 'True'
													elif obj[11]>0:
														return 'True'
													else: return 'True'
												elif obj[5]>0:
													# {"feature": "Direction_same", "instances": 19, "metric_value": 0.432, "depth": 13}
													if obj[11]<=0:
														return 'True'
													elif obj[11]>0:
														return 'True'
													else: return 'True'
												else: return 'True'
											else: return 'True'
										else: return 'True'
									elif obj[10]<=0.0:
										# {"feature": "Children", "instances": 53, "metric_value": 0.267, "depth": 10}
										if obj[5]<=0:
											# {"feature": "Education", "instances": 45, "metric_value": 0.22, "depth": 11}
											if obj[6]<=0:
												# {"feature": "Time", "instances": 25, "metric_value": 0.313, "depth": 12}
												if obj[1]<=3:
													# {"feature": "Direction_same", "instances": 23, "metric_value": 0.3398, "depth": 13}
													if obj[11]>0:
														return 'True'
													elif obj[11]<=0:
														return 'True'
													else: return 'True'
												elif obj[1]>3:
													return 'True'
												else: return 'True'
											elif obj[6]>0:
												# {"feature": "Direction_same", "instances": 20, "metric_value": 0.0909, "depth": 12}
												if obj[11]<=0:
													# {"feature": "Time", "instances": 11, "metric_value": 0.1515, "depth": 13}
													if obj[1]<=1:
														return 'True'
													elif obj[1]>1:
														return 'True'
													else: return 'True'
												elif obj[11]>0:
													return 'True'
												else: return 'True'
											else: return 'True'
										elif obj[5]>0:
											# {"feature": "Time", "instances": 8, "metric_value": 0.1875, "depth": 11}
											if obj[1]>1:
												return 'True'
											elif obj[1]<=1:
												# {"feature": "Direction_same", "instances": 4, "metric_value": 0.0, "depth": 12}
												if obj[11]<=0:
													return 'False'
												elif obj[11]>0:
													return 'True'
												else: return 'True'
											else: return 'False'
										else: return 'True'
									else: return 'True'
								elif obj[8]>1.0:
									# {"feature": "Children", "instances": 397, "metric_value": 0.4662, "depth": 9}
									if obj[5]<=0:
										# {"feature": "Education", "instances": 286, "metric_value": 0.4792, "depth": 10}
										if obj[6]<=3:
											# {"feature": "Restaurant20to50", "instances": 268, "metric_value": 0.4734, "depth": 11}
											if obj[10]>0.0:
												# {"feature": "Time", "instances": 220, "metric_value": 0.4631, "depth": 12}
												if obj[1]>0:
													# {"feature": "Direction_same", "instances": 162, "metric_value": 0.4722, "depth": 13}
													if obj[11]<=0:
														return 'True'
													elif obj[11]>0:
														return 'True'
													else: return 'True'
												elif obj[1]<=0:
													# {"feature": "Direction_same", "instances": 58, "metric_value": 0.4056, "depth": 13}
													if obj[11]<=0:
														return 'True'
													elif obj[11]>0:
														return 'True'
													else: return 'True'
												else: return 'True'
											elif obj[10]<=0.0:
												# {"feature": "Time", "instances": 48, "metric_value": 0.4872, "depth": 12}
												if obj[1]<=3:
													# {"feature": "Direction_same", "instances": 39, "metric_value": 0.4962, "depth": 13}
													if obj[11]>0:
														return 'False'
													elif obj[11]<=0:
														return 'False'
													else: return 'False'
												elif obj[1]>3:
													# {"feature": "Direction_same", "instances": 9, "metric_value": 0.4444, "depth": 13}
													if obj[11]<=0:
														return 'True'
													else: return 'True'
												else: return 'True'
											else: return 'False'
										elif obj[6]>3:
											# {"feature": "Restaurant20to50", "instances": 18, "metric_value": 0.4444, "depth": 11}
											if obj[10]>0.0:
												# {"feature": "Direction_same", "instances": 12, "metric_value": 0.3704, "depth": 12}
												if obj[11]<=0:
													# {"feature": "Time", "instances": 9, "metric_value": 0.4333, "depth": 13}
													if obj[1]<=1:
														return 'True'
													elif obj[1]>1:
														return 'False'
													else: return 'False'
												elif obj[11]>0:
													return 'False'
												else: return 'False'
											elif obj[10]<=0.0:
												# {"feature": "Direction_same", "instances": 6, "metric_value": 0.3333, "depth": 12}
												if obj[11]>0:
													# {"feature": "Time", "instances": 4, "metric_value": 0.5, "depth": 13}
													if obj[1]<=0:
														return 'True'
													elif obj[1]>0:
														return 'False'
													else: return 'False'
												elif obj[11]<=0:
													return 'True'
												else: return 'True'
											else: return 'True'
										else: return 'False'
									elif obj[5]>0:
										# {"feature": "Time", "instances": 111, "metric_value": 0.4132, "depth": 10}
										if obj[1]<=2:
											# {"feature": "Education", "instances": 78, "metric_value": 0.3605, "depth": 11}
											if obj[6]>1:
												# {"feature": "Restaurant20to50", "instances": 50, "metric_value": 0.275, "depth": 12}
												if obj[10]<=2.0:
													# {"feature": "Direction_same", "instances": 35, "metric_value": 0.2, "depth": 13}
													if obj[11]<=0:
														return 'True'
													elif obj[11]>0:
														return 'True'
													else: return 'True'
												elif obj[10]>2.0:
													# {"feature": "Direction_same", "instances": 15, "metric_value": 0.3889, "depth": 13}
													if obj[11]<=0:
														return 'True'
													elif obj[11]>0:
														return 'True'
													else: return 'True'
												else: return 'True'
											elif obj[6]<=1:
												# {"feature": "Restaurant20to50", "instances": 28, "metric_value": 0.4194, "depth": 12}
												if obj[10]<=1.0:
													# {"feature": "Direction_same", "instances": 17, "metric_value": 0.4563, "depth": 13}
													if obj[11]<=0:
														return 'False'
													elif obj[11]>0:
														return 'True'
													else: return 'True'
												elif obj[10]>1.0:
													# {"feature": "Direction_same", "instances": 11, "metric_value": 0.2922, "depth": 13}
													if obj[11]<=0:
														return 'True'
													elif obj[11]>0:
														return 'True'
													else: return 'True'
												else: return 'True'
											else: return 'True'
										elif obj[1]>2:
											# {"feature": "Restaurant20to50", "instances": 33, "metric_value": 0.465, "depth": 11}
											if obj[10]<=1.0:
												# {"feature": "Direction_same", "instances": 17, "metric_value": 0.4843, "depth": 12}
												if obj[11]<=0:
													# {"feature": "Education", "instances": 12, "metric_value": 0.4583, "depth": 13}
													if obj[6]>2:
														return 'True'
													elif obj[6]<=2:
														return 'False'
													else: return 'False'
												elif obj[11]>0:
													# {"feature": "Education", "instances": 5, "metric_value": 0.3, "depth": 13}
													if obj[6]<=2:
														return 'True'
													elif obj[6]>2:
														return 'False'
													else: return 'False'
												else: return 'True'
											elif obj[10]>1.0:
												# {"feature": "Education", "instances": 16, "metric_value": 0.3875, "depth": 12}
												if obj[6]<=4:
													# {"feature": "Direction_same", "instances": 10, "metric_value": 0.3, "depth": 13}
													if obj[11]<=0:
														return 'True'
													elif obj[11]>0:
														return 'True'
													else: return 'True'
												elif obj[6]>4:
													# {"feature": "Direction_same", "instances": 6, "metric_value": 0.4, "depth": 13}
													if obj[11]<=0:
														return 'True'
													elif obj[11]>0:
														return 'False'
													else: return 'False'
												else: return 'True'
											else: return 'True'
										else: return 'True'
									else: return 'True'
								else: return 'True'
							elif obj[7]>19.215025871277074:
								# {"feature": "Education", "instances": 63, "metric_value": 0.2574, "depth": 8}
								if obj[6]<=2:
									# {"feature": "Bar", "instances": 55, "metric_value": 0.2055, "depth": 9}
									if obj[8]<=2.0:
										# {"feature": "Time", "instances": 46, "metric_value": 0.1528, "depth": 10}
										if obj[1]<=3:
											# {"feature": "Direction_same", "instances": 33, "metric_value": 0.2048, "depth": 11}
											if obj[11]>0:
												# {"feature": "Restaurant20to50", "instances": 17, "metric_value": 0.1046, "depth": 12}
												if obj[10]<=1.0:
													# {"feature": "Children", "instances": 9, "metric_value": 0.1944, "depth": 13}
													if obj[5]>0:
														return 'True'
													elif obj[5]<=0:
														return 'True'
													else: return 'True'
												elif obj[10]>1.0:
													return 'True'
												else: return 'True'
											elif obj[11]<=0:
												# {"feature": "Restaurant20to50", "instances": 16, "metric_value": 0.2167, "depth": 12}
												if obj[10]>0.0:
													# {"feature": "Children", "instances": 15, "metric_value": 0.2222, "depth": 13}
													if obj[5]>0:
														return 'True'
													elif obj[5]<=0:
														return 'True'
													else: return 'True'
												elif obj[10]<=0.0:
													return 'False'
												else: return 'False'
											else: return 'True'
										elif obj[1]>3:
											return 'True'
										else: return 'True'
									elif obj[8]>2.0:
										# {"feature": "Direction_same", "instances": 9, "metric_value": 0.4, "depth": 10}
										if obj[11]>0:
											# {"feature": "Time", "instances": 5, "metric_value": 0.2667, "depth": 11}
											if obj[1]>0:
												# {"feature": "Restaurant20to50", "instances": 3, "metric_value": 0.3333, "depth": 12}
												if obj[10]>1.0:
													# {"feature": "Children", "instances": 2, "metric_value": 0.5, "depth": 13}
													if obj[5]<=0:
														return 'True'
													else: return 'True'
												elif obj[10]<=1.0:
													return 'True'
												else: return 'True'
											elif obj[1]<=0:
												return 'True'
											else: return 'True'
										elif obj[11]<=0:
											# {"feature": "Time", "instances": 4, "metric_value": 0.3333, "depth": 11}
											if obj[1]>0:
												# {"feature": "Restaurant20to50", "instances": 3, "metric_value": 0.3333, "depth": 12}
												if obj[10]>1.0:
													# {"feature": "Children", "instances": 2, "metric_value": 0.5, "depth": 13}
													if obj[5]<=0:
														return 'False'
													else: return 'False'
												elif obj[10]<=1.0:
													return 'True'
												else: return 'True'
											elif obj[1]<=0:
												return 'False'
											else: return 'False'
										else: return 'False'
									else: return 'True'
								elif obj[6]>2:
									# {"feature": "Time", "instances": 8, "metric_value": 0.3333, "depth": 9}
									if obj[1]>0:
										# {"feature": "Direction_same", "instances": 6, "metric_value": 0.3333, "depth": 10}
										if obj[11]<=0:
											# {"feature": "Children", "instances": 4, "metric_value": 0.5, "depth": 11}
											if obj[5]<=0:
												# {"feature": "Bar", "instances": 4, "metric_value": 0.5, "depth": 12}
												if obj[8]<=1.0:
													# {"feature": "Restaurant20to50", "instances": 4, "metric_value": 0.5, "depth": 13}
													if obj[10]<=2.0:
														return 'True'
													else: return 'True'
												else: return 'True'
											else: return 'True'
										elif obj[11]>0:
											return 'False'
										else: return 'False'
									elif obj[1]<=0:
										return 'True'
									else: return 'True'
								else: return 'True'
							else: return 'True'
						elif obj[4]>4:
							# {"feature": "Education", "instances": 284, "metric_value": 0.3594, "depth": 7}
							if obj[6]<=0:
								# {"feature": "Occupation", "instances": 165, "metric_value": 0.3, "depth": 8}
								if obj[7]<=21:
									# {"feature": "Time", "instances": 158, "metric_value": 0.2877, "depth": 9}
									if obj[1]<=3:
										# {"feature": "Direction_same", "instances": 132, "metric_value": 0.3122, "depth": 10}
										if obj[11]>0:
											# {"feature": "Restaurant20to50", "instances": 66, "metric_value": 0.2517, "depth": 11}
											if obj[10]>0.0:
												# {"feature": "Children", "instances": 59, "metric_value": 0.2805, "depth": 12}
												if obj[5]<=0:
													# {"feature": "Bar", "instances": 58, "metric_value": 0.2853, "depth": 13}
													if obj[8]<=1.0:
														return 'True'
													elif obj[8]>1.0:
														return 'True'
													else: return 'True'
												elif obj[5]>0:
													return 'True'
												else: return 'True'
											elif obj[10]<=0.0:
												return 'True'
											else: return 'True'
										elif obj[11]<=0:
											# {"feature": "Restaurant20to50", "instances": 66, "metric_value": 0.3588, "depth": 11}
											if obj[10]<=1.0:
												# {"feature": "Bar", "instances": 49, "metric_value": 0.3222, "depth": 12}
												if obj[8]<=0.0:
													# {"feature": "Children", "instances": 30, "metric_value": 0.3578, "depth": 13}
													if obj[5]<=0:
														return 'True'
													else: return 'True'
												elif obj[8]>0.0:
													# {"feature": "Children", "instances": 19, "metric_value": 0.2644, "depth": 13}
													if obj[5]>0:
														return 'True'
													elif obj[5]<=0:
														return 'True'
													else: return 'True'
												else: return 'True'
											elif obj[10]>1.0:
												# {"feature": "Children", "instances": 17, "metric_value": 0.4379, "depth": 12}
												if obj[5]<=0:
													# {"feature": "Bar", "instances": 9, "metric_value": 0.4444, "depth": 13}
													if obj[8]>0.0:
														return 'True'
													elif obj[8]<=0.0:
														return 'False'
													else: return 'False'
												elif obj[5]>0:
													# {"feature": "Bar", "instances": 8, "metric_value": 0.3, "depth": 13}
													if obj[8]>0.0:
														return 'True'
													elif obj[8]<=0.0:
														return 'True'
													else: return 'True'
												else: return 'True'
											else: return 'True'
										else: return 'True'
									elif obj[1]>3:
										# {"feature": "Bar", "instances": 26, "metric_value": 0.1348, "depth": 10}
										if obj[8]<=1.0:
											# {"feature": "Restaurant20to50", "instances": 21, "metric_value": 0.0893, "depth": 11}
											if obj[10]<=1.0:
												# {"feature": "Children", "instances": 16, "metric_value": 0.1172, "depth": 12}
												if obj[5]<=0:
													# {"feature": "Direction_same", "instances": 16, "metric_value": 0.1172, "depth": 13}
													if obj[11]<=0:
														return 'True'
													else: return 'True'
												else: return 'True'
											elif obj[10]>1.0:
												return 'True'
											else: return 'True'
										elif obj[8]>1.0:
											# {"feature": "Children", "instances": 5, "metric_value": 0.2, "depth": 11}
											if obj[5]<=0:
												return 'True'
											elif obj[5]>0:
												# {"feature": "Restaurant20to50", "instances": 2, "metric_value": 0.5, "depth": 12}
												if obj[10]<=1.0:
													# {"feature": "Direction_same", "instances": 2, "metric_value": 0.5, "depth": 13}
													if obj[11]<=0:
														return 'True'
													else: return 'True'
												else: return 'True'
											else: return 'True'
										else: return 'True'
									else: return 'True'
								elif obj[7]>21:
									# {"feature": "Direction_same", "instances": 7, "metric_value": 0.4048, "depth": 9}
									if obj[11]<=0:
										# {"feature": "Time", "instances": 4, "metric_value": 0.25, "depth": 10}
										if obj[1]<=3:
											return 'True'
										elif obj[1]>3:
											# {"feature": "Children", "instances": 2, "metric_value": 0.5, "depth": 11}
											if obj[5]<=0:
												# {"feature": "Bar", "instances": 2, "metric_value": 0.5, "depth": 12}
												if obj[8]<=3.0:
													# {"feature": "Restaurant20to50", "instances": 2, "metric_value": 0.5, "depth": 13}
													if obj[10]<=2.0:
														return 'True'
													else: return 'True'
												else: return 'True'
											else: return 'True'
										else: return 'True'
									elif obj[11]>0:
										# {"feature": "Time", "instances": 3, "metric_value": 0.3333, "depth": 10}
										if obj[1]>0:
											# {"feature": "Children", "instances": 2, "metric_value": 0.5, "depth": 11}
											if obj[5]<=0:
												# {"feature": "Bar", "instances": 2, "metric_value": 0.5, "depth": 12}
												if obj[8]<=3.0:
													# {"feature": "Restaurant20to50", "instances": 2, "metric_value": 0.5, "depth": 13}
													if obj[10]<=2.0:
														return 'False'
													else: return 'False'
												else: return 'False'
											else: return 'False'
										elif obj[1]<=0:
											return 'False'
										else: return 'False'
									else: return 'False'
								else: return 'True'
							elif obj[6]>0:
								# {"feature": "Occupation", "instances": 119, "metric_value": 0.3986, "depth": 8}
								if obj[7]<=13:
									# {"feature": "Time", "instances": 112, "metric_value": 0.3981, "depth": 9}
									if obj[1]<=2:
										# {"feature": "Restaurant20to50", "instances": 76, "metric_value": 0.3388, "depth": 10}
										if obj[10]>0.0:
											# {"feature": "Direction_same", "instances": 69, "metric_value": 0.3186, "depth": 11}
											if obj[11]<=0:
												# {"feature": "Bar", "instances": 36, "metric_value": 0.3577, "depth": 12}
												if obj[8]<=1.0:
													# {"feature": "Children", "instances": 26, "metric_value": 0.4253, "depth": 13}
													if obj[5]>0:
														return 'True'
													elif obj[5]<=0:
														return 'True'
													else: return 'True'
												elif obj[8]>1.0:
													# {"feature": "Children", "instances": 10, "metric_value": 0.1667, "depth": 13}
													if obj[5]<=0:
														return 'True'
													elif obj[5]>0:
														return 'True'
													else: return 'True'
												else: return 'True'
											elif obj[11]>0:
												# {"feature": "Bar", "instances": 33, "metric_value": 0.2414, "depth": 12}
												if obj[8]<=2.0:
													# {"feature": "Children", "instances": 31, "metric_value": 0.2193, "depth": 13}
													if obj[5]<=0:
														return 'True'
													elif obj[5]>0:
														return 'True'
													else: return 'True'
												elif obj[8]>2.0:
													# {"feature": "Children", "instances": 2, "metric_value": 0.5, "depth": 13}
													if obj[5]<=0:
														return 'False'
													else: return 'False'
												else: return 'False'
											else: return 'True'
										elif obj[10]<=0.0:
											# {"feature": "Children", "instances": 7, "metric_value": 0.4857, "depth": 11}
											if obj[5]>0:
												# {"feature": "Bar", "instances": 5, "metric_value": 0.48, "depth": 12}
												if obj[8]<=0.0:
													# {"feature": "Direction_same", "instances": 5, "metric_value": 0.48, "depth": 13}
													if obj[11]<=0:
														return 'False'
													else: return 'False'
												else: return 'False'
											elif obj[5]<=0:
												# {"feature": "Bar", "instances": 2, "metric_value": 0.5, "depth": 12}
												if obj[8]<=0.0:
													# {"feature": "Direction_same", "instances": 2, "metric_value": 0.5, "depth": 13}
													if obj[11]<=0:
														return 'False'
													else: return 'False'
												else: return 'False'
											else: return 'False'
										else: return 'False'
									elif obj[1]>2:
										# {"feature": "Bar", "instances": 36, "metric_value": 0.4214, "depth": 10}
										if obj[8]<=1.0:
											# {"feature": "Children", "instances": 25, "metric_value": 0.384, "depth": 11}
											if obj[5]>0:
												# {"feature": "Restaurant20to50", "instances": 15, "metric_value": 0.28, "depth": 12}
												if obj[10]<=1.0:
													# {"feature": "Direction_same", "instances": 10, "metric_value": 0.4, "depth": 13}
													if obj[11]<=0:
														return 'True'
													elif obj[11]>0:
														return 'True'
													else: return 'True'
												elif obj[10]>1.0:
													return 'True'
												else: return 'True'
											elif obj[5]<=0:
												# {"feature": "Restaurant20to50", "instances": 10, "metric_value": 0.4444, "depth": 12}
												if obj[10]>0.0:
													# {"feature": "Direction_same", "instances": 9, "metric_value": 0.4815, "depth": 13}
													if obj[11]<=0:
														return 'True'
													elif obj[11]>0:
														return 'True'
													else: return 'True'
												elif obj[10]<=0.0:
													return 'True'
												else: return 'True'
											else: return 'True'
										elif obj[8]>1.0:
											# {"feature": "Direction_same", "instances": 11, "metric_value": 0.4182, "depth": 11}
											if obj[11]<=0:
												# {"feature": "Children", "instances": 6, "metric_value": 0.5, "depth": 12}
												if obj[5]<=0:
													# {"feature": "Restaurant20to50", "instances": 4, "metric_value": 0.5, "depth": 13}
													if obj[10]<=2.0:
														return 'False'
													else: return 'False'
												elif obj[5]>0:
													# {"feature": "Restaurant20to50", "instances": 2, "metric_value": 0.5, "depth": 13}
													if obj[10]<=2.0:
														return 'True'
													else: return 'True'
												else: return 'True'
											elif obj[11]>0:
												# {"feature": "Children", "instances": 5, "metric_value": 0.2667, "depth": 12}
												if obj[5]<=0:
													# {"feature": "Restaurant20to50", "instances": 3, "metric_value": 0.4444, "depth": 13}
													if obj[10]<=2.0:
														return 'False'
													else: return 'False'
												elif obj[5]>0:
													return 'False'
												else: return 'False'
											else: return 'False'
										else: return 'False'
									else: return 'True'
								elif obj[7]>13:
									# {"feature": "Time", "instances": 7, "metric_value": 0.1429, "depth": 9}
									if obj[1]<=2:
										return 'False'
									elif obj[1]>2:
										# {"feature": "Direction_same", "instances": 2, "metric_value": 0.0, "depth": 10}
										if obj[11]>0:
											return 'True'
										elif obj[11]<=0:
											return 'False'
										else: return 'False'
									else: return 'True'
								else: return 'False'
							else: return 'True'
						else: return 'True'
					else: return 'True'
				elif obj[0]>2:
					# {"feature": "Bar", "instances": 1390, "metric_value": 0.3797, "depth": 5}
					if obj[8]<=3.0:
						# {"feature": "Age", "instances": 1328, "metric_value": 0.3739, "depth": 6}
						if obj[4]<=4:
							# {"feature": "Occupation", "instances": 1062, "metric_value": 0.3836, "depth": 7}
							if obj[7]>1:
								# {"feature": "Education", "instances": 904, "metric_value": 0.3983, "depth": 8}
								if obj[6]<=3:
									# {"feature": "Time", "instances": 845, "metric_value": 0.4078, "depth": 9}
									if obj[1]<=2:
										# {"feature": "Restaurant20to50", "instances": 521, "metric_value": 0.3854, "depth": 10}
										if obj[10]<=1.0:
											# {"feature": "Children", "instances": 349, "metric_value": 0.4083, "depth": 11}
											if obj[5]<=0:
												# {"feature": "Gender", "instances": 212, "metric_value": 0.3971, "depth": 12}
												if obj[3]<=0:
													# {"feature": "Direction_same", "instances": 115, "metric_value": 0.3856, "depth": 13}
													if obj[11]<=0:
														return 'True'
													else: return 'True'
												elif obj[3]>0:
													# {"feature": "Direction_same", "instances": 97, "metric_value": 0.4107, "depth": 13}
													if obj[11]<=0:
														return 'True'
													else: return 'True'
												else: return 'True'
											elif obj[5]>0:
												# {"feature": "Gender", "instances": 137, "metric_value": 0.4238, "depth": 12}
												if obj[3]>0:
													# {"feature": "Direction_same", "instances": 84, "metric_value": 0.4082, "depth": 13}
													if obj[11]<=0:
														return 'True'
													else: return 'True'
												elif obj[3]<=0:
													# {"feature": "Direction_same", "instances": 53, "metric_value": 0.4486, "depth": 13}
													if obj[11]<=0:
														return 'True'
													else: return 'True'
												else: return 'True'
											else: return 'True'
										elif obj[10]>1.0:
											# {"feature": "Children", "instances": 172, "metric_value": 0.3367, "depth": 11}
											if obj[5]<=0:
												# {"feature": "Gender", "instances": 122, "metric_value": 0.3536, "depth": 12}
												if obj[3]>0:
													# {"feature": "Direction_same", "instances": 67, "metric_value": 0.3475, "depth": 13}
													if obj[11]<=0:
														return 'True'
													else: return 'True'
												elif obj[3]<=0:
													# {"feature": "Direction_same", "instances": 55, "metric_value": 0.361, "depth": 13}
													if obj[11]<=0:
														return 'True'
													else: return 'True'
												else: return 'True'
											elif obj[5]>0:
												# {"feature": "Gender", "instances": 50, "metric_value": 0.294, "depth": 12}
												if obj[3]>0:
													# {"feature": "Direction_same", "instances": 30, "metric_value": 0.32, "depth": 13}
													if obj[11]<=0:
														return 'True'
													else: return 'True'
												elif obj[3]<=0:
													# {"feature": "Direction_same", "instances": 20, "metric_value": 0.255, "depth": 13}
													if obj[11]<=0:
														return 'True'
													else: return 'True'
												else: return 'True'
											else: return 'True'
										else: return 'True'
									elif obj[1]>2:
										# {"feature": "Restaurant20to50", "instances": 324, "metric_value": 0.4372, "depth": 10}
										if obj[10]<=1.0:
											# {"feature": "Children", "instances": 211, "metric_value": 0.4177, "depth": 11}
											if obj[5]<=0:
												# {"feature": "Gender", "instances": 119, "metric_value": 0.3993, "depth": 12}
												if obj[3]<=0:
													# {"feature": "Direction_same", "instances": 60, "metric_value": 0.375, "depth": 13}
													if obj[11]<=0:
														return 'True'
													else: return 'True'
												elif obj[3]>0:
													# {"feature": "Direction_same", "instances": 59, "metric_value": 0.424, "depth": 13}
													if obj[11]<=0:
														return 'True'
													else: return 'True'
												else: return 'True'
											elif obj[5]>0:
												# {"feature": "Gender", "instances": 92, "metric_value": 0.4395, "depth": 12}
												if obj[3]>0:
													# {"feature": "Direction_same", "instances": 58, "metric_value": 0.4405, "depth": 13}
													if obj[11]<=0:
														return 'True'
													else: return 'True'
												elif obj[3]<=0:
													# {"feature": "Direction_same", "instances": 34, "metric_value": 0.4377, "depth": 13}
													if obj[11]<=0:
														return 'True'
													else: return 'True'
												else: return 'True'
											else: return 'True'
										elif obj[10]>1.0:
											# {"feature": "Children", "instances": 113, "metric_value": 0.4686, "depth": 11}
											if obj[5]<=0:
												# {"feature": "Gender", "instances": 66, "metric_value": 0.4537, "depth": 12}
												if obj[3]>0:
													# {"feature": "Direction_same", "instances": 36, "metric_value": 0.4614, "depth": 13}
													if obj[11]<=0:
														return 'True'
													else: return 'True'
												elif obj[3]<=0:
													# {"feature": "Direction_same", "instances": 30, "metric_value": 0.4444, "depth": 13}
													if obj[11]<=0:
														return 'True'
													else: return 'True'
												else: return 'True'
											elif obj[5]>0:
												# {"feature": "Gender", "instances": 47, "metric_value": 0.4876, "depth": 12}
												if obj[3]>0:
													# {"feature": "Direction_same", "instances": 34, "metric_value": 0.4931, "depth": 13}
													if obj[11]<=0:
														return 'True'
													else: return 'True'
												elif obj[3]<=0:
													# {"feature": "Direction_same", "instances": 13, "metric_value": 0.4734, "depth": 13}
													if obj[11]<=0:
														return 'True'
													else: return 'True'
												else: return 'True'
											else: return 'True'
										else: return 'True'
									else: return 'True'
								elif obj[6]>3:
									# {"feature": "Restaurant20to50", "instances": 59, "metric_value": 0.2207, "depth": 9}
									if obj[10]>0.0:
										# {"feature": "Gender", "instances": 43, "metric_value": 0.2925, "depth": 10}
										if obj[3]>0:
											# {"feature": "Time", "instances": 30, "metric_value": 0.3492, "depth": 11}
											if obj[1]>0:
												# {"feature": "Children", "instances": 22, "metric_value": 0.3916, "depth": 12}
												if obj[5]<=0:
													# {"feature": "Direction_same", "instances": 13, "metric_value": 0.355, "depth": 13}
													if obj[11]<=0:
														return 'True'
													else: return 'True'
												elif obj[5]>0:
													# {"feature": "Direction_same", "instances": 9, "metric_value": 0.4444, "depth": 13}
													if obj[11]<=0:
														return 'True'
													else: return 'True'
												else: return 'True'
											elif obj[1]<=0:
												# {"feature": "Children", "instances": 8, "metric_value": 0.1875, "depth": 12}
												if obj[5]<=0:
													return 'True'
												elif obj[5]>0:
													# {"feature": "Direction_same", "instances": 4, "metric_value": 0.375, "depth": 13}
													if obj[11]<=0:
														return 'True'
													else: return 'True'
												else: return 'True'
											else: return 'True'
										elif obj[3]<=0:
											# {"feature": "Children", "instances": 13, "metric_value": 0.1282, "depth": 11}
											if obj[5]>0:
												return 'True'
											elif obj[5]<=0:
												# {"feature": "Time", "instances": 6, "metric_value": 0.2667, "depth": 12}
												if obj[1]>0:
													# {"feature": "Direction_same", "instances": 5, "metric_value": 0.32, "depth": 13}
													if obj[11]<=0:
														return 'True'
													else: return 'True'
												elif obj[1]<=0:
													return 'True'
												else: return 'True'
											else: return 'True'
										else: return 'True'
									elif obj[10]<=0.0:
										return 'True'
									else: return 'True'
								else: return 'True'
							elif obj[7]<=1:
								# {"feature": "Education", "instances": 158, "metric_value": 0.2746, "depth": 8}
								if obj[6]<=4:
									# {"feature": "Restaurant20to50", "instances": 157, "metric_value": 0.2667, "depth": 9}
									if obj[10]<=1.0:
										# {"feature": "Gender", "instances": 116, "metric_value": 0.3243, "depth": 10}
										if obj[3]>0:
											# {"feature": "Time", "instances": 65, "metric_value": 0.3663, "depth": 11}
											if obj[1]<=3:
												# {"feature": "Children", "instances": 47, "metric_value": 0.4001, "depth": 12}
												if obj[5]>0:
													# {"feature": "Direction_same", "instances": 32, "metric_value": 0.4043, "depth": 13}
													if obj[11]<=0:
														return 'True'
													else: return 'True'
												elif obj[5]<=0:
													# {"feature": "Direction_same", "instances": 15, "metric_value": 0.3911, "depth": 13}
													if obj[11]<=0:
														return 'True'
													else: return 'True'
												else: return 'True'
											elif obj[1]>3:
												# {"feature": "Children", "instances": 18, "metric_value": 0.2771, "depth": 12}
												if obj[5]>0:
													# {"feature": "Direction_same", "instances": 11, "metric_value": 0.2975, "depth": 13}
													if obj[11]<=0:
														return 'True'
													else: return 'True'
												elif obj[5]<=0:
													# {"feature": "Direction_same", "instances": 7, "metric_value": 0.2449, "depth": 13}
													if obj[11]<=0:
														return 'True'
													else: return 'True'
												else: return 'True'
											else: return 'True'
										elif obj[3]<=0:
											# {"feature": "Time", "instances": 51, "metric_value": 0.2598, "depth": 11}
											if obj[1]<=2:
												# {"feature": "Children", "instances": 27, "metric_value": 0.1966, "depth": 12}
												if obj[5]<=0:
													# {"feature": "Direction_same", "instances": 26, "metric_value": 0.2041, "depth": 13}
													if obj[11]<=0:
														return 'True'
													else: return 'True'
												elif obj[5]>0:
													return 'True'
												else: return 'True'
											elif obj[1]>2:
												# {"feature": "Children", "instances": 24, "metric_value": 0.3299, "depth": 12}
												if obj[5]<=0:
													# {"feature": "Direction_same", "instances": 24, "metric_value": 0.3299, "depth": 13}
													if obj[11]<=0:
														return 'True'
													else: return 'True'
												else: return 'True'
											else: return 'True'
										else: return 'True'
									elif obj[10]>1.0:
										# {"feature": "Children", "instances": 41, "metric_value": 0.0906, "depth": 10}
										if obj[5]<=0:
											# {"feature": "Time", "instances": 28, "metric_value": 0.1293, "depth": 11}
											if obj[1]<=3:
												# {"feature": "Gender", "instances": 21, "metric_value": 0.0905, "depth": 12}
												if obj[3]>0:
													# {"feature": "Direction_same", "instances": 20, "metric_value": 0.095, "depth": 13}
													if obj[11]<=0:
														return 'True'
													else: return 'True'
												elif obj[3]<=0:
													return 'True'
												else: return 'True'
											elif obj[1]>3:
												# {"feature": "Gender", "instances": 7, "metric_value": 0.2449, "depth": 12}
												if obj[3]<=1:
													# {"feature": "Direction_same", "instances": 7, "metric_value": 0.2449, "depth": 13}
													if obj[11]<=0:
														return 'True'
													else: return 'True'
												else: return 'True'
											else: return 'True'
										elif obj[5]>0:
											return 'True'
										else: return 'True'
									else: return 'True'
								elif obj[6]>4:
									return 'False'
								else: return 'False'
							else: return 'True'
						elif obj[4]>4:
							# {"feature": "Education", "instances": 266, "metric_value": 0.3186, "depth": 7}
							if obj[6]<=1:
								# {"feature": "Occupation", "instances": 136, "metric_value": 0.2522, "depth": 8}
								if obj[7]>5:
									# {"feature": "Restaurant20to50", "instances": 103, "metric_value": 0.1977, "depth": 9}
									if obj[10]<=2.0:
										# {"feature": "Time", "instances": 98, "metric_value": 0.1819, "depth": 10}
										if obj[1]>0:
											# {"feature": "Children", "instances": 78, "metric_value": 0.203, "depth": 11}
											if obj[5]<=0:
												# {"feature": "Gender", "instances": 59, "metric_value": 0.1806, "depth": 12}
												if obj[3]<=0:
													# {"feature": "Direction_same", "instances": 47, "metric_value": 0.1557, "depth": 13}
													if obj[11]<=0:
														return 'True'
													else: return 'True'
												elif obj[3]>0:
													# {"feature": "Direction_same", "instances": 12, "metric_value": 0.2778, "depth": 13}
													if obj[11]<=0:
														return 'True'
													else: return 'True'
												else: return 'True'
											elif obj[5]>0:
												# {"feature": "Gender", "instances": 19, "metric_value": 0.2481, "depth": 12}
												if obj[3]<=0:
													# {"feature": "Direction_same", "instances": 14, "metric_value": 0.3367, "depth": 13}
													if obj[11]<=0:
														return 'True'
													else: return 'True'
												elif obj[3]>0:
													return 'True'
												else: return 'True'
											else: return 'True'
										elif obj[1]<=0:
											# {"feature": "Gender", "instances": 20, "metric_value": 0.0933, "depth": 11}
											if obj[3]<=0:
												# {"feature": "Children", "instances": 15, "metric_value": 0.1212, "depth": 12}
												if obj[5]<=0:
													# {"feature": "Direction_same", "instances": 11, "metric_value": 0.1653, "depth": 13}
													if obj[11]<=0:
														return 'True'
													else: return 'True'
												elif obj[5]>0:
													return 'True'
												else: return 'True'
											elif obj[3]>0:
												return 'True'
											else: return 'True'
										else: return 'True'
									elif obj[10]>2.0:
										# {"feature": "Gender", "instances": 5, "metric_value": 0.2667, "depth": 10}
										if obj[3]<=0:
											# {"feature": "Time", "instances": 3, "metric_value": 0.3333, "depth": 11}
											if obj[1]<=2:
												# {"feature": "Children", "instances": 2, "metric_value": 0.5, "depth": 12}
												if obj[5]<=0:
													# {"feature": "Direction_same", "instances": 2, "metric_value": 0.5, "depth": 13}
													if obj[11]<=0:
														return 'True'
													else: return 'True'
												else: return 'True'
											elif obj[1]>2:
												return 'False'
											else: return 'False'
										elif obj[3]>0:
											return 'True'
										else: return 'True'
									else: return 'True'
								elif obj[7]<=5:
									# {"feature": "Gender", "instances": 33, "metric_value": 0.3409, "depth": 9}
									if obj[3]>0:
										# {"feature": "Children", "instances": 24, "metric_value": 0.4125, "depth": 10}
										if obj[5]>0:
											# {"feature": "Time", "instances": 20, "metric_value": 0.375, "depth": 11}
											if obj[1]<=2:
												# {"feature": "Restaurant20to50", "instances": 16, "metric_value": 0.4375, "depth": 12}
												if obj[10]>1.0:
													# {"feature": "Direction_same", "instances": 8, "metric_value": 0.5, "depth": 13}
													if obj[11]<=0:
														return 'False'
													else: return 'False'
												elif obj[10]<=1.0:
													# {"feature": "Direction_same", "instances": 8, "metric_value": 0.375, "depth": 13}
													if obj[11]<=0:
														return 'True'
													else: return 'True'
												else: return 'True'
											elif obj[1]>2:
												return 'True'
											else: return 'True'
										elif obj[5]<=0:
											# {"feature": "Time", "instances": 4, "metric_value": 0.3333, "depth": 11}
											if obj[1]>0:
												# {"feature": "Restaurant20to50", "instances": 3, "metric_value": 0.4444, "depth": 12}
												if obj[10]<=1.0:
													# {"feature": "Direction_same", "instances": 3, "metric_value": 0.4444, "depth": 13}
													if obj[11]<=0:
														return 'False'
													else: return 'False'
												else: return 'False'
											elif obj[1]<=0:
												return 'False'
											else: return 'False'
										else: return 'False'
									elif obj[3]<=0:
										return 'True'
									else: return 'True'
								else: return 'True'
							elif obj[6]>1:
								# {"feature": "Time", "instances": 130, "metric_value": 0.373, "depth": 8}
								if obj[1]<=2:
									# {"feature": "Occupation", "instances": 73, "metric_value": 0.3936, "depth": 9}
									if obj[7]<=19:
										# {"feature": "Restaurant20to50", "instances": 71, "metric_value": 0.3941, "depth": 10}
										if obj[10]>0.0:
											# {"feature": "Children", "instances": 57, "metric_value": 0.3703, "depth": 11}
											if obj[5]>0:
												# {"feature": "Gender", "instances": 34, "metric_value": 0.3446, "depth": 12}
												if obj[3]>0:
													# {"feature": "Direction_same", "instances": 24, "metric_value": 0.4132, "depth": 13}
													if obj[11]<=0:
														return 'True'
													else: return 'True'
												elif obj[3]<=0:
													# {"feature": "Direction_same", "instances": 10, "metric_value": 0.18, "depth": 13}
													if obj[11]<=0:
														return 'True'
													else: return 'True'
												else: return 'True'
											elif obj[5]<=0:
												# {"feature": "Gender", "instances": 23, "metric_value": 0.3568, "depth": 12}
												if obj[3]<=0:
													# {"feature": "Direction_same", "instances": 14, "metric_value": 0.4592, "depth": 13}
													if obj[11]<=0:
														return 'True'
													else: return 'True'
												elif obj[3]>0:
													# {"feature": "Direction_same", "instances": 9, "metric_value": 0.1975, "depth": 13}
													if obj[11]<=0:
														return 'True'
													else: return 'True'
												else: return 'True'
											else: return 'True'
										elif obj[10]<=0.0:
											# {"feature": "Gender", "instances": 14, "metric_value": 0.449, "depth": 11}
											if obj[3]>0:
												# {"feature": "Children", "instances": 7, "metric_value": 0.3429, "depth": 12}
												if obj[5]<=0:
													# {"feature": "Direction_same", "instances": 5, "metric_value": 0.48, "depth": 13}
													if obj[11]<=0:
														return 'True'
													else: return 'True'
												elif obj[5]>0:
													return 'True'
												else: return 'True'
											elif obj[3]<=0:
												# {"feature": "Children", "instances": 7, "metric_value": 0.4762, "depth": 12}
												if obj[5]<=0:
													# {"feature": "Direction_same", "instances": 4, "metric_value": 0.5, "depth": 13}
													if obj[11]<=0:
														return 'False'
													else: return 'False'
												elif obj[5]>0:
													# {"feature": "Direction_same", "instances": 3, "metric_value": 0.4444, "depth": 13}
													if obj[11]<=0:
														return 'False'
													else: return 'False'
												else: return 'False'
											else: return 'False'
										else: return 'True'
									elif obj[7]>19:
										return 'False'
									else: return 'False'
								elif obj[1]>2:
									# {"feature": "Occupation", "instances": 57, "metric_value": 0.3011, "depth": 9}
									if obj[7]<=12:
										# {"feature": "Restaurant20to50", "instances": 50, "metric_value": 0.3398, "depth": 10}
										if obj[10]>0.0:
											# {"feature": "Children", "instances": 42, "metric_value": 0.3558, "depth": 11}
											if obj[5]<=0:
												# {"feature": "Gender", "instances": 22, "metric_value": 0.2938, "depth": 12}
												if obj[3]<=0:
													# {"feature": "Direction_same", "instances": 14, "metric_value": 0.3367, "depth": 13}
													if obj[11]<=0:
														return 'True'
													else: return 'True'
												elif obj[3]>0:
													# {"feature": "Direction_same", "instances": 8, "metric_value": 0.2188, "depth": 13}
													if obj[11]<=0:
														return 'True'
													else: return 'True'
												else: return 'True'
											elif obj[5]>0:
												# {"feature": "Gender", "instances": 20, "metric_value": 0.4182, "depth": 12}
												if obj[3]<=0:
													# {"feature": "Direction_same", "instances": 11, "metric_value": 0.3967, "depth": 13}
													if obj[11]<=0:
														return 'True'
													else: return 'True'
												elif obj[3]>0:
													# {"feature": "Direction_same", "instances": 9, "metric_value": 0.4444, "depth": 13}
													if obj[11]<=0:
														return 'True'
													else: return 'True'
												else: return 'True'
											else: return 'True'
										elif obj[10]<=0.0:
											# {"feature": "Gender", "instances": 8, "metric_value": 0.1667, "depth": 11}
											if obj[3]>0:
												return 'True'
											elif obj[3]<=0:
												# {"feature": "Children", "instances": 3, "metric_value": 0.3333, "depth": 12}
												if obj[5]<=0:
													# {"feature": "Direction_same", "instances": 2, "metric_value": 0.5, "depth": 13}
													if obj[11]<=0:
														return 'False'
													else: return 'False'
												elif obj[5]>0:
													return 'True'
												else: return 'True'
											else: return 'True'
										else: return 'True'
									elif obj[7]>12:
										return 'True'
									else: return 'True'
								else: return 'True'
							else: return 'True'
						else: return 'True'
					elif obj[8]>3.0:
						# {"feature": "Occupation", "instances": 62, "metric_value": 0.437, "depth": 6}
						if obj[7]<=12:
							# {"feature": "Age", "instances": 47, "metric_value": 0.3928, "depth": 7}
							if obj[4]>0:
								# {"feature": "Gender", "instances": 39, "metric_value": 0.4538, "depth": 8}
								if obj[3]<=0:
									# {"feature": "Time", "instances": 21, "metric_value": 0.4636, "depth": 9}
									if obj[1]>0:
										# {"feature": "Education", "instances": 17, "metric_value": 0.4843, "depth": 10}
										if obj[6]>2:
											# {"feature": "Children", "instances": 12, "metric_value": 0.4861, "depth": 11}
											if obj[5]<=0:
												# {"feature": "Restaurant20to50", "instances": 12, "metric_value": 0.4861, "depth": 12}
												if obj[10]<=4.0:
													# {"feature": "Direction_same", "instances": 12, "metric_value": 0.4861, "depth": 13}
													if obj[11]<=0:
														return 'True'
													else: return 'True'
												else: return 'True'
											else: return 'True'
										elif obj[6]<=2:
											# {"feature": "Children", "instances": 5, "metric_value": 0.48, "depth": 11}
											if obj[5]<=0:
												# {"feature": "Restaurant20to50", "instances": 5, "metric_value": 0.48, "depth": 12}
												if obj[10]<=1.0:
													# {"feature": "Direction_same", "instances": 5, "metric_value": 0.48, "depth": 13}
													if obj[11]<=0:
														return 'True'
													else: return 'True'
												else: return 'True'
											else: return 'True'
										else: return 'True'
									elif obj[1]<=0:
										# {"feature": "Education", "instances": 4, "metric_value": 0.3333, "depth": 10}
										if obj[6]>2:
											# {"feature": "Children", "instances": 3, "metric_value": 0.4444, "depth": 11}
											if obj[5]<=0:
												# {"feature": "Restaurant20to50", "instances": 3, "metric_value": 0.4444, "depth": 12}
												if obj[10]<=4.0:
													# {"feature": "Direction_same", "instances": 3, "metric_value": 0.4444, "depth": 13}
													if obj[11]<=0:
														return 'False'
													else: return 'False'
												else: return 'False'
											else: return 'False'
										elif obj[6]<=2:
											return 'False'
										else: return 'False'
									else: return 'False'
								elif obj[3]>0:
									# {"feature": "Education", "instances": 18, "metric_value": 0.3951, "depth": 9}
									if obj[6]<=0:
										# {"feature": "Time", "instances": 9, "metric_value": 0.3016, "depth": 10}
										if obj[1]>0:
											# {"feature": "Restaurant20to50", "instances": 7, "metric_value": 0.2286, "depth": 11}
											if obj[10]>0.0:
												# {"feature": "Children", "instances": 5, "metric_value": 0.32, "depth": 12}
												if obj[5]<=0:
													# {"feature": "Direction_same", "instances": 5, "metric_value": 0.32, "depth": 13}
													if obj[11]<=0:
														return 'True'
													else: return 'True'
												else: return 'True'
											elif obj[10]<=0.0:
												return 'True'
											else: return 'True'
										elif obj[1]<=0:
											# {"feature": "Restaurant20to50", "instances": 2, "metric_value": 0.0, "depth": 11}
											if obj[10]<=0.0:
												return 'False'
											elif obj[10]>0.0:
												return 'True'
											else: return 'True'
										else: return 'False'
									elif obj[6]>0:
										# {"feature": "Restaurant20to50", "instances": 9, "metric_value": 0.381, "depth": 10}
										if obj[10]>0.0:
											# {"feature": "Time", "instances": 7, "metric_value": 0.4762, "depth": 11}
											if obj[1]>0:
												# {"feature": "Children", "instances": 4, "metric_value": 0.5, "depth": 12}
												if obj[5]<=0:
													# {"feature": "Direction_same", "instances": 4, "metric_value": 0.5, "depth": 13}
													if obj[11]<=0:
														return 'True'
													else: return 'True'
												else: return 'True'
											elif obj[1]<=0:
												# {"feature": "Children", "instances": 3, "metric_value": 0.4444, "depth": 12}
												if obj[5]<=0:
													# {"feature": "Direction_same", "instances": 3, "metric_value": 0.4444, "depth": 13}
													if obj[11]<=0:
														return 'True'
													else: return 'True'
												else: return 'True'
											else: return 'True'
										elif obj[10]<=0.0:
											return 'True'
										else: return 'True'
									else: return 'True'
								else: return 'True'
							elif obj[4]<=0:
								return 'True'
							else: return 'True'
						elif obj[7]>12:
							# {"feature": "Time", "instances": 15, "metric_value": 0.3333, "depth": 7}
							if obj[1]>0:
								# {"feature": "Gender", "instances": 10, "metric_value": 0.4444, "depth": 8}
								if obj[3]<=0:
									# {"feature": "Age", "instances": 9, "metric_value": 0.4889, "depth": 9}
									if obj[4]<=1:
										# {"feature": "Children", "instances": 5, "metric_value": 0.48, "depth": 10}
										if obj[5]<=0:
											# {"feature": "Education", "instances": 5, "metric_value": 0.48, "depth": 11}
											if obj[6]<=0:
												# {"feature": "Restaurant20to50", "instances": 5, "metric_value": 0.48, "depth": 12}
												if obj[10]<=4.0:
													# {"feature": "Direction_same", "instances": 5, "metric_value": 0.48, "depth": 13}
													if obj[11]<=0:
														return 'True'
													else: return 'True'
												else: return 'True'
											else: return 'True'
										else: return 'True'
									elif obj[4]>1:
										# {"feature": "Children", "instances": 4, "metric_value": 0.5, "depth": 10}
										if obj[5]<=0:
											# {"feature": "Education", "instances": 4, "metric_value": 0.5, "depth": 11}
											if obj[6]<=0:
												# {"feature": "Restaurant20to50", "instances": 4, "metric_value": 0.5, "depth": 12}
												if obj[10]<=1.0:
													# {"feature": "Direction_same", "instances": 4, "metric_value": 0.5, "depth": 13}
													if obj[11]<=0:
														return 'True'
													else: return 'True'
												else: return 'True'
											else: return 'True'
										else: return 'True'
									else: return 'True'
								elif obj[3]>0:
									return 'False'
								else: return 'False'
							elif obj[1]<=0:
								return 'False'
							else: return 'False'
						else: return 'False'
					else: return 'True'
				else: return 'True'
			elif obj[12]>2:
				# {"feature": "Passanger", "instances": 435, "metric_value": 0.485, "depth": 4}
				if obj[0]>0:
					# {"feature": "Education", "instances": 419, "metric_value": 0.484, "depth": 5}
					if obj[6]>0:
						# {"feature": "Age", "instances": 281, "metric_value": 0.4651, "depth": 6}
						if obj[4]<=4:
							# {"feature": "Time", "instances": 243, "metric_value": 0.477, "depth": 7}
							if obj[1]>0:
								# {"feature": "Restaurant20to50", "instances": 211, "metric_value": 0.4925, "depth": 8}
								if obj[10]<=2.0:
									# {"feature": "Bar", "instances": 189, "metric_value": 0.4944, "depth": 9}
									if obj[8]>-1.0:
										# {"feature": "Occupation", "instances": 187, "metric_value": 0.4977, "depth": 10}
										if obj[7]>1:
											# {"feature": "Children", "instances": 145, "metric_value": 0.4994, "depth": 11}
											if obj[5]<=0:
												# {"feature": "Gender", "instances": 87, "metric_value": 0.4994, "depth": 12}
												if obj[3]<=0:
													# {"feature": "Direction_same", "instances": 50, "metric_value": 0.4992, "depth": 13}
													if obj[11]<=0:
														return 'True'
													else: return 'True'
												elif obj[3]>0:
													# {"feature": "Direction_same", "instances": 37, "metric_value": 0.4996, "depth": 13}
													if obj[11]<=0:
														return 'True'
													else: return 'True'
												else: return 'True'
											elif obj[5]>0:
												# {"feature": "Gender", "instances": 58, "metric_value": 0.4986, "depth": 12}
												if obj[3]>0:
													# {"feature": "Direction_same", "instances": 34, "metric_value": 0.5, "depth": 13}
													if obj[11]<=0:
														return 'False'
													else: return 'False'
												elif obj[3]<=0:
													# {"feature": "Direction_same", "instances": 24, "metric_value": 0.4965, "depth": 13}
													if obj[11]<=0:
														return 'False'
													else: return 'False'
												else: return 'False'
											else: return 'False'
										elif obj[7]<=1:
											# {"feature": "Children", "instances": 42, "metric_value": 0.4694, "depth": 11}
											if obj[5]<=0:
												# {"feature": "Gender", "instances": 28, "metric_value": 0.4579, "depth": 12}
												if obj[3]>0:
													# {"feature": "Direction_same", "instances": 15, "metric_value": 0.4444, "depth": 13}
													if obj[11]<=0:
														return 'False'
													else: return 'False'
												elif obj[3]<=0:
													# {"feature": "Direction_same", "instances": 13, "metric_value": 0.4734, "depth": 13}
													if obj[11]<=0:
														return 'False'
													else: return 'False'
												else: return 'False'
											elif obj[5]>0:
												# {"feature": "Gender", "instances": 14, "metric_value": 0.4615, "depth": 12}
												if obj[3]>0:
													# {"feature": "Direction_same", "instances": 13, "metric_value": 0.497, "depth": 13}
													if obj[11]<=0:
														return 'True'
													else: return 'True'
												elif obj[3]<=0:
													return 'True'
												else: return 'True'
											else: return 'True'
										else: return 'False'
									elif obj[8]<=-1.0:
										return 'False'
									else: return 'False'
								elif obj[10]>2.0:
									# {"feature": "Children", "instances": 22, "metric_value": 0.3545, "depth": 9}
									if obj[5]<=0:
										# {"feature": "Bar", "instances": 12, "metric_value": 0.3714, "depth": 10}
										if obj[8]<=2.0:
											# {"feature": "Occupation", "instances": 7, "metric_value": 0.2857, "depth": 11}
											if obj[7]>6:
												# {"feature": "Gender", "instances": 4, "metric_value": 0.5, "depth": 12}
												if obj[3]<=0:
													# {"feature": "Direction_same", "instances": 2, "metric_value": 0.5, "depth": 13}
													if obj[11]<=0:
														return 'False'
													else: return 'False'
												elif obj[3]>0:
													# {"feature": "Direction_same", "instances": 2, "metric_value": 0.5, "depth": 13}
													if obj[11]<=0:
														return 'False'
													else: return 'False'
												else: return 'False'
											elif obj[7]<=6:
												return 'True'
											else: return 'True'
										elif obj[8]>2.0:
											# {"feature": "Occupation", "instances": 5, "metric_value": 0.3, "depth": 11}
											if obj[7]<=1:
												# {"feature": "Gender", "instances": 4, "metric_value": 0.375, "depth": 12}
												if obj[3]<=0:
													# {"feature": "Direction_same", "instances": 4, "metric_value": 0.375, "depth": 13}
													if obj[11]<=0:
														return 'False'
													else: return 'False'
												else: return 'False'
											elif obj[7]>1:
												return 'False'
											else: return 'False'
										else: return 'False'
									elif obj[5]>0:
										# {"feature": "Bar", "instances": 10, "metric_value": 0.0, "depth": 10}
										if obj[8]<=3.0:
											return 'False'
										elif obj[8]>3.0:
											return 'True'
										else: return 'True'
									else: return 'False'
								else: return 'False'
							elif obj[1]<=0:
								# {"feature": "Occupation", "instances": 32, "metric_value": 0.2983, "depth": 8}
								if obj[7]<=9:
									# {"feature": "Bar", "instances": 22, "metric_value": 0.3545, "depth": 9}
									if obj[8]<=1.0:
										# {"feature": "Children", "instances": 12, "metric_value": 0.3714, "depth": 10}
										if obj[5]<=0:
											# {"feature": "Restaurant20to50", "instances": 7, "metric_value": 0.3429, "depth": 11}
											if obj[10]<=1.0:
												# {"feature": "Gender", "instances": 5, "metric_value": 0.4667, "depth": 12}
												if obj[3]>0:
													# {"feature": "Direction_same", "instances": 3, "metric_value": 0.4444, "depth": 13}
													if obj[11]<=0:
														return 'True'
													else: return 'True'
												elif obj[3]<=0:
													# {"feature": "Direction_same", "instances": 2, "metric_value": 0.5, "depth": 13}
													if obj[11]<=0:
														return 'False'
													else: return 'False'
												else: return 'False'
											elif obj[10]>1.0:
												return 'True'
											else: return 'True'
										elif obj[5]>0:
											# {"feature": "Gender", "instances": 5, "metric_value": 0.2, "depth": 11}
											if obj[3]<=0:
												return 'False'
											elif obj[3]>0:
												# {"feature": "Restaurant20to50", "instances": 2, "metric_value": 0.5, "depth": 12}
												if obj[10]<=2.0:
													# {"feature": "Direction_same", "instances": 2, "metric_value": 0.5, "depth": 13}
													if obj[11]<=0:
														return 'False'
													else: return 'False'
												else: return 'False'
											else: return 'False'
										else: return 'False'
									elif obj[8]>1.0:
										# {"feature": "Gender", "instances": 10, "metric_value": 0.15, "depth": 10}
										if obj[3]>0:
											return 'False'
										elif obj[3]<=0:
											# {"feature": "Restaurant20to50", "instances": 4, "metric_value": 0.25, "depth": 11}
											if obj[10]<=0.0:
												return 'False'
											elif obj[10]>0.0:
												# {"feature": "Children", "instances": 2, "metric_value": 0.5, "depth": 12}
												if obj[5]<=0:
													# {"feature": "Direction_same", "instances": 2, "metric_value": 0.5, "depth": 13}
													if obj[11]<=0:
														return 'True'
													else: return 'True'
												else: return 'True'
											else: return 'True'
										else: return 'False'
									else: return 'False'
								elif obj[7]>9:
									return 'False'
								else: return 'False'
							else: return 'False'
						elif obj[4]>4:
							# {"feature": "Occupation", "instances": 38, "metric_value": 0.2545, "depth": 7}
							if obj[7]<=7:
								# {"feature": "Time", "instances": 21, "metric_value": 0.0833, "depth": 8}
								if obj[1]<=1:
									return 'False'
								elif obj[1]>1:
									# {"feature": "Bar", "instances": 8, "metric_value": 0.1667, "depth": 9}
									if obj[8]<=0.0:
										return 'False'
									elif obj[8]>0.0:
										# {"feature": "Children", "instances": 3, "metric_value": 0.3333, "depth": 10}
										if obj[5]<=0:
											# {"feature": "Gender", "instances": 2, "metric_value": 0.5, "depth": 11}
											if obj[3]<=1:
												# {"feature": "Restaurant20to50", "instances": 2, "metric_value": 0.5, "depth": 12}
												if obj[10]<=1.0:
													# {"feature": "Direction_same", "instances": 2, "metric_value": 0.5, "depth": 13}
													if obj[11]<=0:
														return 'True'
													else: return 'True'
												else: return 'True'
											else: return 'True'
										elif obj[5]>0:
											return 'False'
										else: return 'False'
									else: return 'False'
								else: return 'False'
							elif obj[7]>7:
								# {"feature": "Time", "instances": 17, "metric_value": 0.4412, "depth": 8}
								if obj[1]<=1:
									# {"feature": "Gender", "instances": 16, "metric_value": 0.4295, "depth": 9}
									if obj[3]<=0:
										# {"feature": "Bar", "instances": 13, "metric_value": 0.3487, "depth": 10}
										if obj[8]<=1.0:
											# {"feature": "Children", "instances": 10, "metric_value": 0.1778, "depth": 11}
											if obj[5]>0:
												# {"feature": "Restaurant20to50", "instances": 9, "metric_value": 0.1778, "depth": 12}
												if obj[10]>1.0:
													# {"feature": "Direction_same", "instances": 5, "metric_value": 0.32, "depth": 13}
													if obj[11]<=0:
														return 'False'
													else: return 'False'
												elif obj[10]<=1.0:
													return 'False'
												else: return 'False'
											elif obj[5]<=0:
												return 'True'
											else: return 'True'
										elif obj[8]>1.0:
											# {"feature": "Children", "instances": 3, "metric_value": 0.0, "depth": 11}
											if obj[5]>0:
												return 'True'
											elif obj[5]<=0:
												return 'False'
											else: return 'False'
										else: return 'True'
									elif obj[3]>0:
										# {"feature": "Children", "instances": 3, "metric_value": 0.0, "depth": 10}
										if obj[5]>0:
											return 'True'
										elif obj[5]<=0:
											return 'False'
										else: return 'False'
									else: return 'True'
								elif obj[1]>1:
									return 'False'
								else: return 'False'
							else: return 'False'
						else: return 'False'
					elif obj[6]<=0:
						# {"feature": "Restaurant20to50", "instances": 138, "metric_value": 0.4841, "depth": 6}
						if obj[10]<=3.0:
							# {"feature": "Time", "instances": 136, "metric_value": 0.4842, "depth": 7}
							if obj[1]>0:
								# {"feature": "Age", "instances": 113, "metric_value": 0.4751, "depth": 8}
								if obj[4]>0:
									# {"feature": "Occupation", "instances": 99, "metric_value": 0.4653, "depth": 9}
									if obj[7]<=22:
										# {"feature": "Gender", "instances": 98, "metric_value": 0.4612, "depth": 10}
										if obj[3]<=0:
											# {"feature": "Bar", "instances": 51, "metric_value": 0.4093, "depth": 11}
											if obj[8]>0.0:
												# {"feature": "Children", "instances": 30, "metric_value": 0.48, "depth": 12}
												if obj[5]<=0:
													# {"feature": "Direction_same", "instances": 20, "metric_value": 0.48, "depth": 13}
													if obj[11]<=0:
														return 'True'
													else: return 'True'
												elif obj[5]>0:
													# {"feature": "Direction_same", "instances": 10, "metric_value": 0.48, "depth": 13}
													if obj[11]<=0:
														return 'True'
													else: return 'True'
												else: return 'True'
											elif obj[8]<=0.0:
												# {"feature": "Children", "instances": 21, "metric_value": 0.2963, "depth": 12}
												if obj[5]<=0:
													# {"feature": "Direction_same", "instances": 18, "metric_value": 0.3457, "depth": 13}
													if obj[11]<=0:
														return 'True'
													else: return 'True'
												elif obj[5]>0:
													return 'True'
												else: return 'True'
											else: return 'True'
										elif obj[3]>0:
											# {"feature": "Bar", "instances": 47, "metric_value": 0.4823, "depth": 11}
											if obj[8]<=0.0:
												# {"feature": "Children", "instances": 32, "metric_value": 0.5, "depth": 12}
												if obj[5]>0:
													# {"feature": "Direction_same", "instances": 22, "metric_value": 0.5, "depth": 13}
													if obj[11]<=0:
														return 'True'
													else: return 'True'
												elif obj[5]<=0:
													# {"feature": "Direction_same", "instances": 10, "metric_value": 0.5, "depth": 13}
													if obj[11]<=0:
														return 'True'
													else: return 'True'
												else: return 'True'
											elif obj[8]>0.0:
												# {"feature": "Children", "instances": 15, "metric_value": 0.44, "depth": 12}
												if obj[5]<=0:
													# {"feature": "Direction_same", "instances": 10, "metric_value": 0.42, "depth": 13}
													if obj[11]<=0:
														return 'True'
													else: return 'True'
												elif obj[5]>0:
													# {"feature": "Direction_same", "instances": 5, "metric_value": 0.48, "depth": 13}
													if obj[11]<=0:
														return 'True'
													else: return 'True'
												else: return 'True'
											else: return 'True'
										else: return 'True'
									elif obj[7]>22:
										return 'False'
									else: return 'False'
								elif obj[4]<=0:
									# {"feature": "Children", "instances": 14, "metric_value": 0.3117, "depth": 9}
									if obj[5]<=0:
										# {"feature": "Bar", "instances": 11, "metric_value": 0.3636, "depth": 10}
										if obj[8]<=3.0:
											# {"feature": "Occupation", "instances": 9, "metric_value": 0.4167, "depth": 11}
											if obj[7]>1:
												# {"feature": "Gender", "instances": 8, "metric_value": 0.3571, "depth": 12}
												if obj[3]>0:
													# {"feature": "Direction_same", "instances": 7, "metric_value": 0.4082, "depth": 13}
													if obj[11]<=0:
														return 'False'
													else: return 'False'
												elif obj[3]<=0:
													return 'True'
												else: return 'True'
											elif obj[7]<=1:
												return 'False'
											else: return 'False'
										elif obj[8]>3.0:
											return 'False'
										else: return 'False'
									elif obj[5]>0:
										return 'True'
									else: return 'True'
								else: return 'False'
							elif obj[1]<=0:
								# {"feature": "Occupation", "instances": 23, "metric_value": 0.4306, "depth": 8}
								if obj[7]>1:
									# {"feature": "Bar", "instances": 21, "metric_value": 0.4121, "depth": 9}
									if obj[8]<=0.0:
										# {"feature": "Age", "instances": 11, "metric_value": 0.3409, "depth": 10}
										if obj[4]>1:
											# {"feature": "Gender", "instances": 8, "metric_value": 0.3, "depth": 11}
											if obj[3]<=0:
												# {"feature": "Children", "instances": 5, "metric_value": 0.48, "depth": 12}
												if obj[5]<=0:
													# {"feature": "Direction_same", "instances": 5, "metric_value": 0.48, "depth": 13}
													if obj[11]<=0:
														return 'True'
													else: return 'True'
												else: return 'True'
											elif obj[3]>0:
												return 'False'
											else: return 'False'
										elif obj[4]<=1:
											return 'True'
										else: return 'True'
									elif obj[8]>0.0:
										# {"feature": "Age", "instances": 10, "metric_value": 0.2667, "depth": 10}
										if obj[4]>3:
											# {"feature": "Gender", "instances": 6, "metric_value": 0.2667, "depth": 11}
											if obj[3]<=0:
												# {"feature": "Children", "instances": 5, "metric_value": 0.32, "depth": 12}
												if obj[5]<=0:
													# {"feature": "Direction_same", "instances": 5, "metric_value": 0.32, "depth": 13}
													if obj[11]<=0:
														return 'False'
													else: return 'False'
												else: return 'False'
											elif obj[3]>0:
												return 'True'
											else: return 'True'
										elif obj[4]<=3:
											return 'False'
										else: return 'False'
									else: return 'False'
								elif obj[7]<=1:
									return 'True'
								else: return 'True'
							else: return 'False'
						elif obj[10]>3.0:
							return 'False'
						else: return 'False'
					else: return 'True'
				elif obj[0]<=0:
					# {"feature": "Children", "instances": 16, "metric_value": 0.1786, "depth": 5}
					if obj[5]<=0:
						# {"feature": "Age", "instances": 14, "metric_value": 0.0952, "depth": 6}
						if obj[4]<=5:
							return 'True'
						elif obj[4]>5:
							# {"feature": "Gender", "instances": 3, "metric_value": 0.0, "depth": 7}
							if obj[3]<=0:
								return 'True'
							elif obj[3]>0:
								return 'False'
							else: return 'False'
						else: return 'True'
					elif obj[5]>0:
						# {"feature": "Gender", "instances": 2, "metric_value": 0.0, "depth": 6}
						if obj[3]<=0:
							return 'False'
						elif obj[3]>0:
							return 'True'
						else: return 'True'
					else: return 'False'
				else: return 'True'
			else: return 'False'
		elif obj[9]<=0.0:
			# {"feature": "Passanger", "instances": 1452, "metric_value": 0.4944, "depth": 3}
			if obj[0]<=1:
				# {"feature": "Distance", "instances": 925, "metric_value": 0.4846, "depth": 4}
				if obj[12]<=1:
					# {"feature": "Time", "instances": 498, "metric_value": 0.486, "depth": 5}
					if obj[1]>0:
						# {"feature": "Bar", "instances": 313, "metric_value": 0.473, "depth": 6}
						if obj[8]<=0.0:
							# {"feature": "Direction_same", "instances": 169, "metric_value": 0.4379, "depth": 7}
							if obj[11]>0:
								# {"feature": "Occupation", "instances": 94, "metric_value": 0.4613, "depth": 8}
								if obj[7]>3:
									# {"feature": "Age", "instances": 63, "metric_value": 0.4959, "depth": 9}
									if obj[4]>0:
										# {"feature": "Restaurant20to50", "instances": 55, "metric_value": 0.4902, "depth": 10}
										if obj[10]>-1.0:
											# {"feature": "Education", "instances": 54, "metric_value": 0.4967, "depth": 11}
											if obj[6]<=3:
												# {"feature": "Gender", "instances": 51, "metric_value": 0.4983, "depth": 12}
												if obj[3]<=0:
													# {"feature": "Children", "instances": 32, "metric_value": 0.498, "depth": 13}
													if obj[5]<=0:
														return 'False'
													elif obj[5]>0:
														return 'False'
													else: return 'False'
												elif obj[3]>0:
													# {"feature": "Children", "instances": 19, "metric_value": 0.4962, "depth": 13}
													if obj[5]<=0:
														return 'False'
													elif obj[5]>0:
														return 'True'
													else: return 'True'
												else: return 'True'
											elif obj[6]>3:
												# {"feature": "Gender", "instances": 3, "metric_value": 0.3333, "depth": 12}
												if obj[3]>0:
													# {"feature": "Children", "instances": 2, "metric_value": 0.0, "depth": 13}
													if obj[5]<=0:
														return 'True'
													elif obj[5]>0:
														return 'False'
													else: return 'False'
												elif obj[3]<=0:
													return 'False'
												else: return 'False'
											else: return 'False'
										elif obj[10]<=-1.0:
											return 'True'
										else: return 'True'
									elif obj[4]<=0:
										# {"feature": "Restaurant20to50", "instances": 8, "metric_value": 0.3571, "depth": 10}
										if obj[10]>-1.0:
											# {"feature": "Gender", "instances": 7, "metric_value": 0.381, "depth": 11}
											if obj[3]<=0:
												# {"feature": "Education", "instances": 6, "metric_value": 0.4, "depth": 12}
												if obj[6]>0:
													# {"feature": "Children", "instances": 5, "metric_value": 0.48, "depth": 13}
													if obj[5]<=1:
														return 'True'
													else: return 'True'
												elif obj[6]<=0:
													return 'True'
												else: return 'True'
											elif obj[3]>0:
												return 'True'
											else: return 'True'
										elif obj[10]<=-1.0:
											return 'False'
										else: return 'False'
									else: return 'True'
								elif obj[7]<=3:
									# {"feature": "Gender", "instances": 31, "metric_value": 0.3632, "depth": 9}
									if obj[3]>0:
										# {"feature": "Education", "instances": 27, "metric_value": 0.4044, "depth": 10}
										if obj[6]<=1:
											# {"feature": "Age", "instances": 17, "metric_value": 0.3557, "depth": 11}
											if obj[4]>0:
												# {"feature": "Restaurant20to50", "instances": 14, "metric_value": 0.3214, "depth": 12}
												if obj[10]<=1.0:
													# {"feature": "Children", "instances": 12, "metric_value": 0.375, "depth": 13}
													if obj[5]>0:
														return 'True'
													elif obj[5]<=0:
														return 'True'
													else: return 'True'
												elif obj[10]>1.0:
													return 'True'
												else: return 'True'
											elif obj[4]<=0:
												# {"feature": "Children", "instances": 3, "metric_value": 0.4444, "depth": 12}
												if obj[5]<=0:
													# {"feature": "Restaurant20to50", "instances": 3, "metric_value": 0.4444, "depth": 13}
													if obj[10]<=2.0:
														return 'True'
													else: return 'True'
												else: return 'True'
											else: return 'True'
										elif obj[6]>1:
											# {"feature": "Age", "instances": 10, "metric_value": 0.4, "depth": 11}
											if obj[4]>1:
												# {"feature": "Children", "instances": 8, "metric_value": 0.5, "depth": 12}
												if obj[5]<=0:
													# {"feature": "Restaurant20to50", "instances": 8, "metric_value": 0.5, "depth": 13}
													if obj[10]<=0.0:
														return 'False'
													else: return 'False'
												else: return 'False'
											elif obj[4]<=1:
												return 'True'
											else: return 'True'
										else: return 'True'
									elif obj[3]<=0:
										return 'True'
									else: return 'True'
								else: return 'True'
							elif obj[11]<=0:
								# {"feature": "Education", "instances": 75, "metric_value": 0.3407, "depth": 8}
								if obj[6]>0:
									# {"feature": "Age", "instances": 40, "metric_value": 0.2034, "depth": 9}
									if obj[4]<=4:
										# {"feature": "Restaurant20to50", "instances": 34, "metric_value": 0.1576, "depth": 10}
										if obj[10]<=1.0:
											# {"feature": "Gender", "instances": 28, "metric_value": 0.186, "depth": 11}
											if obj[3]>0:
												# {"feature": "Children", "instances": 16, "metric_value": 0.1071, "depth": 12}
												if obj[5]>0:
													return 'True'
												elif obj[5]<=0:
													# {"feature": "Occupation", "instances": 7, "metric_value": 0.2143, "depth": 13}
													if obj[7]<=2:
														return 'True'
													elif obj[7]>2:
														return 'True'
													else: return 'True'
												else: return 'True'
											elif obj[3]<=0:
												# {"feature": "Children", "instances": 12, "metric_value": 0.2333, "depth": 12}
												if obj[5]<=0:
													# {"feature": "Occupation", "instances": 10, "metric_value": 0.1333, "depth": 13}
													if obj[7]<=6:
														return 'True'
													elif obj[7]>6:
														return 'True'
													else: return 'True'
												elif obj[5]>0:
													# {"feature": "Occupation", "instances": 2, "metric_value": 0.0, "depth": 13}
													if obj[7]<=6:
														return 'False'
													elif obj[7]>6:
														return 'True'
													else: return 'True'
												else: return 'False'
											else: return 'True'
										elif obj[10]>1.0:
											return 'True'
										else: return 'True'
									elif obj[4]>4:
										# {"feature": "Restaurant20to50", "instances": 6, "metric_value": 0.0, "depth": 10}
										if obj[10]>1.0:
											return 'True'
										elif obj[10]<=1.0:
											return 'False'
										else: return 'False'
									else: return 'True'
								elif obj[6]<=0:
									# {"feature": "Occupation", "instances": 35, "metric_value": 0.4573, "depth": 9}
									if obj[7]>4:
										# {"feature": "Age", "instances": 22, "metric_value": 0.3743, "depth": 10}
										if obj[4]>1:
											# {"feature": "Gender", "instances": 17, "metric_value": 0.4471, "depth": 11}
											if obj[3]<=0:
												# {"feature": "Children", "instances": 12, "metric_value": 0.4815, "depth": 12}
												if obj[5]<=0:
													# {"feature": "Restaurant20to50", "instances": 9, "metric_value": 0.4921, "depth": 13}
													if obj[10]>0.0:
														return 'True'
													elif obj[10]<=0.0:
														return 'False'
													else: return 'False'
												elif obj[5]>0:
													# {"feature": "Restaurant20to50", "instances": 3, "metric_value": 0.4444, "depth": 13}
													if obj[10]<=1.0:
														return 'False'
													else: return 'False'
												else: return 'False'
											elif obj[3]>0:
												# {"feature": "Children", "instances": 5, "metric_value": 0.2667, "depth": 12}
												if obj[5]<=0:
													# {"feature": "Restaurant20to50", "instances": 3, "metric_value": 0.0, "depth": 13}
													if obj[10]<=0.0:
														return 'True'
													elif obj[10]>0.0:
														return 'False'
													else: return 'False'
												elif obj[5]>0:
													return 'True'
												else: return 'True'
											else: return 'True'
										elif obj[4]<=1:
											return 'True'
										else: return 'True'
									elif obj[7]<=4:
										# {"feature": "Age", "instances": 13, "metric_value": 0.4196, "depth": 10}
										if obj[4]>0:
											# {"feature": "Restaurant20to50", "instances": 11, "metric_value": 0.4364, "depth": 11}
											if obj[10]>0.0:
												# {"feature": "Gender", "instances": 10, "metric_value": 0.4667, "depth": 12}
												if obj[3]>0:
													# {"feature": "Children", "instances": 6, "metric_value": 0.4444, "depth": 13}
													if obj[5]<=1:
														return 'True'
													else: return 'True'
												elif obj[3]<=0:
													# {"feature": "Children", "instances": 4, "metric_value": 0.5, "depth": 13}
													if obj[5]<=0:
														return 'False'
													else: return 'False'
												else: return 'False'
											elif obj[10]<=0.0:
												return 'False'
											else: return 'False'
										elif obj[4]<=0:
											return 'False'
										else: return 'False'
									else: return 'False'
								else: return 'True'
							else: return 'True'
						elif obj[8]>0.0:
							# {"feature": "Occupation", "instances": 144, "metric_value": 0.4721, "depth": 7}
							if obj[7]<=20:
								# {"feature": "Age", "instances": 136, "metric_value": 0.4906, "depth": 8}
								if obj[4]>1:
									# {"feature": "Education", "instances": 78, "metric_value": 0.4521, "depth": 9}
									if obj[6]>1:
										# {"feature": "Children", "instances": 58, "metric_value": 0.4733, "depth": 10}
										if obj[5]<=0:
											# {"feature": "Restaurant20to50", "instances": 41, "metric_value": 0.4758, "depth": 11}
											if obj[10]>0.0:
												# {"feature": "Gender", "instances": 26, "metric_value": 0.4567, "depth": 12}
												if obj[3]>0:
													# {"feature": "Direction_same", "instances": 16, "metric_value": 0.4286, "depth": 13}
													if obj[11]<=0:
														return 'True'
													elif obj[11]>0:
														return 'True'
													else: return 'True'
												elif obj[3]<=0:
													# {"feature": "Direction_same", "instances": 10, "metric_value": 0.5, "depth": 13}
													if obj[11]<=0:
														return 'True'
													elif obj[11]>0:
														return 'False'
													else: return 'False'
												else: return 'False'
											elif obj[10]<=0.0:
												# {"feature": "Direction_same", "instances": 15, "metric_value": 0.4778, "depth": 12}
												if obj[11]>0:
													# {"feature": "Gender", "instances": 12, "metric_value": 0.4857, "depth": 13}
													if obj[3]>0:
														return 'False'
													elif obj[3]<=0:
														return 'False'
													else: return 'False'
												elif obj[11]<=0:
													# {"feature": "Gender", "instances": 3, "metric_value": 0.3333, "depth": 13}
													if obj[3]<=0:
														return 'False'
													elif obj[3]>0:
														return 'False'
													else: return 'False'
												else: return 'False'
											else: return 'False'
										elif obj[5]>0:
											# {"feature": "Direction_same", "instances": 17, "metric_value": 0.3644, "depth": 11}
											if obj[11]<=0:
												# {"feature": "Gender", "instances": 9, "metric_value": 0.4444, "depth": 12}
												if obj[3]<=0:
													# {"feature": "Restaurant20to50", "instances": 6, "metric_value": 0.3333, "depth": 13}
													if obj[10]>1.0:
														return 'False'
													elif obj[10]<=1.0:
														return 'False'
													else: return 'False'
												elif obj[3]>0:
													# {"feature": "Restaurant20to50", "instances": 3, "metric_value": 0.3333, "depth": 13}
													if obj[10]>1.0:
														return 'True'
													elif obj[10]<=1.0:
														return 'True'
													else: return 'True'
												else: return 'True'
											elif obj[11]>0:
												# {"feature": "Restaurant20to50", "instances": 8, "metric_value": 0.2, "depth": 12}
												if obj[10]<=1.0:
													# {"feature": "Gender", "instances": 5, "metric_value": 0.3, "depth": 13}
													if obj[3]>0:
														return 'False'
													elif obj[3]<=0:
														return 'False'
													else: return 'False'
												elif obj[10]>1.0:
													return 'False'
												else: return 'False'
											else: return 'False'
										else: return 'False'
									elif obj[6]<=1:
										# {"feature": "Children", "instances": 20, "metric_value": 0.3048, "depth": 10}
										if obj[5]<=0:
											# {"feature": "Restaurant20to50", "instances": 14, "metric_value": 0.2143, "depth": 11}
											if obj[10]<=1.0:
												# {"feature": "Direction_same", "instances": 8, "metric_value": 0.3333, "depth": 12}
												if obj[11]<=0:
													# {"feature": "Gender", "instances": 6, "metric_value": 0.2778, "depth": 13}
													if obj[3]<=0:
														return 'True'
													else: return 'True'
												elif obj[11]>0:
													# {"feature": "Gender", "instances": 2, "metric_value": 0.5, "depth": 13}
													if obj[3]<=0:
														return 'True'
													else: return 'True'
												else: return 'True'
											elif obj[10]>1.0:
												return 'True'
											else: return 'True'
										elif obj[5]>0:
											# {"feature": "Gender", "instances": 6, "metric_value": 0.4167, "depth": 11}
											if obj[3]>0:
												# {"feature": "Direction_same", "instances": 4, "metric_value": 0.0, "depth": 12}
												if obj[11]>0:
													return 'True'
												elif obj[11]<=0:
													return 'False'
												else: return 'False'
											elif obj[3]<=0:
												# {"feature": "Direction_same", "instances": 2, "metric_value": 0.0, "depth": 12}
												if obj[11]>0:
													return 'False'
												elif obj[11]<=0:
													return 'True'
												else: return 'True'
											else: return 'False'
										else: return 'True'
									else: return 'True'
								elif obj[4]<=1:
									# {"feature": "Direction_same", "instances": 58, "metric_value": 0.4713, "depth": 9}
									if obj[11]>0:
										# {"feature": "Restaurant20to50", "instances": 30, "metric_value": 0.4138, "depth": 10}
										if obj[10]>-1.0:
											# {"feature": "Children", "instances": 29, "metric_value": 0.423, "depth": 11}
											if obj[5]<=0:
												# {"feature": "Gender", "instances": 24, "metric_value": 0.4296, "depth": 12}
												if obj[3]<=0:
													# {"feature": "Education", "instances": 15, "metric_value": 0.4571, "depth": 13}
													if obj[6]>0:
														return 'False'
													elif obj[6]<=0:
														return 'False'
													else: return 'False'
												elif obj[3]>0:
													# {"feature": "Education", "instances": 9, "metric_value": 0.3175, "depth": 13}
													if obj[6]>0:
														return 'False'
													elif obj[6]<=0:
														return 'False'
													else: return 'False'
												else: return 'False'
											elif obj[5]>0:
												# {"feature": "Gender", "instances": 5, "metric_value": 0.2, "depth": 12}
												if obj[3]<=0:
													return 'False'
												elif obj[3]>0:
													# {"feature": "Education", "instances": 2, "metric_value": 0.5, "depth": 13}
													if obj[6]<=0:
														return 'False'
													else: return 'False'
												else: return 'False'
											else: return 'False'
										elif obj[10]<=-1.0:
											return 'True'
										else: return 'True'
									elif obj[11]<=0:
										# {"feature": "Gender", "instances": 28, "metric_value": 0.4269, "depth": 10}
										if obj[3]<=0:
											# {"feature": "Restaurant20to50", "instances": 19, "metric_value": 0.4145, "depth": 11}
											if obj[10]>0.0:
												# {"feature": "Education", "instances": 16, "metric_value": 0.4909, "depth": 12}
												if obj[6]>0:
													# {"feature": "Children", "instances": 11, "metric_value": 0.4949, "depth": 13}
													if obj[5]<=0:
														return 'False'
													elif obj[5]>0:
														return 'True'
													else: return 'True'
												elif obj[6]<=0:
													# {"feature": "Children", "instances": 5, "metric_value": 0.48, "depth": 13}
													if obj[5]<=0:
														return 'False'
													else: return 'False'
												else: return 'False'
											elif obj[10]<=0.0:
												return 'False'
											else: return 'False'
										elif obj[3]>0:
											# {"feature": "Education", "instances": 9, "metric_value": 0.3016, "depth": 11}
											if obj[6]<=2:
												# {"feature": "Restaurant20to50", "instances": 7, "metric_value": 0.1429, "depth": 12}
												if obj[10]>-1.0:
													return 'True'
												elif obj[10]<=-1.0:
													# {"feature": "Children", "instances": 2, "metric_value": 0.5, "depth": 13}
													if obj[5]<=1:
														return 'True'
													else: return 'True'
												else: return 'True'
											elif obj[6]>2:
												# {"feature": "Children", "instances": 2, "metric_value": 0.5, "depth": 12}
												if obj[5]<=0:
													# {"feature": "Restaurant20to50", "instances": 2, "metric_value": 0.5, "depth": 13}
													if obj[10]<=1.0:
														return 'False'
													else: return 'False'
												else: return 'False'
											else: return 'False'
										else: return 'True'
									else: return 'False'
								else: return 'False'
							elif obj[7]>20:
								return 'True'
							else: return 'True'
						else: return 'True'
					elif obj[1]<=0:
						# {"feature": "Occupation", "instances": 185, "metric_value": 0.4726, "depth": 6}
						if obj[7]<=7.951351351351351:
							# {"feature": "Education", "instances": 114, "metric_value": 0.4532, "depth": 7}
							if obj[6]<=3:
								# {"feature": "Bar", "instances": 103, "metric_value": 0.4401, "depth": 8}
								if obj[8]>-1.0:
									# {"feature": "Age", "instances": 102, "metric_value": 0.44, "depth": 9}
									if obj[4]>1:
										# {"feature": "Restaurant20to50", "instances": 64, "metric_value": 0.4018, "depth": 10}
										if obj[10]>-1.0:
											# {"feature": "Direction_same", "instances": 63, "metric_value": 0.4061, "depth": 11}
											if obj[11]<=0:
												# {"feature": "Gender", "instances": 35, "metric_value": 0.4303, "depth": 12}
												if obj[3]<=0:
													# {"feature": "Children", "instances": 18, "metric_value": 0.4375, "depth": 13}
													if obj[5]<=0:
														return 'False'
													elif obj[5]>0:
														return 'True'
													else: return 'True'
												elif obj[3]>0:
													# {"feature": "Children", "instances": 17, "metric_value": 0.4118, "depth": 13}
													if obj[5]<=0:
														return 'False'
													elif obj[5]>0:
														return 'False'
													else: return 'False'
												else: return 'False'
											elif obj[11]>0:
												# {"feature": "Children", "instances": 28, "metric_value": 0.3684, "depth": 12}
												if obj[5]<=0:
													# {"feature": "Gender", "instances": 19, "metric_value": 0.3323, "depth": 13}
													if obj[3]>0:
														return 'False'
													elif obj[3]<=0:
														return 'False'
													else: return 'False'
												elif obj[5]>0:
													# {"feature": "Gender", "instances": 9, "metric_value": 0.4444, "depth": 13}
													if obj[3]>0:
														return 'False'
													elif obj[3]<=0:
														return 'False'
													else: return 'False'
												else: return 'False'
											else: return 'False'
										elif obj[10]<=-1.0:
											return 'True'
										else: return 'True'
									elif obj[4]<=1:
										# {"feature": "Restaurant20to50", "instances": 38, "metric_value": 0.4694, "depth": 10}
										if obj[10]>-1.0:
											# {"feature": "Children", "instances": 37, "metric_value": 0.4787, "depth": 11}
											if obj[5]<=0:
												# {"feature": "Direction_same", "instances": 24, "metric_value": 0.4607, "depth": 12}
												if obj[11]<=0:
													# {"feature": "Gender", "instances": 14, "metric_value": 0.4848, "depth": 13}
													if obj[3]<=0:
														return 'False'
													elif obj[3]>0:
														return 'False'
													else: return 'False'
												elif obj[11]>0:
													# {"feature": "Gender", "instances": 10, "metric_value": 0.419, "depth": 13}
													if obj[3]<=0:
														return 'False'
													elif obj[3]>0:
														return 'False'
													else: return 'False'
												else: return 'False'
											elif obj[5]>0:
												# {"feature": "Direction_same", "instances": 13, "metric_value": 0.4718, "depth": 12}
												if obj[11]<=0:
													# {"feature": "Gender", "instances": 10, "metric_value": 0.45, "depth": 13}
													if obj[3]<=0:
														return 'True'
													elif obj[3]>0:
														return 'False'
													else: return 'False'
												elif obj[11]>0:
													# {"feature": "Gender", "instances": 3, "metric_value": 0.3333, "depth": 13}
													if obj[3]<=0:
														return 'False'
													elif obj[3]>0:
														return 'True'
													else: return 'True'
												else: return 'True'
											else: return 'False'
										elif obj[10]<=-1.0:
											return 'False'
										else: return 'False'
									else: return 'False'
								elif obj[8]<=-1.0:
									return 'True'
								else: return 'True'
							elif obj[6]>3:
								# {"feature": "Age", "instances": 11, "metric_value": 0.3409, "depth": 8}
								if obj[4]<=4:
									# {"feature": "Bar", "instances": 8, "metric_value": 0.3, "depth": 9}
									if obj[8]>0.0:
										# {"feature": "Restaurant20to50", "instances": 5, "metric_value": 0.4, "depth": 10}
										if obj[10]<=1.0:
											# {"feature": "Gender", "instances": 4, "metric_value": 0.5, "depth": 11}
											if obj[3]>0:
												# {"feature": "Children", "instances": 2, "metric_value": 0.5, "depth": 12}
												if obj[5]<=0:
													# {"feature": "Direction_same", "instances": 2, "metric_value": 0.5, "depth": 13}
													if obj[11]<=0:
														return 'True'
													else: return 'True'
												else: return 'True'
											elif obj[3]<=0:
												# {"feature": "Children", "instances": 2, "metric_value": 0.5, "depth": 12}
												if obj[5]<=0:
													# {"feature": "Direction_same", "instances": 2, "metric_value": 0.5, "depth": 13}
													if obj[11]<=0:
														return 'True'
													else: return 'True'
												else: return 'True'
											else: return 'True'
										elif obj[10]>1.0:
											return 'True'
										else: return 'True'
									elif obj[8]<=0.0:
										return 'False'
									else: return 'False'
								elif obj[4]>4:
									return 'True'
								else: return 'True'
							else: return 'True'
						elif obj[7]>7.951351351351351:
							# {"feature": "Direction_same", "instances": 71, "metric_value": 0.4524, "depth": 7}
							if obj[11]<=0:
								# {"feature": "Age", "instances": 39, "metric_value": 0.4438, "depth": 8}
								if obj[4]<=2:
									# {"feature": "Education", "instances": 25, "metric_value": 0.4047, "depth": 9}
									if obj[6]>0:
										# {"feature": "Restaurant20to50", "instances": 17, "metric_value": 0.3412, "depth": 10}
										if obj[10]>-1.0:
											# {"feature": "Bar", "instances": 15, "metric_value": 0.3077, "depth": 11}
											if obj[8]<=1.0:
												# {"feature": "Gender", "instances": 13, "metric_value": 0.337, "depth": 12}
												if obj[3]>0:
													# {"feature": "Children", "instances": 7, "metric_value": 0.2143, "depth": 13}
													if obj[5]>0:
														return 'False'
													elif obj[5]<=0:
														return 'False'
													else: return 'False'
												elif obj[3]<=0:
													# {"feature": "Children", "instances": 6, "metric_value": 0.4167, "depth": 13}
													if obj[5]>0:
														return 'False'
													elif obj[5]<=0:
														return 'True'
													else: return 'True'
												else: return 'False'
											elif obj[8]>1.0:
												return 'False'
											else: return 'False'
										elif obj[10]<=-1.0:
											# {"feature": "Gender", "instances": 2, "metric_value": 0.0, "depth": 11}
											if obj[3]<=0:
												return 'False'
											elif obj[3]>0:
												return 'True'
											else: return 'True'
										else: return 'False'
									elif obj[6]<=0:
										# {"feature": "Gender", "instances": 8, "metric_value": 0.4667, "depth": 10}
										if obj[3]<=0:
											# {"feature": "Children", "instances": 5, "metric_value": 0.4667, "depth": 11}
											if obj[5]>0:
												# {"feature": "Bar", "instances": 3, "metric_value": 0.3333, "depth": 12}
												if obj[8]<=0.0:
													# {"feature": "Restaurant20to50", "instances": 2, "metric_value": 0.5, "depth": 13}
													if obj[10]<=1.0:
														return 'False'
													else: return 'False'
												elif obj[8]>0.0:
													return 'True'
												else: return 'True'
											elif obj[5]<=0:
												# {"feature": "Bar", "instances": 2, "metric_value": 0.5, "depth": 12}
												if obj[8]<=3.0:
													# {"feature": "Restaurant20to50", "instances": 2, "metric_value": 0.5, "depth": 13}
													if obj[10]<=0.0:
														return 'False'
													else: return 'False'
												else: return 'False'
											else: return 'False'
										elif obj[3]>0:
											# {"feature": "Children", "instances": 3, "metric_value": 0.0, "depth": 11}
											if obj[5]>0:
												return 'False'
											elif obj[5]<=0:
												return 'True'
											else: return 'True'
										else: return 'False'
									else: return 'False'
								elif obj[4]>2:
									# {"feature": "Children", "instances": 14, "metric_value": 0.3357, "depth": 9}
									if obj[5]<=0:
										# {"feature": "Gender", "instances": 10, "metric_value": 0.2857, "depth": 10}
										if obj[3]<=0:
											# {"feature": "Restaurant20to50", "instances": 7, "metric_value": 0.2381, "depth": 11}
											if obj[10]>0.0:
												# {"feature": "Bar", "instances": 6, "metric_value": 0.2222, "depth": 12}
												if obj[8]<=0.0:
													# {"feature": "Education", "instances": 3, "metric_value": 0.4444, "depth": 13}
													if obj[6]<=2:
														return 'True'
													else: return 'True'
												elif obj[8]>0.0:
													return 'True'
												else: return 'True'
											elif obj[10]<=0.0:
												return 'False'
											else: return 'False'
										elif obj[3]>0:
											return 'True'
										else: return 'True'
									elif obj[5]>0:
										# {"feature": "Gender", "instances": 4, "metric_value": 0.3333, "depth": 10}
										if obj[3]<=0:
											# {"feature": "Education", "instances": 3, "metric_value": 0.3333, "depth": 11}
											if obj[6]>2:
												# {"feature": "Bar", "instances": 2, "metric_value": 0.5, "depth": 12}
												if obj[8]<=0.0:
													# {"feature": "Restaurant20to50", "instances": 2, "metric_value": 0.5, "depth": 13}
													if obj[10]<=2.0:
														return 'False'
													else: return 'False'
												else: return 'False'
											elif obj[6]<=2:
												return 'False'
											else: return 'False'
										elif obj[3]>0:
											return 'False'
										else: return 'False'
									else: return 'False'
								else: return 'True'
							elif obj[11]>0:
								# {"feature": "Bar", "instances": 32, "metric_value": 0.3822, "depth": 8}
								if obj[8]<=1.0:
									# {"feature": "Children", "instances": 26, "metric_value": 0.3067, "depth": 9}
									if obj[5]<=0:
										# {"feature": "Restaurant20to50", "instances": 17, "metric_value": 0.1765, "depth": 10}
										if obj[10]>0.0:
											return 'True'
										elif obj[10]<=0.0:
											# {"feature": "Age", "instances": 8, "metric_value": 0.3, "depth": 11}
											if obj[4]>1:
												# {"feature": "Education", "instances": 5, "metric_value": 0.4, "depth": 12}
												if obj[6]>0:
													# {"feature": "Gender", "instances": 4, "metric_value": 0.5, "depth": 13}
													if obj[3]<=1:
														return 'False'
													else: return 'False'
												elif obj[6]<=0:
													return 'True'
												else: return 'True'
											elif obj[4]<=1:
												return 'True'
											else: return 'True'
										else: return 'True'
									elif obj[5]>0:
										# {"feature": "Gender", "instances": 9, "metric_value": 0.3175, "depth": 10}
										if obj[3]<=0:
											# {"feature": "Age", "instances": 7, "metric_value": 0.3429, "depth": 11}
											if obj[4]<=6:
												# {"feature": "Restaurant20to50", "instances": 5, "metric_value": 0.4, "depth": 12}
												if obj[10]>-1.0:
													# {"feature": "Education", "instances": 4, "metric_value": 0.5, "depth": 13}
													if obj[6]>1:
														return 'True'
													elif obj[6]<=1:
														return 'True'
													else: return 'True'
												elif obj[10]<=-1.0:
													return 'True'
												else: return 'True'
											elif obj[4]>6:
												return 'True'
											else: return 'True'
										elif obj[3]>0:
											return 'False'
										else: return 'False'
									else: return 'True'
								elif obj[8]>1.0:
									# {"feature": "Children", "instances": 6, "metric_value": 0.25, "depth": 9}
									if obj[5]<=0:
										# {"feature": "Gender", "instances": 4, "metric_value": 0.25, "depth": 10}
										if obj[3]>0:
											# {"feature": "Age", "instances": 2, "metric_value": 0.5, "depth": 11}
											if obj[4]<=7:
												# {"feature": "Education", "instances": 2, "metric_value": 0.5, "depth": 12}
												if obj[6]<=0:
													# {"feature": "Restaurant20to50", "instances": 2, "metric_value": 0.5, "depth": 13}
													if obj[10]<=2.0:
														return 'True'
													else: return 'True'
												else: return 'True'
											else: return 'True'
										elif obj[3]<=0:
											return 'False'
										else: return 'False'
									elif obj[5]>0:
										return 'True'
									else: return 'True'
								else: return 'True'
							else: return 'True'
						else: return 'True'
					else: return 'False'
				elif obj[12]>1:
					# {"feature": "Bar", "instances": 427, "metric_value": 0.466, "depth": 5}
					if obj[8]<=1.0:
						# {"feature": "Age", "instances": 341, "metric_value": 0.4752, "depth": 6}
						if obj[4]<=5:
							# {"feature": "Occupation", "instances": 267, "metric_value": 0.4828, "depth": 7}
							if obj[7]<=7.898876404494382:
								# {"feature": "Education", "instances": 166, "metric_value": 0.4879, "depth": 8}
								if obj[6]<=3:
									# {"feature": "Restaurant20to50", "instances": 146, "metric_value": 0.4806, "depth": 9}
									if obj[10]>0.0:
										# {"feature": "Children", "instances": 95, "metric_value": 0.4841, "depth": 10}
										if obj[5]<=0:
											# {"feature": "Direction_same", "instances": 72, "metric_value": 0.463, "depth": 11}
											if obj[11]<=0:
												# {"feature": "Time", "instances": 60, "metric_value": 0.4917, "depth": 12}
												if obj[1]>0:
													# {"feature": "Gender", "instances": 49, "metric_value": 0.4975, "depth": 13}
													if obj[3]<=0:
														return 'True'
													elif obj[3]>0:
														return 'False'
													else: return 'False'
												elif obj[1]<=0:
													# {"feature": "Gender", "instances": 11, "metric_value": 0.4481, "depth": 13}
													if obj[3]<=0:
														return 'False'
													elif obj[3]>0:
														return 'False'
													else: return 'False'
												else: return 'False'
											elif obj[11]>0:
												# {"feature": "Time", "instances": 12, "metric_value": 0.2333, "depth": 12}
												if obj[1]>0:
													# {"feature": "Gender", "instances": 10, "metric_value": 0.1667, "depth": 13}
													if obj[3]>0:
														return 'False'
													elif obj[3]<=0:
														return 'False'
													else: return 'False'
												elif obj[1]<=0:
													# {"feature": "Gender", "instances": 2, "metric_value": 0.0, "depth": 13}
													if obj[3]<=0:
														return 'True'
													elif obj[3]>0:
														return 'False'
													else: return 'False'
												else: return 'True'
											else: return 'False'
										elif obj[5]>0:
											# {"feature": "Direction_same", "instances": 23, "metric_value": 0.3683, "depth": 11}
											if obj[11]<=0:
												# {"feature": "Time", "instances": 17, "metric_value": 0.4706, "depth": 12}
												if obj[1]>0:
													# {"feature": "Gender", "instances": 16, "metric_value": 0.4667, "depth": 13}
													if obj[3]>0:
														return 'False'
													elif obj[3]<=0:
														return 'True'
													else: return 'True'
												elif obj[1]<=0:
													return 'True'
												else: return 'True'
											elif obj[11]>0:
												return 'True'
											else: return 'True'
										else: return 'True'
									elif obj[10]<=0.0:
										# {"feature": "Gender", "instances": 51, "metric_value": 0.4321, "depth": 10}
										if obj[3]<=0:
											# {"feature": "Time", "instances": 27, "metric_value": 0.4392, "depth": 11}
											if obj[1]<=1:
												# {"feature": "Direction_same", "instances": 17, "metric_value": 0.4059, "depth": 12}
												if obj[11]<=0:
													# {"feature": "Children", "instances": 12, "metric_value": 0.3714, "depth": 13}
													if obj[5]<=0:
														return 'False'
													elif obj[5]>0:
														return 'False'
													else: return 'False'
												elif obj[11]>0:
													# {"feature": "Children", "instances": 5, "metric_value": 0.3, "depth": 13}
													if obj[5]<=0:
														return 'False'
													elif obj[5]>0:
														return 'True'
													else: return 'True'
												else: return 'False'
											elif obj[1]>1:
												# {"feature": "Direction_same", "instances": 10, "metric_value": 0.4, "depth": 12}
												if obj[11]<=0:
													# {"feature": "Children", "instances": 8, "metric_value": 0.5, "depth": 13}
													if obj[5]<=0:
														return 'False'
													elif obj[5]>0:
														return 'False'
													else: return 'False'
												elif obj[11]>0:
													return 'True'
												else: return 'True'
											else: return 'True'
										elif obj[3]>0:
											# {"feature": "Time", "instances": 24, "metric_value": 0.3571, "depth": 11}
											if obj[1]>0:
												# {"feature": "Direction_same", "instances": 21, "metric_value": 0.381, "depth": 12}
												if obj[11]<=0:
													# {"feature": "Children", "instances": 18, "metric_value": 0.4329, "depth": 13}
													if obj[5]>0:
														return 'False'
													elif obj[5]<=0:
														return 'False'
													else: return 'False'
												elif obj[11]>0:
													return 'False'
												else: return 'False'
											elif obj[1]<=0:
												return 'False'
											else: return 'False'
										else: return 'False'
									else: return 'False'
								elif obj[6]>3:
									# {"feature": "Time", "instances": 20, "metric_value": 0.3059, "depth": 9}
									if obj[1]>0:
										# {"feature": "Direction_same", "instances": 17, "metric_value": 0.3412, "depth": 10}
										if obj[11]<=0:
											# {"feature": "Gender", "instances": 15, "metric_value": 0.2963, "depth": 11}
											if obj[3]<=0:
												# {"feature": "Restaurant20to50", "instances": 9, "metric_value": 0.1852, "depth": 12}
												if obj[10]<=0.0:
													# {"feature": "Children", "instances": 6, "metric_value": 0.2778, "depth": 13}
													if obj[5]<=0:
														return 'True'
													else: return 'True'
												elif obj[10]>0.0:
													return 'True'
												else: return 'True'
											elif obj[3]>0:
												# {"feature": "Children", "instances": 6, "metric_value": 0.4444, "depth": 12}
												if obj[5]<=0:
													# {"feature": "Restaurant20to50", "instances": 6, "metric_value": 0.4444, "depth": 13}
													if obj[10]<=0.0:
														return 'True'
													else: return 'True'
												else: return 'True'
											else: return 'True'
										elif obj[11]>0:
											# {"feature": "Gender", "instances": 2, "metric_value": 0.0, "depth": 11}
											if obj[3]>0:
												return 'True'
											elif obj[3]<=0:
												return 'False'
											else: return 'False'
										else: return 'True'
									elif obj[1]<=0:
										return 'False'
									else: return 'False'
								else: return 'True'
							elif obj[7]>7.898876404494382:
								# {"feature": "Direction_same", "instances": 101, "metric_value": 0.443, "depth": 8}
								if obj[11]<=0:
									# {"feature": "Children", "instances": 73, "metric_value": 0.4052, "depth": 9}
									if obj[5]<=0:
										# {"feature": "Time", "instances": 39, "metric_value": 0.4409, "depth": 10}
										if obj[1]<=2:
											# {"feature": "Gender", "instances": 25, "metric_value": 0.3806, "depth": 11}
											if obj[3]>0:
												# {"feature": "Education", "instances": 17, "metric_value": 0.4235, "depth": 12}
												if obj[6]>0:
													# {"feature": "Restaurant20to50", "instances": 15, "metric_value": 0.4571, "depth": 13}
													if obj[10]<=0.0:
														return 'False'
													elif obj[10]>0.0:
														return 'True'
													else: return 'True'
												elif obj[6]<=0:
													return 'True'
												else: return 'True'
											elif obj[3]<=0:
												# {"feature": "Restaurant20to50", "instances": 8, "metric_value": 0.1667, "depth": 12}
												if obj[10]<=1.0:
													return 'False'
												elif obj[10]>1.0:
													# {"feature": "Education", "instances": 3, "metric_value": 0.3333, "depth": 13}
													if obj[6]>0:
														return 'True'
													elif obj[6]<=0:
														return 'False'
													else: return 'False'
												else: return 'False'
											else: return 'False'
										elif obj[1]>2:
											# {"feature": "Education", "instances": 14, "metric_value": 0.3, "depth": 11}
											if obj[6]>0:
												# {"feature": "Gender", "instances": 10, "metric_value": 0.3048, "depth": 12}
												if obj[3]>0:
													# {"feature": "Restaurant20to50", "instances": 7, "metric_value": 0.2143, "depth": 13}
													if obj[10]<=0.0:
														return 'False'
													elif obj[10]>0.0:
														return 'False'
													else: return 'False'
												elif obj[3]<=0:
													# {"feature": "Restaurant20to50", "instances": 3, "metric_value": 0.3333, "depth": 13}
													if obj[10]<=1.0:
														return 'False'
													elif obj[10]>1.0:
														return 'True'
													else: return 'True'
												else: return 'True'
											elif obj[6]<=0:
												return 'False'
											else: return 'False'
										else: return 'False'
									elif obj[5]>0:
										# {"feature": "Time", "instances": 34, "metric_value": 0.3013, "depth": 10}
										if obj[1]<=3:
											# {"feature": "Restaurant20to50", "instances": 27, "metric_value": 0.2326, "depth": 11}
											if obj[10]<=2.0:
												# {"feature": "Education", "instances": 25, "metric_value": 0.2, "depth": 12}
												if obj[6]<=2:
													# {"feature": "Gender", "instances": 18, "metric_value": 0.2771, "depth": 13}
													if obj[3]<=0:
														return 'False'
													elif obj[3]>0:
														return 'False'
													else: return 'False'
												elif obj[6]>2:
													return 'False'
												else: return 'False'
											elif obj[10]>2.0:
												# {"feature": "Gender", "instances": 2, "metric_value": 0.5, "depth": 12}
												if obj[3]<=0:
													# {"feature": "Education", "instances": 2, "metric_value": 0.5, "depth": 13}
													if obj[6]<=3:
														return 'False'
													else: return 'False'
												else: return 'False'
											else: return 'False'
										elif obj[1]>3:
											# {"feature": "Restaurant20to50", "instances": 7, "metric_value": 0.2143, "depth": 11}
											if obj[10]<=0.0:
												# {"feature": "Gender", "instances": 4, "metric_value": 0.25, "depth": 12}
												if obj[3]<=0:
													# {"feature": "Education", "instances": 2, "metric_value": 0.5, "depth": 13}
													if obj[6]<=1:
														return 'False'
													else: return 'False'
												elif obj[3]>0:
													return 'True'
												else: return 'True'
											elif obj[10]>0.0:
												return 'False'
											else: return 'False'
										else: return 'False'
									else: return 'False'
								elif obj[11]>0:
									# {"feature": "Time", "instances": 28, "metric_value": 0.3636, "depth": 9}
									if obj[1]>0:
										# {"feature": "Education", "instances": 22, "metric_value": 0.3636, "depth": 10}
										if obj[6]<=2:
											# {"feature": "Gender", "instances": 16, "metric_value": 0.2727, "depth": 11}
											if obj[3]>0:
												# {"feature": "Children", "instances": 11, "metric_value": 0.3636, "depth": 12}
												if obj[5]<=0:
													# {"feature": "Restaurant20to50", "instances": 9, "metric_value": 0.4444, "depth": 13}
													if obj[10]<=0.0:
														return 'False'
													elif obj[10]>0.0:
														return 'False'
													else: return 'False'
												elif obj[5]>0:
													return 'False'
												else: return 'False'
											elif obj[3]<=0:
												return 'True'
											else: return 'True'
										elif obj[6]>2:
											return 'False'
										else: return 'False'
									elif obj[1]<=0:
										return 'True'
									else: return 'True'
								else: return 'True'
							else: return 'False'
						elif obj[4]>5:
							# {"feature": "Occupation", "instances": 74, "metric_value": 0.3997, "depth": 7}
							if obj[7]<=11:
								# {"feature": "Time", "instances": 62, "metric_value": 0.3637, "depth": 8}
								if obj[1]<=1:
									# {"feature": "Education", "instances": 42, "metric_value": 0.2961, "depth": 9}
									if obj[6]>0:
										# {"feature": "Gender", "instances": 29, "metric_value": 0.2318, "depth": 10}
										if obj[3]>0:
											# {"feature": "Restaurant20to50", "instances": 16, "metric_value": 0.2946, "depth": 11}
											if obj[10]<=1.0:
												# {"feature": "Children", "instances": 14, "metric_value": 0.3333, "depth": 12}
												if obj[5]>0:
													# {"feature": "Direction_same", "instances": 8, "metric_value": 0.375, "depth": 13}
													if obj[11]>0:
														return 'False'
													elif obj[11]<=0:
														return 'False'
													else: return 'False'
												elif obj[5]<=0:
													# {"feature": "Direction_same", "instances": 6, "metric_value": 0.25, "depth": 13}
													if obj[11]<=0:
														return 'False'
													elif obj[11]>0:
														return 'False'
													else: return 'False'
												else: return 'False'
											elif obj[10]>1.0:
												return 'False'
											else: return 'False'
										elif obj[3]<=0:
											# {"feature": "Restaurant20to50", "instances": 13, "metric_value": 0.1231, "depth": 11}
											if obj[10]<=1.0:
												return 'False'
											elif obj[10]>1.0:
												# {"feature": "Children", "instances": 5, "metric_value": 0.32, "depth": 12}
												if obj[5]<=1:
													# {"feature": "Direction_same", "instances": 5, "metric_value": 0.32, "depth": 13}
													if obj[11]<=0:
														return 'False'
													else: return 'False'
												else: return 'False'
											else: return 'False'
										else: return 'False'
									elif obj[6]<=0:
										# {"feature": "Direction_same", "instances": 13, "metric_value": 0.3192, "depth": 10}
										if obj[11]<=0:
											# {"feature": "Children", "instances": 8, "metric_value": 0.1667, "depth": 11}
											if obj[5]<=0:
												return 'False'
											elif obj[5]>0:
												# {"feature": "Gender", "instances": 3, "metric_value": 0.4444, "depth": 12}
												if obj[3]<=1:
													# {"feature": "Restaurant20to50", "instances": 3, "metric_value": 0.4444, "depth": 13}
													if obj[10]<=0.0:
														return 'False'
													else: return 'False'
												else: return 'False'
											else: return 'False'
										elif obj[11]>0:
											# {"feature": "Restaurant20to50", "instances": 5, "metric_value": 0.3, "depth": 11}
											if obj[10]>0.0:
												# {"feature": "Gender", "instances": 4, "metric_value": 0.3333, "depth": 12}
												if obj[3]<=0:
													# {"feature": "Children", "instances": 3, "metric_value": 0.4444, "depth": 13}
													if obj[5]<=0:
														return 'True'
													else: return 'True'
												elif obj[3]>0:
													return 'True'
												else: return 'True'
											elif obj[10]<=0.0:
												return 'False'
											else: return 'False'
										else: return 'True'
									else: return 'False'
								elif obj[1]>1:
									# {"feature": "Education", "instances": 20, "metric_value": 0.419, "depth": 9}
									if obj[6]<=2:
										# {"feature": "Children", "instances": 14, "metric_value": 0.3673, "depth": 10}
										if obj[5]>0:
											# {"feature": "Restaurant20to50", "instances": 7, "metric_value": 0.1429, "depth": 11}
											if obj[10]>0.0:
												return 'False'
											elif obj[10]<=0.0:
												# {"feature": "Gender", "instances": 2, "metric_value": 0.5, "depth": 12}
												if obj[3]<=0:
													# {"feature": "Direction_same", "instances": 2, "metric_value": 0.5, "depth": 13}
													if obj[11]<=0:
														return 'False'
													else: return 'False'
												else: return 'False'
											else: return 'False'
										elif obj[5]<=0:
											# {"feature": "Restaurant20to50", "instances": 7, "metric_value": 0.4286, "depth": 11}
											if obj[10]>0.0:
												# {"feature": "Gender", "instances": 6, "metric_value": 0.5, "depth": 12}
												if obj[3]<=0:
													# {"feature": "Direction_same", "instances": 4, "metric_value": 0.5, "depth": 13}
													if obj[11]<=0:
														return 'True'
													else: return 'True'
												elif obj[3]>0:
													# {"feature": "Direction_same", "instances": 2, "metric_value": 0.5, "depth": 13}
													if obj[11]<=0:
														return 'True'
													else: return 'True'
												else: return 'True'
											elif obj[10]<=0.0:
												return 'False'
											else: return 'False'
										else: return 'False'
									elif obj[6]>2:
										# {"feature": "Children", "instances": 6, "metric_value": 0.2667, "depth": 10}
										if obj[5]>0:
											# {"feature": "Gender", "instances": 5, "metric_value": 0.2667, "depth": 11}
											if obj[3]<=0:
												# {"feature": "Restaurant20to50", "instances": 3, "metric_value": 0.4444, "depth": 12}
												if obj[10]<=2.0:
													# {"feature": "Direction_same", "instances": 3, "metric_value": 0.4444, "depth": 13}
													if obj[11]<=0:
														return 'True'
													else: return 'True'
												else: return 'True'
											elif obj[3]>0:
												return 'True'
											else: return 'True'
										elif obj[5]<=0:
											return 'False'
										else: return 'False'
									else: return 'True'
								else: return 'False'
							elif obj[7]>11:
								# {"feature": "Restaurant20to50", "instances": 12, "metric_value": 0.419, "depth": 8}
								if obj[10]>0.0:
									# {"feature": "Direction_same", "instances": 7, "metric_value": 0.381, "depth": 9}
									if obj[11]<=0:
										# {"feature": "Education", "instances": 6, "metric_value": 0.3333, "depth": 10}
										if obj[6]<=1:
											# {"feature": "Time", "instances": 4, "metric_value": 0.3333, "depth": 11}
											if obj[1]>0:
												# {"feature": "Gender", "instances": 3, "metric_value": 0.4444, "depth": 12}
												if obj[3]<=1:
													# {"feature": "Children", "instances": 3, "metric_value": 0.4444, "depth": 13}
													if obj[5]<=1:
														return 'True'
													else: return 'True'
												else: return 'True'
											elif obj[1]<=0:
												return 'False'
											else: return 'False'
										elif obj[6]>1:
											return 'False'
										else: return 'False'
									elif obj[11]>0:
										return 'True'
									else: return 'True'
								elif obj[10]<=0.0:
									# {"feature": "Time", "instances": 5, "metric_value": 0.2, "depth": 9}
									if obj[1]>0:
										return 'True'
									elif obj[1]<=0:
										# {"feature": "Gender", "instances": 2, "metric_value": 0.5, "depth": 10}
										if obj[3]<=0:
											# {"feature": "Children", "instances": 2, "metric_value": 0.5, "depth": 11}
											if obj[5]<=1:
												# {"feature": "Education", "instances": 2, "metric_value": 0.5, "depth": 12}
												if obj[6]<=1:
													# {"feature": "Direction_same", "instances": 2, "metric_value": 0.5, "depth": 13}
													if obj[11]<=1:
														return 'False'
													else: return 'False'
												else: return 'False'
											else: return 'False'
										else: return 'False'
									else: return 'False'
								else: return 'True'
							else: return 'True'
						else: return 'False'
					elif obj[8]>1.0:
						# {"feature": "Occupation", "instances": 86, "metric_value": 0.3849, "depth": 6}
						if obj[7]>5:
							# {"feature": "Gender", "instances": 64, "metric_value": 0.4295, "depth": 7}
							if obj[3]<=0:
								# {"feature": "Education", "instances": 55, "metric_value": 0.3958, "depth": 8}
								if obj[6]<=2:
									# {"feature": "Direction_same", "instances": 49, "metric_value": 0.3444, "depth": 9}
									if obj[11]<=0:
										# {"feature": "Restaurant20to50", "instances": 38, "metric_value": 0.2653, "depth": 10}
										if obj[10]<=1.0:
											# {"feature": "Age", "instances": 25, "metric_value": 0.3537, "depth": 11}
											if obj[4]>0:
												# {"feature": "Time", "instances": 19, "metric_value": 0.4334, "depth": 12}
												if obj[1]>0:
													# {"feature": "Children", "instances": 17, "metric_value": 0.4777, "depth": 13}
													if obj[5]<=0:
														return 'False'
													elif obj[5]>0:
														return 'False'
													else: return 'False'
												elif obj[1]<=0:
													return 'False'
												else: return 'False'
											elif obj[4]<=0:
												return 'False'
											else: return 'False'
										elif obj[10]>1.0:
											return 'False'
										else: return 'False'
									elif obj[11]>0:
										# {"feature": "Time", "instances": 11, "metric_value": 0.297, "depth": 10}
										if obj[1]<=0:
											# {"feature": "Age", "instances": 6, "metric_value": 0.1667, "depth": 11}
											if obj[4]>0:
												return 'True'
											elif obj[4]<=0:
												# {"feature": "Children", "instances": 2, "metric_value": 0.0, "depth": 12}
												if obj[5]<=0:
													return 'True'
												elif obj[5]>0:
													return 'False'
												else: return 'False'
											else: return 'True'
										elif obj[1]>0:
											# {"feature": "Age", "instances": 5, "metric_value": 0.2, "depth": 11}
											if obj[4]>0:
												return 'False'
											elif obj[4]<=0:
												# {"feature": "Children", "instances": 2, "metric_value": 0.5, "depth": 12}
												if obj[5]<=0:
													# {"feature": "Restaurant20to50", "instances": 2, "metric_value": 0.5, "depth": 13}
													if obj[10]<=0.0:
														return 'True'
													else: return 'True'
												else: return 'True'
											else: return 'True'
										else: return 'False'
									else: return 'True'
								elif obj[6]>2:
									# {"feature": "Direction_same", "instances": 6, "metric_value": 0.2667, "depth": 9}
									if obj[11]<=0:
										# {"feature": "Time", "instances": 5, "metric_value": 0.2667, "depth": 10}
										if obj[1]<=1:
											# {"feature": "Age", "instances": 3, "metric_value": 0.4444, "depth": 11}
											if obj[4]<=0:
												# {"feature": "Children", "instances": 3, "metric_value": 0.4444, "depth": 12}
												if obj[5]<=0:
													# {"feature": "Restaurant20to50", "instances": 3, "metric_value": 0.4444, "depth": 13}
													if obj[10]<=1.0:
														return 'True'
													else: return 'True'
												else: return 'True'
											else: return 'True'
										elif obj[1]>1:
											return 'True'
										else: return 'True'
									elif obj[11]>0:
										return 'False'
									else: return 'False'
								else: return 'True'
							elif obj[3]>0:
								# {"feature": "Education", "instances": 9, "metric_value": 0.3333, "depth": 8}
								if obj[6]<=0:
									# {"feature": "Time", "instances": 8, "metric_value": 0.3333, "depth": 9}
									if obj[1]<=2:
										# {"feature": "Children", "instances": 6, "metric_value": 0.2222, "depth": 10}
										if obj[5]<=0:
											return 'True'
										elif obj[5]>0:
											# {"feature": "Age", "instances": 3, "metric_value": 0.4444, "depth": 11}
											if obj[4]<=1:
												# {"feature": "Restaurant20to50", "instances": 3, "metric_value": 0.4444, "depth": 12}
												if obj[10]<=2.0:
													# {"feature": "Direction_same", "instances": 3, "metric_value": 0.4444, "depth": 13}
													if obj[11]<=0:
														return 'True'
													else: return 'True'
												else: return 'True'
											else: return 'True'
										else: return 'True'
									elif obj[1]>2:
										# {"feature": "Children", "instances": 2, "metric_value": 0.0, "depth": 10}
										if obj[5]<=0:
											return 'False'
										elif obj[5]>0:
											return 'True'
										else: return 'True'
									else: return 'False'
								elif obj[6]>0:
									return 'False'
								else: return 'False'
							else: return 'True'
						elif obj[7]<=5:
							# {"feature": "Time", "instances": 22, "metric_value": 0.0909, "depth": 7}
							if obj[1]>0:
								return 'False'
							elif obj[1]<=0:
								# {"feature": "Gender", "instances": 4, "metric_value": 0.3333, "depth": 8}
								if obj[3]<=0:
									# {"feature": "Education", "instances": 3, "metric_value": 0.0, "depth": 9}
									if obj[6]>0:
										return 'False'
									elif obj[6]<=0:
										return 'True'
									else: return 'True'
								elif obj[3]>0:
									return 'True'
								else: return 'True'
							else: return 'False'
						else: return 'False'
					else: return 'False'
				else: return 'False'
			elif obj[0]>1:
				# {"feature": "Distance", "instances": 527, "metric_value": 0.4617, "depth": 4}
				if obj[12]>1:
					# {"feature": "Bar", "instances": 356, "metric_value": 0.4414, "depth": 5}
					if obj[8]<=2.0:
						# {"feature": "Time", "instances": 323, "metric_value": 0.4297, "depth": 6}
						if obj[1]>0:
							# {"feature": "Age", "instances": 252, "metric_value": 0.4492, "depth": 7}
							if obj[4]>1:
								# {"feature": "Occupation", "instances": 178, "metric_value": 0.4665, "depth": 8}
								if obj[7]<=16:
									# {"feature": "Gender", "instances": 164, "metric_value": 0.4816, "depth": 9}
									if obj[3]>0:
										# {"feature": "Restaurant20to50", "instances": 83, "metric_value": 0.4907, "depth": 10}
										if obj[10]>0.0:
											# {"feature": "Education", "instances": 59, "metric_value": 0.4734, "depth": 11}
											if obj[6]<=3:
												# {"feature": "Children", "instances": 53, "metric_value": 0.4936, "depth": 12}
												if obj[5]>0:
													# {"feature": "Direction_same", "instances": 37, "metric_value": 0.4909, "depth": 13}
													if obj[11]<=0:
														return 'True'
													else: return 'True'
												elif obj[5]<=0:
													# {"feature": "Direction_same", "instances": 16, "metric_value": 0.5, "depth": 13}
													if obj[11]<=0:
														return 'False'
													else: return 'False'
												else: return 'False'
											elif obj[6]>3:
												# {"feature": "Children", "instances": 6, "metric_value": 0.0, "depth": 12}
												if obj[5]<=0:
													return 'True'
												elif obj[5]>0:
													return 'False'
												else: return 'False'
											else: return 'True'
										elif obj[10]<=0.0:
											# {"feature": "Education", "instances": 24, "metric_value": 0.4127, "depth": 11}
											if obj[6]>0:
												# {"feature": "Children", "instances": 21, "metric_value": 0.4505, "depth": 12}
												if obj[5]>0:
													# {"feature": "Direction_same", "instances": 13, "metric_value": 0.497, "depth": 13}
													if obj[11]<=0:
														return 'False'
													else: return 'False'
												elif obj[5]<=0:
													# {"feature": "Direction_same", "instances": 8, "metric_value": 0.375, "depth": 13}
													if obj[11]<=0:
														return 'False'
													else: return 'False'
												else: return 'False'
											elif obj[6]<=0:
												return 'True'
											else: return 'True'
										else: return 'False'
									elif obj[3]<=0:
										# {"feature": "Restaurant20to50", "instances": 81, "metric_value": 0.4567, "depth": 10}
										if obj[10]<=1.0:
											# {"feature": "Education", "instances": 64, "metric_value": 0.4742, "depth": 11}
											if obj[6]<=1:
												# {"feature": "Children", "instances": 37, "metric_value": 0.4556, "depth": 12}
												if obj[5]<=0:
													# {"feature": "Direction_same", "instances": 28, "metric_value": 0.4592, "depth": 13}
													if obj[11]<=0:
														return 'True'
													else: return 'True'
												elif obj[5]>0:
													# {"feature": "Direction_same", "instances": 9, "metric_value": 0.4444, "depth": 13}
													if obj[11]<=0:
														return 'True'
													else: return 'True'
												else: return 'True'
											elif obj[6]>1:
												# {"feature": "Children", "instances": 27, "metric_value": 0.4937, "depth": 12}
												if obj[5]<=0:
													# {"feature": "Direction_same", "instances": 16, "metric_value": 0.4922, "depth": 13}
													if obj[11]<=0:
														return 'True'
													else: return 'True'
												elif obj[5]>0:
													# {"feature": "Direction_same", "instances": 11, "metric_value": 0.4959, "depth": 13}
													if obj[11]<=0:
														return 'False'
													else: return 'False'
												else: return 'False'
											else: return 'True'
										elif obj[10]>1.0:
											# {"feature": "Children", "instances": 17, "metric_value": 0.3252, "depth": 11}
											if obj[5]>0:
												# {"feature": "Education", "instances": 9, "metric_value": 0.1905, "depth": 12}
												if obj[6]>0:
													# {"feature": "Direction_same", "instances": 7, "metric_value": 0.2449, "depth": 13}
													if obj[11]<=0:
														return 'True'
													else: return 'True'
												elif obj[6]<=0:
													return 'True'
												else: return 'True'
											elif obj[5]<=0:
												# {"feature": "Education", "instances": 8, "metric_value": 0.4688, "depth": 12}
												if obj[6]<=2:
													# {"feature": "Direction_same", "instances": 8, "metric_value": 0.4688, "depth": 13}
													if obj[11]<=0:
														return 'True'
													else: return 'True'
												else: return 'True'
											else: return 'True'
										else: return 'True'
									else: return 'True'
								elif obj[7]>16:
									# {"feature": "Education", "instances": 14, "metric_value": 0.2143, "depth": 9}
									if obj[6]<=0:
										# {"feature": "Children", "instances": 8, "metric_value": 0.3, "depth": 10}
										if obj[5]>0:
											# {"feature": "Gender", "instances": 5, "metric_value": 0.48, "depth": 11}
											if obj[3]<=1:
												# {"feature": "Restaurant20to50", "instances": 5, "metric_value": 0.48, "depth": 12}
												if obj[10]<=1.0:
													# {"feature": "Direction_same", "instances": 5, "metric_value": 0.48, "depth": 13}
													if obj[11]<=0:
														return 'True'
													else: return 'True'
												else: return 'True'
											else: return 'True'
										elif obj[5]<=0:
											return 'True'
										else: return 'True'
									elif obj[6]>0:
										return 'True'
									else: return 'True'
								else: return 'True'
							elif obj[4]<=1:
								# {"feature": "Occupation", "instances": 74, "metric_value": 0.3665, "depth": 8}
								if obj[7]<=22:
									# {"feature": "Restaurant20to50", "instances": 73, "metric_value": 0.3587, "depth": 9}
									if obj[10]>-1.0:
										# {"feature": "Education", "instances": 66, "metric_value": 0.3934, "depth": 10}
										if obj[6]>1:
											# {"feature": "Gender", "instances": 43, "metric_value": 0.4059, "depth": 11}
											if obj[3]<=0:
												# {"feature": "Children", "instances": 32, "metric_value": 0.3744, "depth": 12}
												if obj[5]<=0:
													# {"feature": "Direction_same", "instances": 23, "metric_value": 0.3856, "depth": 13}
													if obj[11]<=0:
														return 'True'
													else: return 'True'
												elif obj[5]>0:
													# {"feature": "Direction_same", "instances": 9, "metric_value": 0.3457, "depth": 13}
													if obj[11]<=0:
														return 'True'
													else: return 'True'
												else: return 'True'
											elif obj[3]>0:
												# {"feature": "Children", "instances": 11, "metric_value": 0.3879, "depth": 12}
												if obj[5]>0:
													# {"feature": "Direction_same", "instances": 6, "metric_value": 0.4444, "depth": 13}
													if obj[11]<=0:
														return 'False'
													else: return 'False'
												elif obj[5]<=0:
													# {"feature": "Direction_same", "instances": 5, "metric_value": 0.32, "depth": 13}
													if obj[11]<=0:
														return 'True'
													else: return 'True'
												else: return 'True'
											else: return 'True'
										elif obj[6]<=1:
											# {"feature": "Gender", "instances": 23, "metric_value": 0.3401, "depth": 11}
											if obj[3]>0:
												# {"feature": "Children", "instances": 18, "metric_value": 0.3333, "depth": 12}
												if obj[5]>0:
													# {"feature": "Direction_same", "instances": 16, "metric_value": 0.375, "depth": 13}
													if obj[11]<=0:
														return 'True'
													else: return 'True'
												elif obj[5]<=0:
													return 'True'
												else: return 'True'
											elif obj[3]<=0:
												# {"feature": "Children", "instances": 5, "metric_value": 0.2667, "depth": 12}
												if obj[5]<=0:
													# {"feature": "Direction_same", "instances": 3, "metric_value": 0.4444, "depth": 13}
													if obj[11]<=0:
														return 'True'
													else: return 'True'
												elif obj[5]>0:
													return 'True'
												else: return 'True'
											else: return 'True'
										else: return 'True'
									elif obj[10]<=-1.0:
										return 'True'
									else: return 'True'
								elif obj[7]>22:
									return 'False'
								else: return 'False'
							else: return 'True'
						elif obj[1]<=0:
							# {"feature": "Children", "instances": 71, "metric_value": 0.2679, "depth": 7}
							if obj[5]>0:
								# {"feature": "Age", "instances": 41, "metric_value": 0.3777, "depth": 8}
								if obj[4]<=3:
									# {"feature": "Restaurant20to50", "instances": 31, "metric_value": 0.4424, "depth": 9}
									if obj[10]>-1.0:
										# {"feature": "Occupation", "instances": 28, "metric_value": 0.4762, "depth": 10}
										if obj[7]>0:
											# {"feature": "Gender", "instances": 27, "metric_value": 0.4889, "depth": 11}
											if obj[3]>0:
												# {"feature": "Education", "instances": 15, "metric_value": 0.4571, "depth": 12}
												if obj[6]<=2:
													# {"feature": "Direction_same", "instances": 14, "metric_value": 0.4898, "depth": 13}
													if obj[11]<=0:
														return 'True'
													else: return 'True'
												elif obj[6]>2:
													return 'True'
												else: return 'True'
											elif obj[3]<=0:
												# {"feature": "Education", "instances": 12, "metric_value": 0.5, "depth": 12}
												if obj[6]>0:
													# {"feature": "Direction_same", "instances": 10, "metric_value": 0.5, "depth": 13}
													if obj[11]<=0:
														return 'True'
													else: return 'True'
												elif obj[6]<=0:
													# {"feature": "Direction_same", "instances": 2, "metric_value": 0.5, "depth": 13}
													if obj[11]<=0:
														return 'True'
													else: return 'True'
												else: return 'True'
											else: return 'True'
										elif obj[7]<=0:
											return 'True'
										else: return 'True'
									elif obj[10]<=-1.0:
										return 'False'
									else: return 'False'
								elif obj[4]>3:
									return 'True'
								else: return 'True'
							elif obj[5]<=0:
								return 'True'
							else: return 'True'
						else: return 'True'
					elif obj[8]>2.0:
						# {"feature": "Children", "instances": 33, "metric_value": 0.4127, "depth": 6}
						if obj[5]<=0:
							# {"feature": "Time", "instances": 21, "metric_value": 0.4286, "depth": 7}
							if obj[1]>0:
								# {"feature": "Age", "instances": 18, "metric_value": 0.4643, "depth": 8}
								if obj[4]<=1:
									# {"feature": "Occupation", "instances": 14, "metric_value": 0.4762, "depth": 9}
									if obj[7]>2:
										# {"feature": "Education", "instances": 8, "metric_value": 0.4667, "depth": 10}
										if obj[6]<=0:
											# {"feature": "Gender", "instances": 5, "metric_value": 0.48, "depth": 11}
											if obj[3]<=0:
												# {"feature": "Restaurant20to50", "instances": 5, "metric_value": 0.48, "depth": 12}
												if obj[10]<=0.0:
													# {"feature": "Direction_same", "instances": 5, "metric_value": 0.48, "depth": 13}
													if obj[11]<=0:
														return 'False'
													else: return 'False'
												else: return 'False'
											else: return 'False'
										elif obj[6]>0:
											# {"feature": "Gender", "instances": 3, "metric_value": 0.4444, "depth": 11}
											if obj[3]<=0:
												# {"feature": "Restaurant20to50", "instances": 3, "metric_value": 0.4444, "depth": 12}
												if obj[10]<=1.0:
													# {"feature": "Direction_same", "instances": 3, "metric_value": 0.4444, "depth": 13}
													if obj[11]<=0:
														return 'True'
													else: return 'True'
												else: return 'True'
											else: return 'True'
										else: return 'True'
									elif obj[7]<=2:
										# {"feature": "Gender", "instances": 6, "metric_value": 0.4444, "depth": 10}
										if obj[3]>0:
											# {"feature": "Education", "instances": 3, "metric_value": 0.4444, "depth": 11}
											if obj[6]<=4:
												# {"feature": "Restaurant20to50", "instances": 3, "metric_value": 0.4444, "depth": 12}
												if obj[10]<=1.0:
													# {"feature": "Direction_same", "instances": 3, "metric_value": 0.4444, "depth": 13}
													if obj[11]<=0:
														return 'False'
													else: return 'False'
												else: return 'False'
											else: return 'False'
										elif obj[3]<=0:
											# {"feature": "Education", "instances": 3, "metric_value": 0.4444, "depth": 11}
											if obj[6]<=2:
												# {"feature": "Restaurant20to50", "instances": 3, "metric_value": 0.4444, "depth": 12}
												if obj[10]<=1.0:
													# {"feature": "Direction_same", "instances": 3, "metric_value": 0.4444, "depth": 13}
													if obj[11]<=0:
														return 'False'
													else: return 'False'
												else: return 'False'
											else: return 'False'
										else: return 'False'
									else: return 'False'
								elif obj[4]>1:
									# {"feature": "Education", "instances": 4, "metric_value": 0.3333, "depth": 9}
									if obj[6]<=1:
										# {"feature": "Gender", "instances": 3, "metric_value": 0.4444, "depth": 10}
										if obj[3]<=0:
											# {"feature": "Occupation", "instances": 3, "metric_value": 0.4444, "depth": 11}
											if obj[7]<=18:
												# {"feature": "Restaurant20to50", "instances": 3, "metric_value": 0.4444, "depth": 12}
												if obj[10]<=2.0:
													# {"feature": "Direction_same", "instances": 3, "metric_value": 0.4444, "depth": 13}
													if obj[11]<=0:
														return 'True'
													else: return 'True'
												else: return 'True'
											else: return 'True'
										else: return 'True'
									elif obj[6]>1:
										return 'True'
									else: return 'True'
								else: return 'True'
							elif obj[1]<=0:
								return 'True'
							else: return 'True'
						elif obj[5]>0:
							# {"feature": "Age", "instances": 12, "metric_value": 0.2381, "depth": 7}
							if obj[4]>2:
								# {"feature": "Time", "instances": 7, "metric_value": 0.381, "depth": 8}
								if obj[1]>0:
									# {"feature": "Gender", "instances": 6, "metric_value": 0.4444, "depth": 9}
									if obj[3]<=0:
										# {"feature": "Education", "instances": 6, "metric_value": 0.4444, "depth": 10}
										if obj[6]<=2:
											# {"feature": "Occupation", "instances": 6, "metric_value": 0.4444, "depth": 11}
											if obj[7]<=12:
												# {"feature": "Restaurant20to50", "instances": 6, "metric_value": 0.4444, "depth": 12}
												if obj[10]<=2.0:
													# {"feature": "Direction_same", "instances": 6, "metric_value": 0.4444, "depth": 13}
													if obj[11]<=0:
														return 'False'
													else: return 'False'
												else: return 'False'
											else: return 'False'
										else: return 'False'
									else: return 'False'
								elif obj[1]<=0:
									return 'False'
								else: return 'False'
							elif obj[4]<=2:
								return 'False'
							else: return 'False'
						else: return 'False'
					else: return 'False'
				elif obj[12]<=1:
					# {"feature": "Occupation", "instances": 171, "metric_value": 0.4644, "depth": 5}
					if obj[7]>1.3264107549745603:
						# {"feature": "Age", "instances": 137, "metric_value": 0.4449, "depth": 6}
						if obj[4]<=2:
							# {"feature": "Education", "instances": 76, "metric_value": 0.4768, "depth": 7}
							if obj[6]<=3:
								# {"feature": "Restaurant20to50", "instances": 67, "metric_value": 0.4602, "depth": 8}
								if obj[10]>-1.0:
									# {"feature": "Time", "instances": 59, "metric_value": 0.4807, "depth": 9}
									if obj[1]<=3:
										# {"feature": "Children", "instances": 43, "metric_value": 0.4776, "depth": 10}
										if obj[5]<=0:
											# {"feature": "Bar", "instances": 27, "metric_value": 0.451, "depth": 11}
											if obj[8]>0.0:
												# {"feature": "Gender", "instances": 14, "metric_value": 0.3929, "depth": 12}
												if obj[3]<=0:
													# {"feature": "Direction_same", "instances": 12, "metric_value": 0.375, "depth": 13}
													if obj[11]<=0:
														return 'False'
													else: return 'False'
												elif obj[3]>0:
													# {"feature": "Direction_same", "instances": 2, "metric_value": 0.5, "depth": 13}
													if obj[11]<=0:
														return 'True'
													else: return 'True'
												else: return 'True'
											elif obj[8]<=0.0:
												# {"feature": "Gender", "instances": 13, "metric_value": 0.3538, "depth": 12}
												if obj[3]<=0:
													# {"feature": "Direction_same", "instances": 8, "metric_value": 0.375, "depth": 13}
													if obj[11]<=0:
														return 'True'
													else: return 'True'
												elif obj[3]>0:
													# {"feature": "Direction_same", "instances": 5, "metric_value": 0.32, "depth": 13}
													if obj[11]<=0:
														return 'False'
													else: return 'False'
												else: return 'False'
											else: return 'True'
										elif obj[5]>0:
											# {"feature": "Bar", "instances": 16, "metric_value": 0.3, "depth": 11}
											if obj[8]<=0.0:
												# {"feature": "Gender", "instances": 10, "metric_value": 0.3167, "depth": 12}
												if obj[3]<=0:
													# {"feature": "Direction_same", "instances": 6, "metric_value": 0.2778, "depth": 13}
													if obj[11]<=0:
														return 'False'
													else: return 'False'
												elif obj[3]>0:
													# {"feature": "Direction_same", "instances": 4, "metric_value": 0.375, "depth": 13}
													if obj[11]<=0:
														return 'True'
													else: return 'True'
												else: return 'True'
											elif obj[8]>0.0:
												return 'True'
											else: return 'True'
										else: return 'True'
									elif obj[1]>3:
										# {"feature": "Gender", "instances": 16, "metric_value": 0.4042, "depth": 10}
										if obj[3]<=0:
											# {"feature": "Bar", "instances": 10, "metric_value": 0.4444, "depth": 11}
											if obj[8]<=1.0:
												# {"feature": "Children", "instances": 9, "metric_value": 0.4815, "depth": 12}
												if obj[5]>0:
													# {"feature": "Direction_same", "instances": 6, "metric_value": 0.5, "depth": 13}
													if obj[11]<=0:
														return 'False'
													else: return 'False'
												elif obj[5]<=0:
													# {"feature": "Direction_same", "instances": 3, "metric_value": 0.4444, "depth": 13}
													if obj[11]<=0:
														return 'False'
													else: return 'False'
												else: return 'False'
											elif obj[8]>1.0:
												return 'False'
											else: return 'False'
										elif obj[3]>0:
											# {"feature": "Children", "instances": 6, "metric_value": 0.2667, "depth": 11}
											if obj[5]>0:
												# {"feature": "Bar", "instances": 5, "metric_value": 0.32, "depth": 12}
												if obj[8]<=0.0:
													# {"feature": "Direction_same", "instances": 5, "metric_value": 0.32, "depth": 13}
													if obj[11]<=0:
														return 'False'
													else: return 'False'
												else: return 'False'
											elif obj[5]<=0:
												return 'False'
											else: return 'False'
										else: return 'False'
									else: return 'False'
								elif obj[10]<=-1.0:
									# {"feature": "Bar", "instances": 8, "metric_value": 0.2, "depth": 9}
									if obj[8]<=-1.0:
										# {"feature": "Time", "instances": 5, "metric_value": 0.2667, "depth": 10}
										if obj[1]>0:
											# {"feature": "Children", "instances": 3, "metric_value": 0.3333, "depth": 11}
											if obj[5]>0:
												# {"feature": "Gender", "instances": 2, "metric_value": 0.5, "depth": 12}
												if obj[3]<=0:
													# {"feature": "Direction_same", "instances": 2, "metric_value": 0.5, "depth": 13}
													if obj[11]<=0:
														return 'True'
													else: return 'True'
												else: return 'True'
											elif obj[5]<=0:
												return 'False'
											else: return 'False'
										elif obj[1]<=0:
											return 'False'
										else: return 'False'
									elif obj[8]>-1.0:
										return 'False'
									else: return 'False'
								else: return 'False'
							elif obj[6]>3:
								# {"feature": "Bar", "instances": 9, "metric_value": 0.0, "depth": 8}
								if obj[8]<=0.0:
									return 'True'
								elif obj[8]>0.0:
									return 'False'
								else: return 'False'
							else: return 'True'
						elif obj[4]>2:
							# {"feature": "Restaurant20to50", "instances": 61, "metric_value": 0.3305, "depth": 7}
							if obj[10]>0.0:
								# {"feature": "Time", "instances": 38, "metric_value": 0.1887, "depth": 8}
								if obj[1]>0:
									# {"feature": "Bar", "instances": 31, "metric_value": 0.1105, "depth": 9}
									if obj[8]<=2.0:
										# {"feature": "Children", "instances": 27, "metric_value": 0.0673, "depth": 10}
										if obj[5]<=0:
											return 'False'
										elif obj[5]>0:
											# {"feature": "Gender", "instances": 11, "metric_value": 0.1455, "depth": 11}
											if obj[3]>0:
												return 'False'
											elif obj[3]<=0:
												# {"feature": "Education", "instances": 5, "metric_value": 0.2667, "depth": 12}
												if obj[6]<=2:
													# {"feature": "Direction_same", "instances": 3, "metric_value": 0.4444, "depth": 13}
													if obj[11]<=0:
														return 'False'
													else: return 'False'
												elif obj[6]>2:
													return 'False'
												else: return 'False'
											else: return 'False'
										else: return 'False'
									elif obj[8]>2.0:
										# {"feature": "Children", "instances": 4, "metric_value": 0.3333, "depth": 10}
										if obj[5]<=0:
											# {"feature": "Education", "instances": 3, "metric_value": 0.3333, "depth": 11}
											if obj[6]>1:
												# {"feature": "Gender", "instances": 2, "metric_value": 0.5, "depth": 12}
												if obj[3]<=0:
													# {"feature": "Direction_same", "instances": 2, "metric_value": 0.5, "depth": 13}
													if obj[11]<=0:
														return 'False'
													else: return 'False'
												else: return 'False'
											elif obj[6]<=1:
												return 'False'
											else: return 'False'
										elif obj[5]>0:
											return 'False'
										else: return 'False'
									else: return 'False'
								elif obj[1]<=0:
									# {"feature": "Children", "instances": 7, "metric_value": 0.2143, "depth": 9}
									if obj[5]>0:
										# {"feature": "Gender", "instances": 4, "metric_value": 0.0, "depth": 10}
										if obj[3]<=0:
											return 'True'
										elif obj[3]>0:
											return 'False'
										else: return 'False'
									elif obj[5]<=0:
										return 'False'
									else: return 'False'
								else: return 'False'
							elif obj[10]<=0.0:
								# {"feature": "Bar", "instances": 23, "metric_value": 0.4174, "depth": 8}
								if obj[8]<=1.0:
									# {"feature": "Gender", "instances": 20, "metric_value": 0.4125, "depth": 9}
									if obj[3]<=0:
										# {"feature": "Education", "instances": 12, "metric_value": 0.2727, "depth": 10}
										if obj[6]<=3:
											# {"feature": "Time", "instances": 11, "metric_value": 0.2525, "depth": 11}
											if obj[1]<=3:
												# {"feature": "Children", "instances": 9, "metric_value": 0.1852, "depth": 12}
												if obj[5]<=0:
													# {"feature": "Direction_same", "instances": 6, "metric_value": 0.2778, "depth": 13}
													if obj[11]<=0:
														return 'False'
													else: return 'False'
												elif obj[5]>0:
													return 'False'
												else: return 'False'
											elif obj[1]>3:
												# {"feature": "Children", "instances": 2, "metric_value": 0.0, "depth": 12}
												if obj[5]>0:
													return 'True'
												elif obj[5]<=0:
													return 'False'
												else: return 'False'
											else: return 'True'
										elif obj[6]>3:
											return 'True'
										else: return 'True'
									elif obj[3]>0:
										# {"feature": "Children", "instances": 8, "metric_value": 0.2083, "depth": 10}
										if obj[5]<=0:
											# {"feature": "Time", "instances": 6, "metric_value": 0.1667, "depth": 11}
											if obj[1]>0:
												return 'True'
											elif obj[1]<=0:
												# {"feature": "Education", "instances": 2, "metric_value": 0.0, "depth": 12}
												if obj[6]<=0:
													return 'True'
												elif obj[6]>0:
													return 'False'
												else: return 'False'
											else: return 'True'
										elif obj[5]>0:
											return 'False'
										else: return 'False'
									else: return 'True'
								elif obj[8]>1.0:
									return 'True'
								else: return 'True'
							else: return 'False'
						else: return 'False'
					elif obj[7]<=1.3264107549745603:
						# {"feature": "Education", "instances": 34, "metric_value": 0.444, "depth": 6}
						if obj[6]>1:
							# {"feature": "Age", "instances": 18, "metric_value": 0.2738, "depth": 7}
							if obj[4]<=4:
								# {"feature": "Time", "instances": 14, "metric_value": 0.1429, "depth": 8}
								if obj[1]>0:
									return 'True'
								elif obj[1]<=0:
									# {"feature": "Bar", "instances": 4, "metric_value": 0.3333, "depth": 9}
									if obj[8]>-1.0:
										# {"feature": "Gender", "instances": 3, "metric_value": 0.3333, "depth": 10}
										if obj[3]>0:
											# {"feature": "Children", "instances": 2, "metric_value": 0.5, "depth": 11}
											if obj[5]<=0:
												# {"feature": "Restaurant20to50", "instances": 2, "metric_value": 0.5, "depth": 12}
												if obj[10]<=1.0:
													# {"feature": "Direction_same", "instances": 2, "metric_value": 0.5, "depth": 13}
													if obj[11]<=0:
														return 'False'
													else: return 'False'
												else: return 'False'
											else: return 'False'
										elif obj[3]<=0:
											return 'True'
										else: return 'True'
									elif obj[8]<=-1.0:
										return 'False'
									else: return 'False'
								else: return 'False'
							elif obj[4]>4:
								# {"feature": "Time", "instances": 4, "metric_value": 0.25, "depth": 8}
								if obj[1]>3:
									# {"feature": "Children", "instances": 2, "metric_value": 0.0, "depth": 9}
									if obj[5]>0:
										return 'True'
									elif obj[5]<=0:
										return 'False'
									else: return 'False'
								elif obj[1]<=3:
									return 'False'
								else: return 'False'
							else: return 'False'
						elif obj[6]<=1:
							# {"feature": "Age", "instances": 16, "metric_value": 0.3571, "depth": 7}
							if obj[4]>2:
								# {"feature": "Time", "instances": 9, "metric_value": 0.3333, "depth": 8}
								if obj[1]<=3:
									# {"feature": "Restaurant20to50", "instances": 6, "metric_value": 0.1667, "depth": 9}
									if obj[10]>0.0:
										return 'True'
									elif obj[10]<=0.0:
										# {"feature": "Gender", "instances": 2, "metric_value": 0.5, "depth": 10}
										if obj[3]<=0:
											# {"feature": "Children", "instances": 2, "metric_value": 0.5, "depth": 11}
											if obj[5]<=1:
												# {"feature": "Bar", "instances": 2, "metric_value": 0.5, "depth": 12}
												if obj[8]<=0.0:
													# {"feature": "Direction_same", "instances": 2, "metric_value": 0.5, "depth": 13}
													if obj[11]<=0:
														return 'False'
													else: return 'False'
												else: return 'False'
											else: return 'False'
										else: return 'False'
									else: return 'False'
								elif obj[1]>3:
									# {"feature": "Restaurant20to50", "instances": 3, "metric_value": 0.3333, "depth": 9}
									if obj[10]<=1.0:
										# {"feature": "Gender", "instances": 2, "metric_value": 0.5, "depth": 10}
										if obj[3]<=1:
											# {"feature": "Children", "instances": 2, "metric_value": 0.5, "depth": 11}
											if obj[5]<=1:
												# {"feature": "Bar", "instances": 2, "metric_value": 0.5, "depth": 12}
												if obj[8]<=0.0:
													# {"feature": "Direction_same", "instances": 2, "metric_value": 0.5, "depth": 13}
													if obj[11]<=0:
														return 'True'
													else: return 'True'
												else: return 'True'
											else: return 'True'
										else: return 'True'
									elif obj[10]>1.0:
										return 'False'
									else: return 'False'
								else: return 'False'
							elif obj[4]<=2:
								# {"feature": "Restaurant20to50", "instances": 7, "metric_value": 0.0, "depth": 8}
								if obj[10]<=1.0:
									return 'False'
								elif obj[10]>1.0:
									return 'True'
								else: return 'True'
							else: return 'False'
						else: return 'False'
					else: return 'True'
				else: return 'False'
			else: return 'True'
		else: return 'True'
	elif obj[2]<=1:
		# {"feature": "Bar", "instances": 2281, "metric_value": 0.4567, "depth": 2}
		if obj[8]<=1.0:
			# {"feature": "Children", "instances": 1601, "metric_value": 0.4408, "depth": 3}
			if obj[5]>0:
				# {"feature": "Occupation", "instances": 804, "metric_value": 0.3945, "depth": 4}
				if obj[7]>1.5424315569353801:
					# {"feature": "Time", "instances": 645, "metric_value": 0.4151, "depth": 5}
					if obj[1]<=3:
						# {"feature": "Coffeehouse", "instances": 565, "metric_value": 0.4343, "depth": 6}
						if obj[9]<=2.0:
							# {"feature": "Distance", "instances": 447, "metric_value": 0.4578, "depth": 7}
							if obj[12]<=2:
								# {"feature": "Restaurant20to50", "instances": 352, "metric_value": 0.4701, "depth": 8}
								if obj[10]<=2.0:
									# {"feature": "Education", "instances": 327, "metric_value": 0.4631, "depth": 9}
									if obj[6]<=2:
										# {"feature": "Direction_same", "instances": 242, "metric_value": 0.4459, "depth": 10}
										if obj[11]<=0:
											# {"feature": "Passanger", "instances": 174, "metric_value": 0.4624, "depth": 11}
											if obj[0]>1:
												# {"feature": "Age", "instances": 90, "metric_value": 0.4263, "depth": 12}
												if obj[4]<=6:
													# {"feature": "Gender", "instances": 83, "metric_value": 0.4108, "depth": 13}
													if obj[3]>0:
														return 'False'
													elif obj[3]<=0:
														return 'False'
													else: return 'False'
												elif obj[4]>6:
													# {"feature": "Gender", "instances": 7, "metric_value": 0.3429, "depth": 13}
													if obj[3]<=0:
														return 'False'
													elif obj[3]>0:
														return 'True'
													else: return 'True'
												else: return 'True'
											elif obj[0]<=1:
												# {"feature": "Age", "instances": 84, "metric_value": 0.4503, "depth": 12}
												if obj[4]<=2:
													# {"feature": "Gender", "instances": 47, "metric_value": 0.4908, "depth": 13}
													if obj[3]>0:
														return 'True'
													elif obj[3]<=0:
														return 'True'
													else: return 'True'
												elif obj[4]>2:
													# {"feature": "Gender", "instances": 37, "metric_value": 0.3935, "depth": 13}
													if obj[3]<=0:
														return 'False'
													elif obj[3]>0:
														return 'False'
													else: return 'False'
												else: return 'False'
											else: return 'False'
										elif obj[11]>0:
											# {"feature": "Passanger", "instances": 68, "metric_value": 0.383, "depth": 11}
											if obj[0]<=1:
												# {"feature": "Age", "instances": 58, "metric_value": 0.3577, "depth": 12}
												if obj[4]<=4:
													# {"feature": "Gender", "instances": 44, "metric_value": 0.3202, "depth": 13}
													if obj[3]>0:
														return 'False'
													elif obj[3]<=0:
														return 'False'
													else: return 'False'
												elif obj[4]>4:
													# {"feature": "Gender", "instances": 14, "metric_value": 0.4317, "depth": 13}
													if obj[3]<=0:
														return 'False'
													elif obj[3]>0:
														return 'False'
													else: return 'False'
												else: return 'False'
											elif obj[0]>1:
												# {"feature": "Gender", "instances": 10, "metric_value": 0.4, "depth": 12}
												if obj[3]<=0:
													# {"feature": "Age", "instances": 5, "metric_value": 0.4, "depth": 13}
													if obj[4]<=1:
														return 'True'
													elif obj[4]>1:
														return 'True'
													else: return 'True'
												elif obj[3]>0:
													# {"feature": "Age", "instances": 5, "metric_value": 0.2, "depth": 13}
													if obj[4]>0:
														return 'False'
													elif obj[4]<=0:
														return 'False'
													else: return 'False'
												else: return 'False'
											else: return 'False'
										else: return 'False'
									elif obj[6]>2:
										# {"feature": "Passanger", "instances": 85, "metric_value": 0.455, "depth": 10}
										if obj[0]<=2:
											# {"feature": "Direction_same", "instances": 73, "metric_value": 0.4729, "depth": 11}
											if obj[11]<=0:
												# {"feature": "Age", "instances": 50, "metric_value": 0.4387, "depth": 12}
												if obj[4]>2:
													# {"feature": "Gender", "instances": 32, "metric_value": 0.4023, "depth": 13}
													if obj[3]<=0:
														return 'False'
													elif obj[3]>0:
														return 'False'
													else: return 'False'
												elif obj[4]<=2:
													# {"feature": "Gender", "instances": 18, "metric_value": 0.4722, "depth": 13}
													if obj[3]>0:
														return 'False'
													elif obj[3]<=0:
														return 'True'
													else: return 'True'
												else: return 'True'
											elif obj[11]>0:
												# {"feature": "Gender", "instances": 23, "metric_value": 0.475, "depth": 12}
												if obj[3]<=0:
													# {"feature": "Age", "instances": 12, "metric_value": 0.375, "depth": 13}
													if obj[4]<=6:
														return 'False'
													elif obj[4]>6:
														return 'True'
													else: return 'True'
												elif obj[3]>0:
													# {"feature": "Age", "instances": 11, "metric_value": 0.2828, "depth": 13}
													if obj[4]<=3:
														return 'True'
													elif obj[4]>3:
														return 'False'
													else: return 'False'
												else: return 'True'
											else: return 'True'
										elif obj[0]>2:
											# {"feature": "Age", "instances": 12, "metric_value": 0.2593, "depth": 11}
											if obj[4]<=6:
												# {"feature": "Gender", "instances": 9, "metric_value": 0.1905, "depth": 12}
												if obj[3]>0:
													# {"feature": "Direction_same", "instances": 7, "metric_value": 0.2449, "depth": 13}
													if obj[11]<=0:
														return 'True'
													else: return 'True'
												elif obj[3]<=0:
													return 'True'
												else: return 'True'
											elif obj[4]>6:
												# {"feature": "Gender", "instances": 3, "metric_value": 0.4444, "depth": 12}
												if obj[3]<=0:
													# {"feature": "Direction_same", "instances": 3, "metric_value": 0.4444, "depth": 13}
													if obj[11]<=0:
														return 'True'
													else: return 'True'
												else: return 'True'
											else: return 'True'
										else: return 'True'
									else: return 'False'
								elif obj[10]>2.0:
									# {"feature": "Age", "instances": 25, "metric_value": 0.419, "depth": 9}
									if obj[4]<=4:
										# {"feature": "Education", "instances": 21, "metric_value": 0.4894, "depth": 10}
										if obj[6]<=3:
											# {"feature": "Gender", "instances": 12, "metric_value": 0.4167, "depth": 11}
											if obj[3]>0:
												# {"feature": "Passanger", "instances": 10, "metric_value": 0.4167, "depth": 12}
												if obj[0]<=1:
													# {"feature": "Direction_same", "instances": 6, "metric_value": 0.3333, "depth": 13}
													if obj[11]<=0:
														return 'False'
													elif obj[11]>0:
														return 'False'
													else: return 'False'
												elif obj[0]>1:
													# {"feature": "Direction_same", "instances": 4, "metric_value": 0.3333, "depth": 13}
													if obj[11]<=0:
														return 'True'
													elif obj[11]>0:
														return 'True'
													else: return 'True'
												else: return 'True'
											elif obj[3]<=0:
												return 'True'
											else: return 'True'
										elif obj[6]>3:
											# {"feature": "Passanger", "instances": 9, "metric_value": 0.4444, "depth": 11}
											if obj[0]>1:
												# {"feature": "Direction_same", "instances": 6, "metric_value": 0.2667, "depth": 12}
												if obj[11]<=0:
													# {"feature": "Gender", "instances": 5, "metric_value": 0.32, "depth": 13}
													if obj[3]<=0:
														return 'False'
													else: return 'False'
												elif obj[11]>0:
													return 'True'
												else: return 'True'
											elif obj[0]<=1:
												# {"feature": "Direction_same", "instances": 3, "metric_value": 0.3333, "depth": 12}
												if obj[11]>0:
													# {"feature": "Gender", "instances": 2, "metric_value": 0.5, "depth": 13}
													if obj[3]<=0:
														return 'True'
													else: return 'True'
												elif obj[11]<=0:
													return 'True'
												else: return 'True'
											else: return 'True'
										else: return 'False'
									elif obj[4]>4:
										return 'True'
									else: return 'True'
								else: return 'True'
							elif obj[12]>2:
								# {"feature": "Education", "instances": 95, "metric_value": 0.3455, "depth": 8}
								if obj[6]>0:
									# {"feature": "Passanger", "instances": 69, "metric_value": 0.2466, "depth": 9}
									if obj[0]<=1:
										# {"feature": "Restaurant20to50", "instances": 67, "metric_value": 0.2445, "depth": 10}
										if obj[10]<=1.0:
											# {"feature": "Age", "instances": 46, "metric_value": 0.3062, "depth": 11}
											if obj[4]>2:
												# {"feature": "Gender", "instances": 23, "metric_value": 0.3742, "depth": 12}
												if obj[3]>0:
													# {"feature": "Direction_same", "instances": 12, "metric_value": 0.4444, "depth": 13}
													if obj[11]<=0:
														return 'False'
													else: return 'False'
												elif obj[3]<=0:
													# {"feature": "Direction_same", "instances": 11, "metric_value": 0.2975, "depth": 13}
													if obj[11]<=0:
														return 'False'
													else: return 'False'
												else: return 'False'
											elif obj[4]<=2:
												# {"feature": "Gender", "instances": 23, "metric_value": 0.1897, "depth": 12}
												if obj[3]>0:
													return 'False'
												elif obj[3]<=0:
													# {"feature": "Direction_same", "instances": 11, "metric_value": 0.3967, "depth": 13}
													if obj[11]<=0:
														return 'False'
													else: return 'False'
												else: return 'False'
											else: return 'False'
										elif obj[10]>1.0:
											# {"feature": "Age", "instances": 21, "metric_value": 0.0847, "depth": 11}
											if obj[4]<=3:
												return 'False'
											elif obj[4]>3:
												# {"feature": "Gender", "instances": 9, "metric_value": 0.1778, "depth": 12}
												if obj[3]>0:
													# {"feature": "Direction_same", "instances": 5, "metric_value": 0.32, "depth": 13}
													if obj[11]<=0:
														return 'False'
													else: return 'False'
												elif obj[3]<=0:
													return 'False'
												else: return 'False'
											else: return 'False'
										else: return 'False'
									elif obj[0]>1:
										return 'True'
									else: return 'True'
								elif obj[6]<=0:
									# {"feature": "Gender", "instances": 26, "metric_value": 0.4242, "depth": 9}
									if obj[3]>0:
										# {"feature": "Age", "instances": 15, "metric_value": 0.3889, "depth": 10}
										if obj[4]<=4:
											# {"feature": "Restaurant20to50", "instances": 12, "metric_value": 0.4583, "depth": 11}
											if obj[10]<=1.0:
												# {"feature": "Passanger", "instances": 8, "metric_value": 0.5, "depth": 12}
												if obj[0]<=1:
													# {"feature": "Direction_same", "instances": 8, "metric_value": 0.5, "depth": 13}
													if obj[11]<=0:
														return 'True'
													else: return 'True'
												else: return 'True'
											elif obj[10]>1.0:
												# {"feature": "Passanger", "instances": 4, "metric_value": 0.375, "depth": 12}
												if obj[0]<=1:
													# {"feature": "Direction_same", "instances": 4, "metric_value": 0.375, "depth": 13}
													if obj[11]<=0:
														return 'True'
													else: return 'True'
												else: return 'True'
											else: return 'True'
										elif obj[4]>4:
											return 'True'
										else: return 'True'
									elif obj[3]<=0:
										# {"feature": "Restaurant20to50", "instances": 11, "metric_value": 0.2727, "depth": 10}
										if obj[10]<=1.0:
											# {"feature": "Age", "instances": 6, "metric_value": 0.4444, "depth": 11}
											if obj[4]>0:
												# {"feature": "Passanger", "instances": 3, "metric_value": 0.4444, "depth": 12}
												if obj[0]<=1:
													# {"feature": "Direction_same", "instances": 3, "metric_value": 0.4444, "depth": 13}
													if obj[11]<=0:
														return 'False'
													else: return 'False'
												else: return 'False'
											elif obj[4]<=0:
												# {"feature": "Passanger", "instances": 3, "metric_value": 0.4444, "depth": 12}
												if obj[0]<=1:
													# {"feature": "Direction_same", "instances": 3, "metric_value": 0.4444, "depth": 13}
													if obj[11]<=0:
														return 'True'
													else: return 'True'
												else: return 'True'
											else: return 'True'
										elif obj[10]>1.0:
											return 'False'
										else: return 'False'
									else: return 'False'
								else: return 'False'
							else: return 'False'
						elif obj[9]>2.0:
							# {"feature": "Direction_same", "instances": 118, "metric_value": 0.3094, "depth": 7}
							if obj[11]<=0:
								# {"feature": "Restaurant20to50", "instances": 86, "metric_value": 0.2449, "depth": 8}
								if obj[10]<=1.0:
									# {"feature": "Education", "instances": 65, "metric_value": 0.176, "depth": 9}
									if obj[6]>1:
										# {"feature": "Age", "instances": 44, "metric_value": 0.083, "depth": 10}
										if obj[4]>2:
											# {"feature": "Passanger", "instances": 23, "metric_value": 0.1491, "depth": 11}
											if obj[0]<=1:
												# {"feature": "Gender", "instances": 14, "metric_value": 0.2413, "depth": 12}
												if obj[3]>0:
													# {"feature": "Distance", "instances": 9, "metric_value": 0.1852, "depth": 13}
													if obj[12]<=2:
														return 'False'
													elif obj[12]>2:
														return 'False'
													else: return 'False'
												elif obj[3]<=0:
													# {"feature": "Distance", "instances": 5, "metric_value": 0.2, "depth": 13}
													if obj[12]<=2:
														return 'False'
													elif obj[12]>2:
														return 'False'
													else: return 'False'
												else: return 'False'
											elif obj[0]>1:
												return 'False'
											else: return 'False'
										elif obj[4]<=2:
											return 'False'
										else: return 'False'
									elif obj[6]<=1:
										# {"feature": "Age", "instances": 21, "metric_value": 0.3175, "depth": 10}
										if obj[4]<=2:
											# {"feature": "Distance", "instances": 15, "metric_value": 0.381, "depth": 11}
											if obj[12]>1:
												# {"feature": "Passanger", "instances": 14, "metric_value": 0.3429, "depth": 12}
												if obj[0]<=1:
													# {"feature": "Gender", "instances": 10, "metric_value": 0.4667, "depth": 13}
													if obj[3]<=0:
														return 'False'
													elif obj[3]>0:
														return 'True'
													else: return 'True'
												elif obj[0]>1:
													return 'False'
												else: return 'False'
											elif obj[12]<=1:
												return 'True'
											else: return 'True'
										elif obj[4]>2:
											return 'False'
										else: return 'False'
									else: return 'False'
								elif obj[10]>1.0:
									# {"feature": "Passanger", "instances": 21, "metric_value": 0.3464, "depth": 9}
									if obj[0]<=2:
										# {"feature": "Age", "instances": 16, "metric_value": 0.2396, "depth": 10}
										if obj[4]>2:
											# {"feature": "Education", "instances": 12, "metric_value": 0.1458, "depth": 11}
											if obj[6]>0:
												# {"feature": "Distance", "instances": 8, "metric_value": 0.2, "depth": 12}
												if obj[12]<=2:
													# {"feature": "Gender", "instances": 5, "metric_value": 0.32, "depth": 13}
													if obj[3]<=1:
														return 'False'
													else: return 'False'
												elif obj[12]>2:
													return 'False'
												else: return 'False'
											elif obj[6]<=0:
												return 'False'
											else: return 'False'
										elif obj[4]<=2:
											# {"feature": "Distance", "instances": 4, "metric_value": 0.3333, "depth": 11}
											if obj[12]<=2:
												# {"feature": "Gender", "instances": 3, "metric_value": 0.4444, "depth": 12}
												if obj[3]<=1:
													# {"feature": "Education", "instances": 3, "metric_value": 0.4444, "depth": 13}
													if obj[6]<=2:
														return 'False'
													else: return 'False'
												else: return 'False'
											elif obj[12]>2:
												return 'True'
											else: return 'True'
										else: return 'True'
									elif obj[0]>2:
										# {"feature": "Age", "instances": 5, "metric_value": 0.2667, "depth": 10}
										if obj[4]<=2:
											# {"feature": "Gender", "instances": 3, "metric_value": 0.4444, "depth": 11}
											if obj[3]<=1:
												# {"feature": "Education", "instances": 3, "metric_value": 0.4444, "depth": 12}
												if obj[6]<=2:
													# {"feature": "Distance", "instances": 3, "metric_value": 0.4444, "depth": 13}
													if obj[12]<=2:
														return 'False'
													else: return 'False'
												else: return 'False'
											else: return 'False'
										elif obj[4]>2:
											return 'True'
										else: return 'True'
									else: return 'True'
								else: return 'False'
							elif obj[11]>0:
								# {"feature": "Age", "instances": 32, "metric_value": 0.3842, "depth": 8}
								if obj[4]>2:
									# {"feature": "Distance", "instances": 21, "metric_value": 0.4222, "depth": 9}
									if obj[12]<=1:
										# {"feature": "Restaurant20to50", "instances": 15, "metric_value": 0.4308, "depth": 10}
										if obj[10]<=2.0:
											# {"feature": "Education", "instances": 13, "metric_value": 0.4249, "depth": 11}
											if obj[6]>2:
												# {"feature": "Gender", "instances": 7, "metric_value": 0.381, "depth": 12}
												if obj[3]>0:
													# {"feature": "Passanger", "instances": 6, "metric_value": 0.4444, "depth": 13}
													if obj[0]<=1:
														return 'True'
													else: return 'True'
												elif obj[3]<=0:
													return 'True'
												else: return 'True'
											elif obj[6]<=2:
												# {"feature": "Passanger", "instances": 6, "metric_value": 0.4444, "depth": 12}
												if obj[0]<=1:
													# {"feature": "Gender", "instances": 6, "metric_value": 0.4444, "depth": 13}
													if obj[3]<=1:
														return 'False'
													else: return 'False'
												else: return 'False'
											else: return 'False'
										elif obj[10]>2.0:
											return 'True'
										else: return 'True'
									elif obj[12]>1:
										# {"feature": "Passanger", "instances": 6, "metric_value": 0.2222, "depth": 10}
										if obj[0]>1:
											return 'False'
										elif obj[0]<=1:
											# {"feature": "Education", "instances": 3, "metric_value": 0.3333, "depth": 11}
											if obj[6]>0:
												# {"feature": "Restaurant20to50", "instances": 2, "metric_value": 0.0, "depth": 12}
												if obj[10]<=1.0:
													return 'True'
												elif obj[10]>1.0:
													return 'False'
												else: return 'False'
											elif obj[6]<=0:
												return 'False'
											else: return 'False'
										else: return 'False'
									else: return 'False'
								elif obj[4]<=2:
									# {"feature": "Passanger", "instances": 11, "metric_value": 0.1212, "depth": 9}
									if obj[0]<=1:
										return 'False'
									elif obj[0]>1:
										# {"feature": "Education", "instances": 3, "metric_value": 0.0, "depth": 10}
										if obj[6]>1:
											return 'False'
										elif obj[6]<=1:
											return 'True'
										else: return 'True'
									else: return 'False'
								else: return 'False'
							else: return 'False'
						else: return 'False'
					elif obj[1]>3:
						# {"feature": "Passanger", "instances": 80, "metric_value": 0.2039, "depth": 6}
						if obj[0]<=2:
							# {"feature": "Distance", "instances": 76, "metric_value": 0.1805, "depth": 7}
							if obj[12]>1:
								# {"feature": "Gender", "instances": 50, "metric_value": 0.1036, "depth": 8}
								if obj[3]>0:
									return 'False'
								elif obj[3]<=0:
									# {"feature": "Age", "instances": 22, "metric_value": 0.2143, "depth": 9}
									if obj[4]>0:
										# {"feature": "Restaurant20to50", "instances": 14, "metric_value": 0.2984, "depth": 10}
										if obj[10]>1.0:
											# {"feature": "Education", "instances": 9, "metric_value": 0.1778, "depth": 11}
											if obj[6]>1:
												# {"feature": "Coffeehouse", "instances": 5, "metric_value": 0.2, "depth": 12}
												if obj[9]<=1.0:
													return 'False'
												elif obj[9]>1.0:
													# {"feature": "Direction_same", "instances": 2, "metric_value": 0.5, "depth": 13}
													if obj[11]<=0:
														return 'False'
													else: return 'False'
												else: return 'False'
											elif obj[6]<=1:
												return 'False'
											else: return 'False'
										elif obj[10]<=1.0:
											# {"feature": "Coffeehouse", "instances": 5, "metric_value": 0.2667, "depth": 11}
											if obj[9]>0.0:
												# {"feature": "Education", "instances": 3, "metric_value": 0.0, "depth": 12}
												if obj[6]<=2:
													return 'True'
												elif obj[6]>2:
													return 'False'
												else: return 'False'
											elif obj[9]<=0.0:
												return 'False'
											else: return 'False'
										else: return 'False'
									elif obj[4]<=0:
										return 'False'
									else: return 'False'
								else: return 'False'
							elif obj[12]<=1:
								# {"feature": "Age", "instances": 26, "metric_value": 0.284, "depth": 8}
								if obj[4]>2:
									# {"feature": "Coffeehouse", "instances": 13, "metric_value": 0.4103, "depth": 9}
									if obj[9]<=3.0:
										# {"feature": "Restaurant20to50", "instances": 12, "metric_value": 0.4167, "depth": 10}
										if obj[10]<=1.0:
											# {"feature": "Gender", "instances": 8, "metric_value": 0.3333, "depth": 11}
											if obj[3]>0:
												# {"feature": "Education", "instances": 6, "metric_value": 0.4167, "depth": 12}
												if obj[6]<=0:
													# {"feature": "Direction_same", "instances": 4, "metric_value": 0.375, "depth": 13}
													if obj[11]<=0:
														return 'False'
													else: return 'False'
												elif obj[6]>0:
													# {"feature": "Direction_same", "instances": 2, "metric_value": 0.5, "depth": 13}
													if obj[11]<=0:
														return 'True'
													else: return 'True'
												else: return 'True'
											elif obj[3]<=0:
												return 'False'
											else: return 'False'
										elif obj[10]>1.0:
											# {"feature": "Gender", "instances": 4, "metric_value": 0.5, "depth": 11}
											if obj[3]<=0:
												# {"feature": "Education", "instances": 4, "metric_value": 0.5, "depth": 12}
												if obj[6]>0:
													# {"feature": "Direction_same", "instances": 2, "metric_value": 0.5, "depth": 13}
													if obj[11]<=0:
														return 'True'
													else: return 'True'
												elif obj[6]<=0:
													# {"feature": "Direction_same", "instances": 2, "metric_value": 0.5, "depth": 13}
													if obj[11]<=0:
														return 'False'
													else: return 'False'
												else: return 'False'
											else: return 'True'
										else: return 'True'
									elif obj[9]>3.0:
										return 'False'
									else: return 'False'
								elif obj[4]<=2:
									# {"feature": "Coffeehouse", "instances": 13, "metric_value": 0.1026, "depth": 9}
									if obj[9]<=2.0:
										return 'False'
									elif obj[9]>2.0:
										# {"feature": "Education", "instances": 3, "metric_value": 0.3333, "depth": 10}
										if obj[6]>0:
											# {"feature": "Gender", "instances": 2, "metric_value": 0.5, "depth": 11}
											if obj[3]<=0:
												# {"feature": "Restaurant20to50", "instances": 2, "metric_value": 0.5, "depth": 12}
												if obj[10]<=1.0:
													# {"feature": "Direction_same", "instances": 2, "metric_value": 0.5, "depth": 13}
													if obj[11]<=0:
														return 'False'
													else: return 'False'
												else: return 'False'
											else: return 'False'
										elif obj[6]<=0:
											return 'False'
										else: return 'False'
									else: return 'False'
								else: return 'False'
							else: return 'False'
						elif obj[0]>2:
							# {"feature": "Age", "instances": 4, "metric_value": 0.0, "depth": 7}
							if obj[4]>3:
								return 'False'
							elif obj[4]<=3:
								return 'True'
							else: return 'True'
						else: return 'False'
					else: return 'False'
				elif obj[7]<=1.5424315569353801:
					# {"feature": "Age", "instances": 159, "metric_value": 0.2582, "depth": 5}
					if obj[4]<=6:
						# {"feature": "Restaurant20to50", "instances": 152, "metric_value": 0.2379, "depth": 6}
						if obj[10]<=2.0:
							# {"feature": "Direction_same", "instances": 151, "metric_value": 0.2335, "depth": 7}
							if obj[11]<=0:
								# {"feature": "Education", "instances": 118, "metric_value": 0.1898, "depth": 8}
								if obj[6]>0:
									# {"feature": "Time", "instances": 66, "metric_value": 0.11, "depth": 9}
									if obj[1]>1:
										# {"feature": "Coffeehouse", "instances": 40, "metric_value": 0.0467, "depth": 10}
										if obj[9]<=1.0:
											return 'False'
										elif obj[9]>1.0:
											# {"feature": "Passanger", "instances": 15, "metric_value": 0.1143, "depth": 11}
											if obj[0]<=1:
												return 'False'
											elif obj[0]>1:
												# {"feature": "Gender", "instances": 7, "metric_value": 0.2449, "depth": 12}
												if obj[3]<=1:
													# {"feature": "Distance", "instances": 7, "metric_value": 0.2449, "depth": 13}
													if obj[12]<=2:
														return 'False'
													else: return 'False'
												else: return 'False'
											else: return 'False'
										else: return 'False'
									elif obj[1]<=1:
										# {"feature": "Passanger", "instances": 26, "metric_value": 0.1828, "depth": 10}
										if obj[0]<=1:
											# {"feature": "Coffeehouse", "instances": 19, "metric_value": 0.0936, "depth": 11}
											if obj[9]>1.0:
												return 'False'
											elif obj[9]<=1.0:
												# {"feature": "Distance", "instances": 9, "metric_value": 0.1852, "depth": 12}
												if obj[12]>2:
													# {"feature": "Gender", "instances": 6, "metric_value": 0.2667, "depth": 13}
													if obj[3]>0:
														return 'False'
													elif obj[3]<=0:
														return 'False'
													else: return 'False'
												elif obj[12]<=2:
													return 'False'
												else: return 'False'
											else: return 'False'
										elif obj[0]>1:
											# {"feature": "Distance", "instances": 7, "metric_value": 0.2381, "depth": 11}
											if obj[12]<=2:
												# {"feature": "Coffeehouse", "instances": 6, "metric_value": 0.2222, "depth": 12}
												if obj[9]>1.0:
													return 'False'
												elif obj[9]<=1.0:
													# {"feature": "Gender", "instances": 3, "metric_value": 0.3333, "depth": 13}
													if obj[3]>0:
														return 'True'
													elif obj[3]<=0:
														return 'False'
													else: return 'False'
												else: return 'False'
											elif obj[12]>2:
												return 'True'
											else: return 'True'
										else: return 'False'
									else: return 'False'
								elif obj[6]<=0:
									# {"feature": "Coffeehouse", "instances": 52, "metric_value": 0.2564, "depth": 9}
									if obj[9]<=1.0:
										# {"feature": "Distance", "instances": 39, "metric_value": 0.1736, "depth": 10}
										if obj[12]<=2:
											# {"feature": "Passanger", "instances": 26, "metric_value": 0.2337, "depth": 11}
											if obj[0]>1:
												# {"feature": "Gender", "instances": 16, "metric_value": 0.0938, "depth": 12}
												if obj[3]>0:
													return 'False'
												elif obj[3]<=0:
													# {"feature": "Time", "instances": 4, "metric_value": 0.25, "depth": 13}
													if obj[1]<=2:
														return 'False'
													elif obj[1]>2:
														return 'True'
													else: return 'True'
												else: return 'False'
											elif obj[0]<=1:
												# {"feature": "Time", "instances": 10, "metric_value": 0.3048, "depth": 12}
												if obj[1]>0:
													# {"feature": "Gender", "instances": 7, "metric_value": 0.2449, "depth": 13}
													if obj[3]<=1:
														return 'False'
													else: return 'False'
												elif obj[1]<=0:
													# {"feature": "Gender", "instances": 3, "metric_value": 0.4444, "depth": 13}
													if obj[3]<=1:
														return 'True'
													else: return 'True'
												else: return 'True'
											else: return 'False'
										elif obj[12]>2:
											return 'False'
										else: return 'False'
									elif obj[9]>1.0:
										# {"feature": "Distance", "instances": 13, "metric_value": 0.3846, "depth": 10}
										if obj[12]<=2:
											# {"feature": "Passanger", "instances": 10, "metric_value": 0.4167, "depth": 11}
											if obj[0]>1:
												# {"feature": "Time", "instances": 6, "metric_value": 0.2222, "depth": 12}
												if obj[1]>2:
													return 'False'
												elif obj[1]<=2:
													# {"feature": "Gender", "instances": 3, "metric_value": 0.4444, "depth": 13}
													if obj[3]<=1:
														return 'True'
													else: return 'True'
												else: return 'True'
											elif obj[0]<=1:
												# {"feature": "Time", "instances": 4, "metric_value": 0.25, "depth": 12}
												if obj[1]<=1:
													return 'True'
												elif obj[1]>1:
													# {"feature": "Gender", "instances": 2, "metric_value": 0.5, "depth": 13}
													if obj[3]<=1:
														return 'True'
													else: return 'True'
												else: return 'True'
											else: return 'True'
										elif obj[12]>2:
											return 'False'
										else: return 'False'
									else: return 'False'
								else: return 'False'
							elif obj[11]>0:
								# {"feature": "Time", "instances": 33, "metric_value": 0.3216, "depth": 8}
								if obj[1]<=1:
									# {"feature": "Education", "instances": 28, "metric_value": 0.2434, "depth": 9}
									if obj[6]<=2:
										# {"feature": "Coffeehouse", "instances": 27, "metric_value": 0.2438, "depth": 10}
										if obj[9]<=2.0:
											# {"feature": "Distance", "instances": 24, "metric_value": 0.2125, "depth": 11}
											if obj[12]<=1:
												# {"feature": "Gender", "instances": 20, "metric_value": 0.2526, "depth": 12}
												if obj[3]>0:
													# {"feature": "Passanger", "instances": 19, "metric_value": 0.2659, "depth": 13}
													if obj[0]<=1:
														return 'False'
													else: return 'False'
												elif obj[3]<=0:
													return 'False'
												else: return 'False'
											elif obj[12]>1:
												return 'False'
											else: return 'False'
										elif obj[9]>2.0:
											# {"feature": "Passanger", "instances": 3, "metric_value": 0.3333, "depth": 11}
											if obj[0]<=1:
												# {"feature": "Gender", "instances": 2, "metric_value": 0.5, "depth": 12}
												if obj[3]<=1:
													# {"feature": "Distance", "instances": 2, "metric_value": 0.5, "depth": 13}
													if obj[12]<=2:
														return 'True'
													else: return 'True'
												else: return 'True'
											elif obj[0]>1:
												return 'False'
											else: return 'False'
										else: return 'False'
									elif obj[6]>2:
										return 'True'
									else: return 'True'
								elif obj[1]>1:
									# {"feature": "Education", "instances": 5, "metric_value": 0.3, "depth": 9}
									if obj[6]>0:
										# {"feature": "Coffeehouse", "instances": 4, "metric_value": 0.3333, "depth": 10}
										if obj[9]<=1.0:
											# {"feature": "Passanger", "instances": 3, "metric_value": 0.4444, "depth": 11}
											if obj[0]<=2:
												# {"feature": "Gender", "instances": 3, "metric_value": 0.4444, "depth": 12}
												if obj[3]<=1:
													# {"feature": "Distance", "instances": 3, "metric_value": 0.4444, "depth": 13}
													if obj[12]<=2:
														return 'True'
													else: return 'True'
												else: return 'True'
											else: return 'True'
										elif obj[9]>1.0:
											return 'True'
										else: return 'True'
									elif obj[6]<=0:
										return 'False'
									else: return 'False'
								else: return 'True'
							else: return 'False'
						elif obj[10]>2.0:
							return 'True'
						else: return 'True'
					elif obj[4]>6:
						# {"feature": "Distance", "instances": 7, "metric_value": 0.3429, "depth": 6}
						if obj[12]<=2:
							# {"feature": "Passanger", "instances": 5, "metric_value": 0.4, "depth": 7}
							if obj[0]<=1:
								# {"feature": "Time", "instances": 4, "metric_value": 0.3333, "depth": 8}
								if obj[1]>0:
									# {"feature": "Gender", "instances": 3, "metric_value": 0.4444, "depth": 9}
									if obj[3]<=1:
										# {"feature": "Education", "instances": 3, "metric_value": 0.4444, "depth": 10}
										if obj[6]<=5:
											# {"feature": "Coffeehouse", "instances": 3, "metric_value": 0.4444, "depth": 11}
											if obj[9]<=0.0:
												# {"feature": "Restaurant20to50", "instances": 3, "metric_value": 0.4444, "depth": 12}
												if obj[10]<=0.0:
													# {"feature": "Direction_same", "instances": 3, "metric_value": 0.4444, "depth": 13}
													if obj[11]<=0:
														return 'True'
													else: return 'True'
												else: return 'True'
											else: return 'True'
										else: return 'True'
									else: return 'True'
								elif obj[1]<=0:
									return 'False'
								else: return 'False'
							elif obj[0]>1:
								return 'False'
							else: return 'False'
						elif obj[12]>2:
							return 'True'
						else: return 'True'
					else: return 'True'
				else: return 'False'
			elif obj[5]<=0:
				# {"feature": "Restaurant20to50", "instances": 797, "metric_value": 0.4734, "depth": 4}
				if obj[10]<=1.0:
					# {"feature": "Education", "instances": 590, "metric_value": 0.4585, "depth": 5}
					if obj[6]<=1:
						# {"feature": "Age", "instances": 296, "metric_value": 0.4757, "depth": 6}
						if obj[4]>2:
							# {"feature": "Occupation", "instances": 192, "metric_value": 0.4847, "depth": 7}
							if obj[7]>0:
								# {"feature": "Gender", "instances": 184, "metric_value": 0.4827, "depth": 8}
								if obj[3]<=0:
									# {"feature": "Coffeehouse", "instances": 125, "metric_value": 0.4625, "depth": 9}
									if obj[9]<=2.0:
										# {"feature": "Passanger", "instances": 95, "metric_value": 0.4844, "depth": 10}
										if obj[0]>0:
											# {"feature": "Distance", "instances": 86, "metric_value": 0.4949, "depth": 11}
											if obj[12]>1:
												# {"feature": "Time", "instances": 57, "metric_value": 0.4881, "depth": 12}
												if obj[1]<=2:
													# {"feature": "Direction_same", "instances": 43, "metric_value": 0.4974, "depth": 13}
													if obj[11]<=0:
														return 'False'
													elif obj[11]>0:
														return 'False'
													else: return 'False'
												elif obj[1]>2:
													# {"feature": "Direction_same", "instances": 14, "metric_value": 0.4589, "depth": 13}
													if obj[11]<=0:
														return 'True'
													elif obj[11]>0:
														return 'True'
													else: return 'True'
												else: return 'True'
											elif obj[12]<=1:
												# {"feature": "Time", "instances": 29, "metric_value": 0.4713, "depth": 12}
												if obj[1]>1:
													# {"feature": "Direction_same", "instances": 15, "metric_value": 0.4444, "depth": 13}
													if obj[11]<=0:
														return 'False'
													else: return 'False'
												elif obj[1]<=1:
													# {"feature": "Direction_same", "instances": 14, "metric_value": 0.5, "depth": 13}
													if obj[11]<=1:
														return 'True'
													else: return 'True'
												else: return 'True'
											else: return 'False'
										elif obj[0]<=0:
											# {"feature": "Time", "instances": 9, "metric_value": 0.2667, "depth": 11}
											if obj[1]<=2:
												# {"feature": "Distance", "instances": 5, "metric_value": 0.4667, "depth": 12}
												if obj[12]>1:
													# {"feature": "Direction_same", "instances": 3, "metric_value": 0.4444, "depth": 13}
													if obj[11]<=0:
														return 'False'
													else: return 'False'
												elif obj[12]<=1:
													# {"feature": "Direction_same", "instances": 2, "metric_value": 0.5, "depth": 13}
													if obj[11]<=0:
														return 'False'
													else: return 'False'
												else: return 'False'
											elif obj[1]>2:
												return 'False'
											else: return 'False'
										else: return 'False'
									elif obj[9]>2.0:
										# {"feature": "Passanger", "instances": 30, "metric_value": 0.35, "depth": 10}
										if obj[0]>0:
											# {"feature": "Time", "instances": 28, "metric_value": 0.3673, "depth": 11}
											if obj[1]<=3:
												# {"feature": "Distance", "instances": 21, "metric_value": 0.3968, "depth": 12}
												if obj[12]>1:
													# {"feature": "Direction_same", "instances": 15, "metric_value": 0.381, "depth": 13}
													if obj[11]<=0:
														return 'False'
													elif obj[11]>0:
														return 'True'
													else: return 'True'
												elif obj[12]<=1:
													# {"feature": "Direction_same", "instances": 6, "metric_value": 0.2667, "depth": 13}
													if obj[11]>0:
														return 'False'
													elif obj[11]<=0:
														return 'False'
													else: return 'False'
												else: return 'False'
											elif obj[1]>3:
												# {"feature": "Distance", "instances": 7, "metric_value": 0.2286, "depth": 12}
												if obj[12]<=1:
													# {"feature": "Direction_same", "instances": 5, "metric_value": 0.32, "depth": 13}
													if obj[11]<=0:
														return 'False'
													else: return 'False'
												elif obj[12]>1:
													return 'False'
												else: return 'False'
											else: return 'False'
										elif obj[0]<=0:
											return 'False'
										else: return 'False'
									else: return 'False'
								elif obj[3]>0:
									# {"feature": "Time", "instances": 59, "metric_value": 0.4309, "depth": 9}
									if obj[1]>0:
										# {"feature": "Passanger", "instances": 44, "metric_value": 0.4893, "depth": 10}
										if obj[0]<=1:
											# {"feature": "Distance", "instances": 36, "metric_value": 0.4715, "depth": 11}
											if obj[12]>1:
												# {"feature": "Coffeehouse", "instances": 20, "metric_value": 0.4357, "depth": 12}
												if obj[9]<=2.0:
													# {"feature": "Direction_same", "instances": 14, "metric_value": 0.3929, "depth": 13}
													if obj[11]<=0:
														return 'False'
													elif obj[11]>0:
														return 'True'
													else: return 'True'
												elif obj[9]>2.0:
													# {"feature": "Direction_same", "instances": 6, "metric_value": 0.4, "depth": 13}
													if obj[11]<=0:
														return 'True'
													elif obj[11]>0:
														return 'False'
													else: return 'False'
												else: return 'True'
											elif obj[12]<=1:
												# {"feature": "Coffeehouse", "instances": 16, "metric_value": 0.4643, "depth": 12}
												if obj[9]>1.0:
													# {"feature": "Direction_same", "instances": 9, "metric_value": 0.4444, "depth": 13}
													if obj[11]<=0:
														return 'True'
													else: return 'True'
												elif obj[9]<=1.0:
													# {"feature": "Direction_same", "instances": 7, "metric_value": 0.381, "depth": 13}
													if obj[11]<=0:
														return 'False'
													elif obj[11]>0:
														return 'True'
													else: return 'True'
												else: return 'False'
											else: return 'True'
										elif obj[0]>1:
											# {"feature": "Coffeehouse", "instances": 8, "metric_value": 0.3571, "depth": 11}
											if obj[9]<=2.0:
												# {"feature": "Distance", "instances": 7, "metric_value": 0.3714, "depth": 12}
												if obj[12]>1:
													# {"feature": "Direction_same", "instances": 5, "metric_value": 0.32, "depth": 13}
													if obj[11]<=0:
														return 'True'
													else: return 'True'
												elif obj[12]<=1:
													# {"feature": "Direction_same", "instances": 2, "metric_value": 0.5, "depth": 13}
													if obj[11]<=0:
														return 'True'
													else: return 'True'
												else: return 'True'
											elif obj[9]>2.0:
												return 'False'
											else: return 'False'
										else: return 'True'
									elif obj[1]<=0:
										# {"feature": "Distance", "instances": 15, "metric_value": 0.1897, "depth": 10}
										if obj[12]<=2:
											# {"feature": "Coffeehouse", "instances": 13, "metric_value": 0.1319, "depth": 11}
											if obj[9]>1.0:
												# {"feature": "Direction_same", "instances": 7, "metric_value": 0.2143, "depth": 12}
												if obj[11]<=0:
													# {"feature": "Passanger", "instances": 4, "metric_value": 0.25, "depth": 13}
													if obj[0]<=0:
														return 'True'
													elif obj[0]>0:
														return 'False'
													else: return 'False'
												elif obj[11]>0:
													return 'True'
												else: return 'True'
											elif obj[9]<=1.0:
												return 'True'
											else: return 'True'
										elif obj[12]>2:
											# {"feature": "Coffeehouse", "instances": 2, "metric_value": 0.0, "depth": 11}
											if obj[9]>2.0:
												return 'False'
											elif obj[9]<=2.0:
												return 'True'
											else: return 'True'
										else: return 'False'
									else: return 'True'
								else: return 'True'
							elif obj[7]<=0:
								# {"feature": "Direction_same", "instances": 8, "metric_value": 0.0, "depth": 8}
								if obj[11]<=0:
									return 'True'
								elif obj[11]>0:
									return 'False'
								else: return 'False'
							else: return 'True'
						elif obj[4]<=2:
							# {"feature": "Passanger", "instances": 104, "metric_value": 0.36, "depth": 7}
							if obj[0]>0:
								# {"feature": "Distance", "instances": 80, "metric_value": 0.3195, "depth": 8}
								if obj[12]>1:
									# {"feature": "Time", "instances": 50, "metric_value": 0.3572, "depth": 9}
									if obj[1]<=1:
										# {"feature": "Gender", "instances": 31, "metric_value": 0.233, "depth": 10}
										if obj[3]>0:
											# {"feature": "Occupation", "instances": 18, "metric_value": 0.3639, "depth": 11}
											if obj[7]<=6:
												# {"feature": "Direction_same", "instances": 10, "metric_value": 0.4, "depth": 12}
												if obj[11]<=0:
													# {"feature": "Coffeehouse", "instances": 9, "metric_value": 0.4444, "depth": 13}
													if obj[9]<=1.0:
														return 'False'
													else: return 'False'
												elif obj[11]>0:
													return 'True'
												else: return 'True'
											elif obj[7]>6:
												# {"feature": "Coffeehouse", "instances": 8, "metric_value": 0.125, "depth": 12}
												if obj[9]<=1.0:
													return 'False'
												elif obj[9]>1.0:
													# {"feature": "Direction_same", "instances": 2, "metric_value": 0.5, "depth": 13}
													if obj[11]<=0:
														return 'True'
													else: return 'True'
												else: return 'True'
											else: return 'False'
										elif obj[3]<=0:
											return 'False'
										else: return 'False'
									elif obj[1]>1:
										# {"feature": "Occupation", "instances": 19, "metric_value": 0.3947, "depth": 10}
										if obj[7]>1:
											# {"feature": "Gender", "instances": 16, "metric_value": 0.4409, "depth": 11}
											if obj[3]>0:
												# {"feature": "Coffeehouse", "instances": 11, "metric_value": 0.4364, "depth": 12}
												if obj[9]>0.0:
													# {"feature": "Direction_same", "instances": 10, "metric_value": 0.48, "depth": 13}
													if obj[11]<=0:
														return 'False'
													else: return 'False'
												elif obj[9]<=0.0:
													return 'True'
												else: return 'True'
											elif obj[3]<=0:
												# {"feature": "Coffeehouse", "instances": 5, "metric_value": 0.2667, "depth": 12}
												if obj[9]>0.0:
													# {"feature": "Direction_same", "instances": 3, "metric_value": 0.4444, "depth": 13}
													if obj[11]<=0:
														return 'False'
													else: return 'False'
												elif obj[9]<=0.0:
													return 'False'
												else: return 'False'
											else: return 'False'
										elif obj[7]<=1:
											return 'True'
										else: return 'True'
									else: return 'False'
								elif obj[12]<=1:
									# {"feature": "Occupation", "instances": 30, "metric_value": 0.17, "depth": 9}
									if obj[7]>1:
										# {"feature": "Time", "instances": 20, "metric_value": 0.09, "depth": 10}
										if obj[1]>0:
											return 'False'
										elif obj[1]<=0:
											# {"feature": "Gender", "instances": 10, "metric_value": 0.175, "depth": 11}
											if obj[3]>0:
												# {"feature": "Coffeehouse", "instances": 8, "metric_value": 0.2188, "depth": 12}
												if obj[9]<=1.0:
													# {"feature": "Direction_same", "instances": 8, "metric_value": 0.2188, "depth": 13}
													if obj[11]<=1:
														return 'False'
													else: return 'False'
												else: return 'False'
											elif obj[3]<=0:
												return 'False'
											else: return 'False'
										else: return 'False'
									elif obj[7]<=1:
										# {"feature": "Coffeehouse", "instances": 10, "metric_value": 0.2857, "depth": 10}
										if obj[9]>0.0:
											# {"feature": "Time", "instances": 7, "metric_value": 0.3714, "depth": 11}
											if obj[1]>0:
												# {"feature": "Direction_same", "instances": 5, "metric_value": 0.3, "depth": 12}
												if obj[11]<=0:
													# {"feature": "Gender", "instances": 4, "metric_value": 0.375, "depth": 13}
													if obj[3]<=0:
														return 'False'
													else: return 'False'
												elif obj[11]>0:
													return 'False'
												else: return 'False'
											elif obj[1]<=0:
												# {"feature": "Gender", "instances": 2, "metric_value": 0.5, "depth": 12}
												if obj[3]<=0:
													# {"feature": "Direction_same", "instances": 2, "metric_value": 0.5, "depth": 13}
													if obj[11]<=1:
														return 'False'
													else: return 'False'
												else: return 'False'
											else: return 'False'
										elif obj[9]<=0.0:
											return 'False'
										else: return 'False'
									else: return 'False'
								else: return 'False'
							elif obj[0]<=0:
								# {"feature": "Occupation", "instances": 24, "metric_value": 0.3175, "depth": 8}
								if obj[7]>1:
									# {"feature": "Coffeehouse", "instances": 21, "metric_value": 0.3439, "depth": 9}
									if obj[9]>-1.0:
										# {"feature": "Distance", "instances": 18, "metric_value": 0.3861, "depth": 10}
										if obj[12]>1:
											# {"feature": "Time", "instances": 10, "metric_value": 0.2857, "depth": 11}
											if obj[1]<=3:
												# {"feature": "Gender", "instances": 7, "metric_value": 0.381, "depth": 12}
												if obj[3]>0:
													# {"feature": "Direction_same", "instances": 6, "metric_value": 0.4444, "depth": 13}
													if obj[11]<=0:
														return 'True'
													else: return 'True'
												elif obj[3]<=0:
													return 'True'
												else: return 'True'
											elif obj[1]>3:
												return 'True'
											else: return 'True'
										elif obj[12]<=1:
											# {"feature": "Time", "instances": 8, "metric_value": 0.4375, "depth": 11}
											if obj[1]>2:
												# {"feature": "Gender", "instances": 4, "metric_value": 0.5, "depth": 12}
												if obj[3]<=1:
													# {"feature": "Direction_same", "instances": 4, "metric_value": 0.5, "depth": 13}
													if obj[11]<=0:
														return 'False'
													else: return 'False'
												else: return 'False'
											elif obj[1]<=2:
												# {"feature": "Gender", "instances": 4, "metric_value": 0.25, "depth": 12}
												if obj[3]<=0:
													# {"feature": "Direction_same", "instances": 2, "metric_value": 0.5, "depth": 13}
													if obj[11]<=0:
														return 'False'
													else: return 'False'
												elif obj[3]>0:
													return 'True'
												else: return 'True'
											else: return 'True'
										else: return 'True'
									elif obj[9]<=-1.0:
										return 'True'
									else: return 'True'
								elif obj[7]<=1:
									return 'False'
								else: return 'False'
							else: return 'True'
						else: return 'False'
					elif obj[6]>1:
						# {"feature": "Gender", "instances": 294, "metric_value": 0.4196, "depth": 6}
						if obj[3]>0:
							# {"feature": "Distance", "instances": 149, "metric_value": 0.3531, "depth": 7}
							if obj[12]<=2:
								# {"feature": "Occupation", "instances": 121, "metric_value": 0.3842, "depth": 8}
								if obj[7]>1:
									# {"feature": "Time", "instances": 92, "metric_value": 0.4354, "depth": 9}
									if obj[1]>0:
										# {"feature": "Age", "instances": 63, "metric_value": 0.3917, "depth": 10}
										if obj[4]<=6:
											# {"feature": "Coffeehouse", "instances": 62, "metric_value": 0.3867, "depth": 11}
											if obj[9]<=1.0:
												# {"feature": "Passanger", "instances": 34, "metric_value": 0.32, "depth": 12}
												if obj[0]>0:
													# {"feature": "Direction_same", "instances": 28, "metric_value": 0.2911, "depth": 13}
													if obj[11]<=0:
														return 'False'
													elif obj[11]>0:
														return 'False'
													else: return 'False'
												elif obj[0]<=0:
													# {"feature": "Direction_same", "instances": 6, "metric_value": 0.4444, "depth": 13}
													if obj[11]<=0:
														return 'False'
													else: return 'False'
												else: return 'False'
											elif obj[9]>1.0:
												# {"feature": "Direction_same", "instances": 28, "metric_value": 0.4497, "depth": 12}
												if obj[11]<=0:
													# {"feature": "Passanger", "instances": 27, "metric_value": 0.463, "depth": 13}
													if obj[0]>0:
														return 'False'
													elif obj[0]<=0:
														return 'False'
													else: return 'False'
												elif obj[11]>0:
													return 'False'
												else: return 'False'
											else: return 'False'
										elif obj[4]>6:
											return 'True'
										else: return 'True'
									elif obj[1]<=0:
										# {"feature": "Age", "instances": 29, "metric_value": 0.4496, "depth": 10}
										if obj[4]<=5:
											# {"feature": "Direction_same", "instances": 27, "metric_value": 0.4392, "depth": 11}
											if obj[11]<=0:
												# {"feature": "Coffeehouse", "instances": 17, "metric_value": 0.3832, "depth": 12}
												if obj[9]>1.0:
													# {"feature": "Passanger", "instances": 10, "metric_value": 0.4762, "depth": 13}
													if obj[0]<=0:
														return 'False'
													elif obj[0]>0:
														return 'False'
													else: return 'False'
												elif obj[9]<=1.0:
													# {"feature": "Passanger", "instances": 7, "metric_value": 0.2381, "depth": 13}
													if obj[0]>0:
														return 'False'
													elif obj[0]<=0:
														return 'False'
													else: return 'False'
												else: return 'False'
											elif obj[11]>0:
												# {"feature": "Coffeehouse", "instances": 10, "metric_value": 0.4, "depth": 12}
												if obj[9]>1.0:
													# {"feature": "Passanger", "instances": 8, "metric_value": 0.5, "depth": 13}
													if obj[0]<=1:
														return 'False'
													else: return 'False'
												elif obj[9]<=1.0:
													return 'True'
												else: return 'True'
											else: return 'True'
										elif obj[4]>5:
											return 'True'
										else: return 'True'
									else: return 'False'
								elif obj[7]<=1:
									# {"feature": "Age", "instances": 29, "metric_value": 0.1352, "depth": 9}
									if obj[4]<=6:
										# {"feature": "Passanger", "instances": 25, "metric_value": 0.06, "depth": 10}
										if obj[0]>0:
											return 'False'
										elif obj[0]<=0:
											# {"feature": "Time", "instances": 4, "metric_value": 0.25, "depth": 11}
											if obj[1]>0:
												# {"feature": "Coffeehouse", "instances": 2, "metric_value": 0.5, "depth": 12}
												if obj[9]<=0.0:
													# {"feature": "Direction_same", "instances": 2, "metric_value": 0.5, "depth": 13}
													if obj[11]<=0:
														return 'True'
													else: return 'True'
												else: return 'True'
											elif obj[1]<=0:
												return 'False'
											else: return 'False'
										else: return 'False'
									elif obj[4]>6:
										# {"feature": "Passanger", "instances": 4, "metric_value": 0.0, "depth": 10}
										if obj[0]>1:
											return 'True'
										elif obj[0]<=1:
											return 'False'
										else: return 'False'
									else: return 'True'
								else: return 'False'
							elif obj[12]>2:
								# {"feature": "Coffeehouse", "instances": 28, "metric_value": 0.1209, "depth": 8}
								if obj[9]<=1.0:
									return 'False'
								elif obj[9]>1.0:
									# {"feature": "Time", "instances": 13, "metric_value": 0.2168, "depth": 9}
									if obj[1]>0:
										# {"feature": "Age", "instances": 11, "metric_value": 0.1212, "depth": 10}
										if obj[4]<=2:
											return 'False'
										elif obj[4]>2:
											# {"feature": "Occupation", "instances": 3, "metric_value": 0.3333, "depth": 11}
											if obj[7]>1:
												# {"feature": "Passanger", "instances": 2, "metric_value": 0.5, "depth": 12}
												if obj[0]<=1:
													# {"feature": "Direction_same", "instances": 2, "metric_value": 0.5, "depth": 13}
													if obj[11]<=0:
														return 'False'
													else: return 'False'
												else: return 'False'
											elif obj[7]<=1:
												return 'False'
											else: return 'False'
										else: return 'False'
									elif obj[1]<=0:
										# {"feature": "Age", "instances": 2, "metric_value": 0.0, "depth": 10}
										if obj[4]<=0:
											return 'True'
										elif obj[4]>0:
											return 'False'
										else: return 'False'
									else: return 'True'
								else: return 'False'
							else: return 'False'
						elif obj[3]<=0:
							# {"feature": "Coffeehouse", "instances": 145, "metric_value": 0.457, "depth": 7}
							if obj[9]<=1.0:
								# {"feature": "Occupation", "instances": 106, "metric_value": 0.4315, "depth": 8}
								if obj[7]<=8:
									# {"feature": "Age", "instances": 61, "metric_value": 0.4659, "depth": 9}
									if obj[4]>0:
										# {"feature": "Distance", "instances": 48, "metric_value": 0.4238, "depth": 10}
										if obj[12]>1:
											# {"feature": "Time", "instances": 31, "metric_value": 0.3752, "depth": 11}
											if obj[1]<=2:
												# {"feature": "Direction_same", "instances": 24, "metric_value": 0.3977, "depth": 12}
												if obj[11]<=0:
													# {"feature": "Passanger", "instances": 22, "metric_value": 0.4273, "depth": 13}
													if obj[0]>0:
														return 'False'
													elif obj[0]<=0:
														return 'True'
													else: return 'True'
												elif obj[11]>0:
													return 'False'
												else: return 'False'
											elif obj[1]>2:
												# {"feature": "Direction_same", "instances": 7, "metric_value": 0.1429, "depth": 12}
												if obj[11]<=0:
													return 'False'
												elif obj[11]>0:
													# {"feature": "Passanger", "instances": 2, "metric_value": 0.5, "depth": 13}
													if obj[0]<=1:
														return 'False'
													else: return 'False'
												else: return 'False'
											else: return 'False'
										elif obj[12]<=1:
											# {"feature": "Time", "instances": 17, "metric_value": 0.4941, "depth": 11}
											if obj[1]>0:
												# {"feature": "Passanger", "instances": 12, "metric_value": 0.4857, "depth": 12}
												if obj[0]<=0:
													# {"feature": "Direction_same", "instances": 7, "metric_value": 0.4898, "depth": 13}
													if obj[11]<=0:
														return 'True'
													else: return 'True'
												elif obj[0]>0:
													# {"feature": "Direction_same", "instances": 5, "metric_value": 0.48, "depth": 13}
													if obj[11]<=0:
														return 'False'
													else: return 'False'
												else: return 'False'
											elif obj[1]<=0:
												# {"feature": "Passanger", "instances": 5, "metric_value": 0.48, "depth": 12}
												if obj[0]<=1:
													# {"feature": "Direction_same", "instances": 5, "metric_value": 0.48, "depth": 13}
													if obj[11]<=1:
														return 'True'
													else: return 'True'
												else: return 'True'
											else: return 'True'
										else: return 'True'
									elif obj[4]<=0:
										# {"feature": "Time", "instances": 13, "metric_value": 0.3538, "depth": 10}
										if obj[1]<=2:
											# {"feature": "Passanger", "instances": 8, "metric_value": 0.2143, "depth": 11}
											if obj[0]>0:
												# {"feature": "Direction_same", "instances": 7, "metric_value": 0.1905, "depth": 12}
												if obj[11]<=0:
													return 'True'
												elif obj[11]>0:
													# {"feature": "Distance", "instances": 3, "metric_value": 0.3333, "depth": 13}
													if obj[12]<=1:
														return 'False'
													elif obj[12]>1:
														return 'True'
													else: return 'True'
												else: return 'True'
											elif obj[0]<=0:
												return 'False'
											else: return 'False'
										elif obj[1]>2:
											# {"feature": "Passanger", "instances": 5, "metric_value": 0.2667, "depth": 11}
											if obj[0]<=1:
												# {"feature": "Distance", "instances": 3, "metric_value": 0.3333, "depth": 12}
												if obj[12]>1:
													# {"feature": "Direction_same", "instances": 2, "metric_value": 0.5, "depth": 13}
													if obj[11]<=0:
														return 'False'
													else: return 'False'
												elif obj[12]<=1:
													return 'False'
												else: return 'False'
											elif obj[0]>1:
												return 'False'
											else: return 'False'
										else: return 'False'
									else: return 'True'
								elif obj[7]>8:
									# {"feature": "Passanger", "instances": 45, "metric_value": 0.3145, "depth": 9}
									if obj[0]<=1:
										# {"feature": "Age", "instances": 39, "metric_value": 0.2815, "depth": 10}
										if obj[4]>1:
											# {"feature": "Time", "instances": 25, "metric_value": 0.3575, "depth": 11}
											if obj[1]<=1:
												# {"feature": "Distance", "instances": 18, "metric_value": 0.3897, "depth": 12}
												if obj[12]<=2:
													# {"feature": "Direction_same", "instances": 13, "metric_value": 0.3538, "depth": 13}
													if obj[11]<=0:
														return 'False'
													elif obj[11]>0:
														return 'False'
													else: return 'False'
												elif obj[12]>2:
													# {"feature": "Direction_same", "instances": 5, "metric_value": 0.48, "depth": 13}
													if obj[11]<=0:
														return 'False'
													else: return 'False'
												else: return 'False'
											elif obj[1]>1:
												# {"feature": "Distance", "instances": 7, "metric_value": 0.2381, "depth": 12}
												if obj[12]<=1:
													# {"feature": "Direction_same", "instances": 6, "metric_value": 0.2778, "depth": 13}
													if obj[11]<=0:
														return 'False'
													else: return 'False'
												elif obj[12]>1:
													return 'False'
												else: return 'False'
											else: return 'False'
										elif obj[4]<=1:
											# {"feature": "Time", "instances": 14, "metric_value": 0.1071, "depth": 11}
											if obj[1]<=2:
												return 'False'
											elif obj[1]>2:
												# {"feature": "Distance", "instances": 4, "metric_value": 0.3333, "depth": 12}
												if obj[12]<=1:
													# {"feature": "Direction_same", "instances": 3, "metric_value": 0.4444, "depth": 13}
													if obj[11]<=0:
														return 'False'
													else: return 'False'
												elif obj[12]>1:
													return 'False'
												else: return 'False'
											else: return 'False'
										else: return 'False'
									elif obj[0]>1:
										# {"feature": "Age", "instances": 6, "metric_value": 0.2222, "depth": 10}
										if obj[4]<=2:
											return 'True'
										elif obj[4]>2:
											# {"feature": "Time", "instances": 3, "metric_value": 0.0, "depth": 11}
											if obj[1]<=3:
												return 'False'
											elif obj[1]>3:
												return 'True'
											else: return 'True'
										else: return 'False'
									else: return 'True'
								else: return 'False'
							elif obj[9]>1.0:
								# {"feature": "Age", "instances": 39, "metric_value": 0.4487, "depth": 8}
								if obj[4]>0:
									# {"feature": "Occupation", "instances": 36, "metric_value": 0.4609, "depth": 9}
									if obj[7]>1:
										# {"feature": "Distance", "instances": 27, "metric_value": 0.4431, "depth": 10}
										if obj[12]>1:
											# {"feature": "Direction_same", "instances": 17, "metric_value": 0.4044, "depth": 11}
											if obj[11]<=0:
												# {"feature": "Passanger", "instances": 16, "metric_value": 0.4167, "depth": 12}
												if obj[0]>0:
													# {"feature": "Time", "instances": 15, "metric_value": 0.4286, "depth": 13}
													if obj[1]<=3:
														return 'True'
													elif obj[1]>3:
														return 'True'
													else: return 'True'
												elif obj[0]<=0:
													return 'True'
												else: return 'True'
											elif obj[11]>0:
												return 'False'
											else: return 'False'
										elif obj[12]<=1:
											# {"feature": "Passanger", "instances": 10, "metric_value": 0.3111, "depth": 11}
											if obj[0]<=1:
												# {"feature": "Time", "instances": 9, "metric_value": 0.3333, "depth": 12}
												if obj[1]>0:
													# {"feature": "Direction_same", "instances": 6, "metric_value": 0.2667, "depth": 13}
													if obj[11]<=0:
														return 'False'
													elif obj[11]>0:
														return 'False'
													else: return 'False'
												elif obj[1]<=0:
													# {"feature": "Direction_same", "instances": 3, "metric_value": 0.4444, "depth": 13}
													if obj[11]<=1:
														return 'False'
													else: return 'False'
												else: return 'False'
											elif obj[0]>1:
												return 'True'
											else: return 'True'
										else: return 'False'
									elif obj[7]<=1:
										# {"feature": "Time", "instances": 9, "metric_value": 0.2963, "depth": 10}
										if obj[1]>0:
											# {"feature": "Distance", "instances": 6, "metric_value": 0.4, "depth": 11}
											if obj[12]>1:
												# {"feature": "Passanger", "instances": 5, "metric_value": 0.4667, "depth": 12}
												if obj[0]<=1:
													# {"feature": "Direction_same", "instances": 3, "metric_value": 0.4444, "depth": 13}
													if obj[11]<=0:
														return 'True'
													else: return 'True'
												elif obj[0]>1:
													# {"feature": "Direction_same", "instances": 2, "metric_value": 0.5, "depth": 13}
													if obj[11]<=0:
														return 'True'
													else: return 'True'
												else: return 'True'
											elif obj[12]<=1:
												return 'True'
											else: return 'True'
										elif obj[1]<=0:
											return 'True'
										else: return 'True'
									else: return 'True'
								elif obj[4]<=0:
									return 'False'
								else: return 'False'
							else: return 'True'
						else: return 'False'
					else: return 'False'
				elif obj[10]>1.0:
					# {"feature": "Age", "instances": 207, "metric_value": 0.49, "depth": 5}
					if obj[4]<=2:
						# {"feature": "Coffeehouse", "instances": 107, "metric_value": 0.4728, "depth": 6}
						if obj[9]<=3.0:
							# {"feature": "Occupation", "instances": 98, "metric_value": 0.4645, "depth": 7}
							if obj[7]<=6:
								# {"feature": "Time", "instances": 56, "metric_value": 0.4362, "depth": 8}
								if obj[1]<=3:
									# {"feature": "Passanger", "instances": 50, "metric_value": 0.4174, "depth": 9}
									if obj[0]>0:
										# {"feature": "Distance", "instances": 46, "metric_value": 0.4451, "depth": 10}
										if obj[12]>1:
											# {"feature": "Direction_same", "instances": 30, "metric_value": 0.4, "depth": 11}
											if obj[11]<=0:
												# {"feature": "Education", "instances": 27, "metric_value": 0.44, "depth": 12}
												if obj[6]>0:
													# {"feature": "Gender", "instances": 25, "metric_value": 0.435, "depth": 13}
													if obj[3]<=0:
														return 'False'
													elif obj[3]>0:
														return 'False'
													else: return 'False'
												elif obj[6]<=0:
													# {"feature": "Gender", "instances": 2, "metric_value": 0.5, "depth": 13}
													if obj[3]<=1:
														return 'True'
													else: return 'True'
												else: return 'True'
											elif obj[11]>0:
												return 'False'
											else: return 'False'
										elif obj[12]<=1:
											# {"feature": "Education", "instances": 16, "metric_value": 0.4409, "depth": 11}
											if obj[6]>1:
												# {"feature": "Gender", "instances": 11, "metric_value": 0.4481, "depth": 12}
												if obj[3]<=0:
													# {"feature": "Direction_same", "instances": 7, "metric_value": 0.4857, "depth": 13}
													if obj[11]>0:
														return 'False'
													elif obj[11]<=0:
														return 'True'
													else: return 'True'
												elif obj[3]>0:
													# {"feature": "Direction_same", "instances": 4, "metric_value": 0.3333, "depth": 13}
													if obj[11]>0:
														return 'True'
													elif obj[11]<=0:
														return 'True'
													else: return 'True'
												else: return 'True'
											elif obj[6]<=1:
												# {"feature": "Direction_same", "instances": 5, "metric_value": 0.2667, "depth": 12}
												if obj[11]<=0:
													# {"feature": "Gender", "instances": 3, "metric_value": 0.4444, "depth": 13}
													if obj[3]<=1:
														return 'False'
													else: return 'False'
												elif obj[11]>0:
													return 'False'
												else: return 'False'
											else: return 'False'
										else: return 'False'
									elif obj[0]<=0:
										return 'False'
									else: return 'False'
								elif obj[1]>3:
									# {"feature": "Passanger", "instances": 6, "metric_value": 0.2667, "depth": 9}
									if obj[0]<=1:
										# {"feature": "Distance", "instances": 5, "metric_value": 0.0, "depth": 10}
										if obj[12]<=1:
											return 'True'
										elif obj[12]>1:
											return 'False'
										else: return 'False'
									elif obj[0]>1:
										return 'False'
									else: return 'False'
								else: return 'True'
							elif obj[7]>6:
								# {"feature": "Gender", "instances": 42, "metric_value": 0.4505, "depth": 8}
								if obj[3]>0:
									# {"feature": "Education", "instances": 26, "metric_value": 0.4573, "depth": 9}
									if obj[6]>0:
										# {"feature": "Direction_same", "instances": 18, "metric_value": 0.4148, "depth": 10}
										if obj[11]<=0:
											# {"feature": "Time", "instances": 15, "metric_value": 0.4405, "depth": 11}
											if obj[1]<=1:
												# {"feature": "Passanger", "instances": 8, "metric_value": 0.4286, "depth": 12}
												if obj[0]>0:
													# {"feature": "Distance", "instances": 7, "metric_value": 0.4762, "depth": 13}
													if obj[12]<=2:
														return 'True'
													elif obj[12]>2:
														return 'False'
													else: return 'False'
												elif obj[0]<=0:
													return 'False'
												else: return 'False'
											elif obj[1]>1:
												# {"feature": "Distance", "instances": 7, "metric_value": 0.381, "depth": 12}
												if obj[12]<=1:
													# {"feature": "Passanger", "instances": 6, "metric_value": 0.4167, "depth": 13}
													if obj[0]<=0:
														return 'True'
													elif obj[0]>0:
														return 'False'
													else: return 'False'
												elif obj[12]>1:
													return 'True'
												else: return 'True'
											else: return 'True'
										elif obj[11]>0:
											return 'False'
										else: return 'False'
									elif obj[6]<=0:
										# {"feature": "Distance", "instances": 8, "metric_value": 0.2143, "depth": 10}
										if obj[12]<=2:
											# {"feature": "Time", "instances": 7, "metric_value": 0.1429, "depth": 11}
											if obj[1]<=3:
												return 'True'
											elif obj[1]>3:
												# {"feature": "Passanger", "instances": 2, "metric_value": 0.5, "depth": 12}
												if obj[0]<=0:
													# {"feature": "Direction_same", "instances": 2, "metric_value": 0.5, "depth": 13}
													if obj[11]<=0:
														return 'True'
													else: return 'True'
												else: return 'True'
											else: return 'True'
										elif obj[12]>2:
											return 'False'
										else: return 'False'
									else: return 'True'
								elif obj[3]<=0:
									# {"feature": "Passanger", "instances": 16, "metric_value": 0.3, "depth": 9}
									if obj[0]<=1:
										# {"feature": "Time", "instances": 15, "metric_value": 0.28, "depth": 10}
										if obj[1]<=2:
											# {"feature": "Education", "instances": 10, "metric_value": 0.1333, "depth": 11}
											if obj[6]>0:
												return 'True'
											elif obj[6]<=0:
												# {"feature": "Distance", "instances": 3, "metric_value": 0.0, "depth": 12}
												if obj[12]<=2:
													return 'True'
												elif obj[12]>2:
													return 'False'
												else: return 'False'
											else: return 'True'
										elif obj[1]>2:
											# {"feature": "Distance", "instances": 5, "metric_value": 0.2667, "depth": 11}
											if obj[12]<=1:
												# {"feature": "Education", "instances": 3, "metric_value": 0.3333, "depth": 12}
												if obj[6]<=0:
													# {"feature": "Direction_same", "instances": 2, "metric_value": 0.5, "depth": 13}
													if obj[11]<=0:
														return 'True'
													else: return 'True'
												elif obj[6]>0:
													return 'False'
												else: return 'False'
											elif obj[12]>1:
												return 'True'
											else: return 'True'
										else: return 'True'
									elif obj[0]>1:
										return 'False'
									else: return 'False'
								else: return 'True'
							else: return 'True'
						elif obj[9]>3.0:
							# {"feature": "Passanger", "instances": 9, "metric_value": 0.1481, "depth": 7}
							if obj[0]>0:
								return 'False'
							elif obj[0]<=0:
								# {"feature": "Time", "instances": 3, "metric_value": 0.3333, "depth": 8}
								if obj[1]<=2:
									# {"feature": "Gender", "instances": 2, "metric_value": 0.5, "depth": 9}
									if obj[3]<=0:
										# {"feature": "Education", "instances": 2, "metric_value": 0.5, "depth": 10}
										if obj[6]<=3:
											# {"feature": "Occupation", "instances": 2, "metric_value": 0.5, "depth": 11}
											if obj[7]<=20:
												# {"feature": "Direction_same", "instances": 2, "metric_value": 0.5, "depth": 12}
												if obj[11]<=0:
													# {"feature": "Distance", "instances": 2, "metric_value": 0.5, "depth": 13}
													if obj[12]<=1:
														return 'False'
													else: return 'False'
												else: return 'False'
											else: return 'False'
										else: return 'False'
									else: return 'False'
								elif obj[1]>2:
									return 'False'
								else: return 'False'
							else: return 'False'
						else: return 'False'
					elif obj[4]>2:
						# {"feature": "Gender", "instances": 100, "metric_value": 0.4744, "depth": 6}
						if obj[3]>0:
							# {"feature": "Passanger", "instances": 50, "metric_value": 0.4681, "depth": 7}
							if obj[0]<=2:
								# {"feature": "Distance", "instances": 47, "metric_value": 0.4617, "depth": 8}
								if obj[12]>1:
									# {"feature": "Coffeehouse", "instances": 30, "metric_value": 0.4159, "depth": 9}
									if obj[9]>1.0:
										# {"feature": "Education", "instances": 22, "metric_value": 0.3409, "depth": 10}
										if obj[6]<=0:
											# {"feature": "Direction_same", "instances": 16, "metric_value": 0.4038, "depth": 11}
											if obj[11]<=0:
												# {"feature": "Occupation", "instances": 13, "metric_value": 0.4487, "depth": 12}
												if obj[7]>1:
													# {"feature": "Time", "instances": 12, "metric_value": 0.4792, "depth": 13}
													if obj[1]>0:
														return 'False'
													elif obj[1]<=0:
														return 'True'
													else: return 'True'
												elif obj[7]<=1:
													return 'True'
												else: return 'True'
											elif obj[11]>0:
												return 'False'
											else: return 'False'
										elif obj[6]>0:
											return 'False'
										else: return 'False'
									elif obj[9]<=1.0:
										# {"feature": "Time", "instances": 8, "metric_value": 0.3667, "depth": 10}
										if obj[1]>0:
											# {"feature": "Occupation", "instances": 5, "metric_value": 0.2, "depth": 11}
											if obj[7]>1:
												return 'True'
											elif obj[7]<=1:
												# {"feature": "Education", "instances": 2, "metric_value": 0.5, "depth": 12}
												if obj[6]<=1:
													# {"feature": "Direction_same", "instances": 2, "metric_value": 0.5, "depth": 13}
													if obj[11]<=0:
														return 'True'
													else: return 'True'
												else: return 'True'
											else: return 'True'
										elif obj[1]<=0:
											# {"feature": "Occupation", "instances": 3, "metric_value": 0.0, "depth": 11}
											if obj[7]<=2:
												return 'False'
											elif obj[7]>2:
												return 'True'
											else: return 'True'
										else: return 'False'
									else: return 'True'
								elif obj[12]<=1:
									# {"feature": "Occupation", "instances": 17, "metric_value": 0.3899, "depth": 9}
									if obj[7]>1:
										# {"feature": "Time", "instances": 10, "metric_value": 0.3, "depth": 10}
										if obj[1]>0:
											# {"feature": "Direction_same", "instances": 8, "metric_value": 0.2143, "depth": 11}
											if obj[11]<=0:
												# {"feature": "Education", "instances": 7, "metric_value": 0.1429, "depth": 12}
												if obj[6]<=0:
													return 'True'
												elif obj[6]>0:
													# {"feature": "Coffeehouse", "instances": 2, "metric_value": 0.0, "depth": 13}
													if obj[9]<=0.0:
														return 'True'
													elif obj[9]>0.0:
														return 'False'
													else: return 'False'
												else: return 'True'
											elif obj[11]>0:
												return 'False'
											else: return 'False'
										elif obj[1]<=0:
											return 'True'
										else: return 'True'
									elif obj[7]<=1:
										# {"feature": "Coffeehouse", "instances": 7, "metric_value": 0.3429, "depth": 10}
										if obj[9]<=2.0:
											# {"feature": "Time", "instances": 5, "metric_value": 0.2667, "depth": 11}
											if obj[1]<=1:
												# {"feature": "Education", "instances": 3, "metric_value": 0.3333, "depth": 12}
												if obj[6]>1:
													# {"feature": "Direction_same", "instances": 2, "metric_value": 0.5, "depth": 13}
													if obj[11]<=1:
														return 'True'
													else: return 'True'
												elif obj[6]<=1:
													return 'False'
												else: return 'False'
											elif obj[1]>1:
												return 'True'
											else: return 'True'
										elif obj[9]>2.0:
											return 'False'
										else: return 'False'
									else: return 'False'
								else: return 'True'
							elif obj[0]>2:
								return 'True'
							else: return 'True'
						elif obj[3]<=0:
							# {"feature": "Education", "instances": 50, "metric_value": 0.4162, "depth": 7}
							if obj[6]>0:
								# {"feature": "Coffeehouse", "instances": 27, "metric_value": 0.3085, "depth": 8}
								if obj[9]>1.0:
									# {"feature": "Passanger", "instances": 17, "metric_value": 0.1412, "depth": 9}
									if obj[0]>0:
										return 'True'
									elif obj[0]<=0:
										# {"feature": "Time", "instances": 5, "metric_value": 0.2667, "depth": 10}
										if obj[1]>0:
											# {"feature": "Occupation", "instances": 3, "metric_value": 0.3333, "depth": 11}
											if obj[7]>2:
												# {"feature": "Direction_same", "instances": 2, "metric_value": 0.5, "depth": 12}
												if obj[11]<=0:
													# {"feature": "Distance", "instances": 2, "metric_value": 0.5, "depth": 13}
													if obj[12]<=1:
														return 'True'
													else: return 'True'
												else: return 'True'
											elif obj[7]<=2:
												return 'False'
											else: return 'False'
										elif obj[1]<=0:
											return 'True'
										else: return 'True'
									else: return 'True'
								elif obj[9]<=1.0:
									# {"feature": "Passanger", "instances": 10, "metric_value": 0.4, "depth": 9}
									if obj[0]<=1:
										# {"feature": "Time", "instances": 9, "metric_value": 0.381, "depth": 10}
										if obj[1]<=1:
											# {"feature": "Distance", "instances": 7, "metric_value": 0.3429, "depth": 11}
											if obj[12]<=2:
												# {"feature": "Occupation", "instances": 5, "metric_value": 0.3, "depth": 12}
												if obj[7]>6:
													# {"feature": "Direction_same", "instances": 4, "metric_value": 0.25, "depth": 13}
													if obj[11]<=0:
														return 'False'
													elif obj[11]>0:
														return 'True'
													else: return 'True'
												elif obj[7]<=6:
													return 'True'
												else: return 'True'
											elif obj[12]>2:
												return 'True'
											else: return 'True'
										elif obj[1]>1:
											return 'True'
										else: return 'True'
									elif obj[0]>1:
										return 'False'
									else: return 'False'
								else: return 'True'
							elif obj[6]<=0:
								# {"feature": "Distance", "instances": 23, "metric_value": 0.4101, "depth": 8}
								if obj[12]<=2:
									# {"feature": "Passanger", "instances": 17, "metric_value": 0.4235, "depth": 9}
									if obj[0]<=1:
										# {"feature": "Coffeehouse", "instances": 15, "metric_value": 0.44, "depth": 10}
										if obj[9]<=1.0:
											# {"feature": "Time", "instances": 10, "metric_value": 0.4444, "depth": 11}
											if obj[1]<=3:
												# {"feature": "Occupation", "instances": 9, "metric_value": 0.381, "depth": 12}
												if obj[7]>5:
													# {"feature": "Direction_same", "instances": 7, "metric_value": 0.4857, "depth": 13}
													if obj[11]<=0:
														return 'True'
													elif obj[11]>0:
														return 'False'
													else: return 'False'
												elif obj[7]<=5:
													return 'False'
												else: return 'False'
											elif obj[1]>3:
												return 'True'
											else: return 'True'
										elif obj[9]>1.0:
											# {"feature": "Time", "instances": 5, "metric_value": 0.2667, "depth": 11}
											if obj[1]>0:
												# {"feature": "Occupation", "instances": 3, "metric_value": 0.4444, "depth": 12}
												if obj[7]<=7:
													# {"feature": "Direction_same", "instances": 3, "metric_value": 0.4444, "depth": 13}
													if obj[11]<=0:
														return 'True'
													else: return 'True'
												else: return 'True'
											elif obj[1]<=0:
												return 'True'
											else: return 'True'
										else: return 'True'
									elif obj[0]>1:
										return 'True'
									else: return 'True'
								elif obj[12]>2:
									# {"feature": "Time", "instances": 6, "metric_value": 0.1667, "depth": 9}
									if obj[1]>0:
										return 'False'
									elif obj[1]<=0:
										# {"feature": "Occupation", "instances": 2, "metric_value": 0.0, "depth": 10}
										if obj[7]>7:
											return 'True'
										elif obj[7]<=7:
											return 'False'
										else: return 'False'
									else: return 'True'
								else: return 'False'
							else: return 'True'
						else: return 'True'
					else: return 'True'
				else: return 'True'
			else: return 'False'
		elif obj[8]>1.0:
			# {"feature": "Restaurant20to50", "instances": 680, "metric_value": 0.4641, "depth": 3}
			if obj[10]<=1.0:
				# {"feature": "Time", "instances": 365, "metric_value": 0.4856, "depth": 4}
				if obj[1]>0:
					# {"feature": "Passanger", "instances": 267, "metric_value": 0.4792, "depth": 5}
					if obj[0]<=2:
						# {"feature": "Occupation", "instances": 207, "metric_value": 0.4675, "depth": 6}
						if obj[7]<=14.155999220544217:
							# {"feature": "Distance", "instances": 174, "metric_value": 0.4853, "depth": 7}
							if obj[12]<=2:
								# {"feature": "Age", "instances": 128, "metric_value": 0.4792, "depth": 8}
								if obj[4]<=4:
									# {"feature": "Coffeehouse", "instances": 120, "metric_value": 0.4839, "depth": 9}
									if obj[9]<=2.0:
										# {"feature": "Education", "instances": 75, "metric_value": 0.4876, "depth": 10}
										if obj[6]>1:
											# {"feature": "Children", "instances": 42, "metric_value": 0.4937, "depth": 11}
											if obj[5]<=0:
												# {"feature": "Direction_same", "instances": 30, "metric_value": 0.4643, "depth": 12}
												if obj[11]<=0:
													# {"feature": "Gender", "instances": 28, "metric_value": 0.4949, "depth": 13}
													if obj[3]<=0:
														return 'False'
													elif obj[3]>0:
														return 'False'
													else: return 'False'
												elif obj[11]>0:
													return 'False'
												else: return 'False'
											elif obj[5]>0:
												# {"feature": "Gender", "instances": 12, "metric_value": 0.3333, "depth": 12}
												if obj[3]<=0:
													# {"feature": "Direction_same", "instances": 9, "metric_value": 0.4286, "depth": 13}
													if obj[11]<=0:
														return 'False'
													elif obj[11]>0:
														return 'False'
													else: return 'False'
												elif obj[3]>0:
													return 'True'
												else: return 'True'
											else: return 'True'
										elif obj[6]<=1:
											# {"feature": "Gender", "instances": 33, "metric_value": 0.4563, "depth": 11}
											if obj[3]<=0:
												# {"feature": "Direction_same", "instances": 17, "metric_value": 0.362, "depth": 12}
												if obj[11]<=0:
													# {"feature": "Children", "instances": 13, "metric_value": 0.4573, "depth": 13}
													if obj[5]<=0:
														return 'True'
													elif obj[5]>0:
														return 'True'
													else: return 'True'
												elif obj[11]>0:
													return 'True'
												else: return 'True'
											elif obj[3]>0:
												# {"feature": "Direction_same", "instances": 16, "metric_value": 0.4667, "depth": 12}
												if obj[11]<=0:
													# {"feature": "Children", "instances": 15, "metric_value": 0.4786, "depth": 13}
													if obj[5]<=0:
														return 'True'
													elif obj[5]>0:
														return 'False'
													else: return 'False'
												elif obj[11]>0:
													return 'False'
												else: return 'False'
											else: return 'True'
										else: return 'True'
									elif obj[9]>2.0:
										# {"feature": "Education", "instances": 45, "metric_value": 0.4387, "depth": 10}
										if obj[6]>0:
											# {"feature": "Children", "instances": 34, "metric_value": 0.4673, "depth": 11}
											if obj[5]<=0:
												# {"feature": "Direction_same", "instances": 23, "metric_value": 0.4306, "depth": 12}
												if obj[11]<=0:
													# {"feature": "Gender", "instances": 21, "metric_value": 0.4694, "depth": 13}
													if obj[3]<=0:
														return 'False'
													elif obj[3]>0:
														return 'False'
													else: return 'False'
												elif obj[11]>0:
													return 'False'
												else: return 'False'
											elif obj[5]>0:
												# {"feature": "Direction_same", "instances": 11, "metric_value": 0.3409, "depth": 12}
												if obj[11]<=0:
													# {"feature": "Gender", "instances": 8, "metric_value": 0.375, "depth": 13}
													if obj[3]<=0:
														return 'True'
													elif obj[3]>0:
														return 'False'
													else: return 'False'
												elif obj[11]>0:
													return 'True'
												else: return 'True'
											else: return 'True'
										elif obj[6]<=0:
											# {"feature": "Gender", "instances": 11, "metric_value": 0.2597, "depth": 11}
											if obj[3]>0:
												# {"feature": "Children", "instances": 7, "metric_value": 0.3429, "depth": 12}
												if obj[5]<=0:
													# {"feature": "Direction_same", "instances": 5, "metric_value": 0.4, "depth": 13}
													if obj[11]<=0:
														return 'True'
													elif obj[11]>0:
														return 'False'
													else: return 'False'
												elif obj[5]>0:
													return 'False'
												else: return 'False'
											elif obj[3]<=0:
												return 'False'
											else: return 'False'
										else: return 'False'
									else: return 'False'
								elif obj[4]>4:
									# {"feature": "Coffeehouse", "instances": 8, "metric_value": 0.1875, "depth": 9}
									if obj[9]>1.0:
										return 'False'
									elif obj[9]<=1.0:
										# {"feature": "Education", "instances": 4, "metric_value": 0.25, "depth": 10}
										if obj[6]<=0:
											# {"feature": "Gender", "instances": 2, "metric_value": 0.5, "depth": 11}
											if obj[3]<=0:
												# {"feature": "Children", "instances": 2, "metric_value": 0.5, "depth": 12}
												if obj[5]<=1:
													# {"feature": "Direction_same", "instances": 2, "metric_value": 0.5, "depth": 13}
													if obj[11]<=0:
														return 'False'
													else: return 'False'
												else: return 'False'
											else: return 'False'
										elif obj[6]>0:
											return 'False'
										else: return 'False'
									else: return 'False'
								else: return 'False'
							elif obj[12]>2:
								# {"feature": "Children", "instances": 46, "metric_value": 0.4369, "depth": 8}
								if obj[5]<=0:
									# {"feature": "Coffeehouse", "instances": 34, "metric_value": 0.4592, "depth": 9}
									if obj[9]<=2.0:
										# {"feature": "Age", "instances": 20, "metric_value": 0.4768, "depth": 10}
										if obj[4]<=2:
											# {"feature": "Education", "instances": 11, "metric_value": 0.3818, "depth": 11}
											if obj[6]<=3:
												# {"feature": "Gender", "instances": 10, "metric_value": 0.4, "depth": 12}
												if obj[3]<=0:
													# {"feature": "Direction_same", "instances": 9, "metric_value": 0.4444, "depth": 13}
													if obj[11]<=0:
														return 'False'
													else: return 'False'
												elif obj[3]>0:
													return 'False'
												else: return 'False'
											elif obj[6]>3:
												return 'True'
											else: return 'True'
										elif obj[4]>2:
											# {"feature": "Education", "instances": 9, "metric_value": 0.4167, "depth": 11}
											if obj[6]<=2:
												# {"feature": "Gender", "instances": 8, "metric_value": 0.4667, "depth": 12}
												if obj[3]>0:
													# {"feature": "Direction_same", "instances": 5, "metric_value": 0.48, "depth": 13}
													if obj[11]<=0:
														return 'True'
													else: return 'True'
												elif obj[3]<=0:
													# {"feature": "Direction_same", "instances": 3, "metric_value": 0.4444, "depth": 13}
													if obj[11]<=0:
														return 'True'
													else: return 'True'
												else: return 'True'
											elif obj[6]>2:
												return 'False'
											else: return 'False'
										else: return 'True'
									elif obj[9]>2.0:
										# {"feature": "Education", "instances": 14, "metric_value": 0.3297, "depth": 10}
										if obj[6]<=2:
											# {"feature": "Age", "instances": 13, "metric_value": 0.3231, "depth": 11}
											if obj[4]>1:
												# {"feature": "Gender", "instances": 10, "metric_value": 0.4167, "depth": 12}
												if obj[3]>0:
													# {"feature": "Direction_same", "instances": 6, "metric_value": 0.4444, "depth": 13}
													if obj[11]<=0:
														return 'True'
													else: return 'True'
												elif obj[3]<=0:
													# {"feature": "Direction_same", "instances": 4, "metric_value": 0.375, "depth": 13}
													if obj[11]<=0:
														return 'True'
													else: return 'True'
												else: return 'True'
											elif obj[4]<=1:
												return 'True'
											else: return 'True'
										elif obj[6]>2:
											return 'False'
										else: return 'False'
									else: return 'True'
								elif obj[5]>0:
									# {"feature": "Gender", "instances": 12, "metric_value": 0.2, "depth": 9}
									if obj[3]<=0:
										return 'True'
									elif obj[3]>0:
										# {"feature": "Age", "instances": 5, "metric_value": 0.3, "depth": 10}
										if obj[4]>0:
											# {"feature": "Coffeehouse", "instances": 4, "metric_value": 0.25, "depth": 11}
											if obj[9]<=2.0:
												return 'True'
											elif obj[9]>2.0:
												# {"feature": "Education", "instances": 2, "metric_value": 0.0, "depth": 12}
												if obj[6]>2:
													return 'True'
												elif obj[6]<=2:
													return 'False'
												else: return 'False'
											else: return 'True'
										elif obj[4]<=0:
											return 'False'
										else: return 'False'
									else: return 'True'
								else: return 'True'
							else: return 'True'
						elif obj[7]>14.155999220544217:
							# {"feature": "Age", "instances": 33, "metric_value": 0.2458, "depth": 7}
							if obj[4]<=2:
								# {"feature": "Gender", "instances": 24, "metric_value": 0.1212, "depth": 8}
								if obj[3]<=0:
									# {"feature": "Coffeehouse", "instances": 22, "metric_value": 0.0808, "depth": 9}
									if obj[9]>2.0:
										return 'False'
									elif obj[9]<=2.0:
										# {"feature": "Distance", "instances": 9, "metric_value": 0.1111, "depth": 10}
										if obj[12]>1:
											return 'False'
										elif obj[12]<=1:
											# {"feature": "Children", "instances": 2, "metric_value": 0.5, "depth": 11}
											if obj[5]<=1:
												# {"feature": "Education", "instances": 2, "metric_value": 0.5, "depth": 12}
												if obj[6]<=3:
													# {"feature": "Direction_same", "instances": 2, "metric_value": 0.5, "depth": 13}
													if obj[11]<=0:
														return 'True'
													else: return 'True'
												else: return 'True'
											else: return 'True'
										else: return 'True'
									else: return 'False'
								elif obj[3]>0:
									# {"feature": "Direction_same", "instances": 2, "metric_value": 0.0, "depth": 9}
									if obj[11]>0:
										return 'True'
									elif obj[11]<=0:
										return 'False'
									else: return 'False'
								else: return 'True'
							elif obj[4]>2:
								# {"feature": "Distance", "instances": 9, "metric_value": 0.2963, "depth": 8}
								if obj[12]>1:
									# {"feature": "Coffeehouse", "instances": 6, "metric_value": 0.2222, "depth": 9}
									if obj[9]>1.0:
										return 'True'
									elif obj[9]<=1.0:
										# {"feature": "Children", "instances": 3, "metric_value": 0.3333, "depth": 10}
										if obj[5]<=0:
											# {"feature": "Gender", "instances": 2, "metric_value": 0.5, "depth": 11}
											if obj[3]<=0:
												# {"feature": "Education", "instances": 2, "metric_value": 0.5, "depth": 12}
												if obj[6]<=2:
													# {"feature": "Direction_same", "instances": 2, "metric_value": 0.5, "depth": 13}
													if obj[11]<=0:
														return 'True'
													else: return 'True'
												else: return 'True'
											else: return 'True'
										elif obj[5]>0:
											return 'False'
										else: return 'False'
									else: return 'False'
								elif obj[12]<=1:
									return 'False'
								else: return 'False'
							else: return 'False'
						else: return 'False'
					elif obj[0]>2:
						# {"feature": "Age", "instances": 60, "metric_value": 0.4169, "depth": 6}
						if obj[4]<=6:
							# {"feature": "Coffeehouse", "instances": 59, "metric_value": 0.3999, "depth": 7}
							if obj[9]<=2.0:
								# {"feature": "Children", "instances": 43, "metric_value": 0.438, "depth": 8}
								if obj[5]<=0:
									# {"feature": "Occupation", "instances": 35, "metric_value": 0.419, "depth": 9}
									if obj[7]<=16:
										# {"feature": "Education", "instances": 33, "metric_value": 0.4409, "depth": 10}
										if obj[6]<=2:
											# {"feature": "Gender", "instances": 31, "metric_value": 0.4363, "depth": 11}
											if obj[3]<=0:
												# {"feature": "Distance", "instances": 24, "metric_value": 0.4351, "depth": 12}
												if obj[12]>1:
													# {"feature": "Direction_same", "instances": 19, "metric_value": 0.4654, "depth": 13}
													if obj[11]<=0:
														return 'True'
													else: return 'True'
												elif obj[12]<=1:
													# {"feature": "Direction_same", "instances": 5, "metric_value": 0.32, "depth": 13}
													if obj[11]<=0:
														return 'True'
													else: return 'True'
												else: return 'True'
											elif obj[3]>0:
												# {"feature": "Distance", "instances": 7, "metric_value": 0.2381, "depth": 12}
												if obj[12]>1:
													# {"feature": "Direction_same", "instances": 6, "metric_value": 0.2778, "depth": 13}
													if obj[11]<=0:
														return 'True'
													else: return 'True'
												elif obj[12]<=1:
													return 'False'
												else: return 'False'
											else: return 'True'
										elif obj[6]>2:
											# {"feature": "Gender", "instances": 2, "metric_value": 0.0, "depth": 11}
											if obj[3]>0:
												return 'False'
											elif obj[3]<=0:
												return 'True'
											else: return 'True'
										else: return 'False'
									elif obj[7]>16:
										return 'True'
									else: return 'True'
								elif obj[5]>0:
									# {"feature": "Gender", "instances": 8, "metric_value": 0.375, "depth": 9}
									if obj[3]<=0:
										# {"feature": "Occupation", "instances": 6, "metric_value": 0.25, "depth": 10}
										if obj[7]<=15:
											# {"feature": "Education", "instances": 4, "metric_value": 0.25, "depth": 11}
											if obj[6]>0:
												# {"feature": "Direction_same", "instances": 2, "metric_value": 0.5, "depth": 12}
												if obj[11]<=0:
													# {"feature": "Distance", "instances": 2, "metric_value": 0.5, "depth": 13}
													if obj[12]<=2:
														return 'False'
													else: return 'False'
												else: return 'False'
											elif obj[6]<=0:
												return 'True'
											else: return 'True'
										elif obj[7]>15:
											return 'False'
										else: return 'False'
									elif obj[3]>0:
										return 'False'
									else: return 'False'
								else: return 'False'
							elif obj[9]>2.0:
								# {"feature": "Education", "instances": 16, "metric_value": 0.1786, "depth": 8}
								if obj[6]<=2:
									# {"feature": "Occupation", "instances": 14, "metric_value": 0.1143, "depth": 9}
									if obj[7]>6:
										return 'True'
									elif obj[7]<=6:
										# {"feature": "Gender", "instances": 5, "metric_value": 0.2667, "depth": 10}
										if obj[3]<=0:
											# {"feature": "Children", "instances": 3, "metric_value": 0.0, "depth": 11}
											if obj[5]<=0:
												return 'True'
											elif obj[5]>0:
												return 'False'
											else: return 'False'
										elif obj[3]>0:
											return 'True'
										else: return 'True'
									else: return 'True'
								elif obj[6]>2:
									# {"feature": "Children", "instances": 2, "metric_value": 0.0, "depth": 9}
									if obj[5]<=0:
										return 'False'
									elif obj[5]>0:
										return 'True'
									else: return 'True'
								else: return 'False'
							else: return 'True'
						elif obj[4]>6:
							return 'False'
						else: return 'False'
					else: return 'True'
				elif obj[1]<=0:
					# {"feature": "Passanger", "instances": 98, "metric_value": 0.4319, "depth": 5}
					if obj[0]<=1:
						# {"feature": "Distance", "instances": 90, "metric_value": 0.4178, "depth": 6}
						if obj[12]<=1:
							# {"feature": "Occupation", "instances": 46, "metric_value": 0.3188, "depth": 7}
							if obj[7]>3:
								# {"feature": "Gender", "instances": 33, "metric_value": 0.4139, "depth": 8}
								if obj[3]<=0:
									# {"feature": "Age", "instances": 26, "metric_value": 0.3523, "depth": 9}
									if obj[4]<=5:
										# {"feature": "Education", "instances": 23, "metric_value": 0.3066, "depth": 10}
										if obj[6]<=2:
											# {"feature": "Coffeehouse", "instances": 19, "metric_value": 0.2481, "depth": 11}
											if obj[9]<=2.0:
												# {"feature": "Children", "instances": 14, "metric_value": 0.3214, "depth": 12}
												if obj[5]<=0:
													# {"feature": "Direction_same", "instances": 12, "metric_value": 0.375, "depth": 13}
													if obj[11]<=1:
														return 'True'
													else: return 'True'
												elif obj[5]>0:
													return 'True'
												else: return 'True'
											elif obj[9]>2.0:
												return 'True'
											else: return 'True'
										elif obj[6]>2:
											# {"feature": "Coffeehouse", "instances": 4, "metric_value": 0.3333, "depth": 11}
											if obj[9]<=2.0:
												# {"feature": "Children", "instances": 3, "metric_value": 0.3333, "depth": 12}
												if obj[5]>0:
													# {"feature": "Direction_same", "instances": 2, "metric_value": 0.5, "depth": 13}
													if obj[11]<=1:
														return 'True'
													else: return 'True'
												elif obj[5]<=0:
													return 'True'
												else: return 'True'
											elif obj[9]>2.0:
												return 'False'
											else: return 'False'
										else: return 'False'
									elif obj[4]>5:
										# {"feature": "Coffeehouse", "instances": 3, "metric_value": 0.0, "depth": 10}
										if obj[9]<=1.0:
											return 'False'
										elif obj[9]>1.0:
											return 'True'
										else: return 'True'
									else: return 'False'
								elif obj[3]>0:
									# {"feature": "Coffeehouse", "instances": 7, "metric_value": 0.2286, "depth": 9}
									if obj[9]<=2.0:
										# {"feature": "Age", "instances": 5, "metric_value": 0.0, "depth": 10}
										if obj[4]>0:
											return 'False'
										elif obj[4]<=0:
											return 'True'
										else: return 'True'
									elif obj[9]>2.0:
										return 'True'
									else: return 'True'
								else: return 'False'
							elif obj[7]<=3:
								return 'True'
							else: return 'True'
						elif obj[12]>1:
							# {"feature": "Occupation", "instances": 44, "metric_value": 0.4325, "depth": 7}
							if obj[7]>4:
								# {"feature": "Education", "instances": 33, "metric_value": 0.3866, "depth": 8}
								if obj[6]>0:
									# {"feature": "Coffeehouse", "instances": 23, "metric_value": 0.4551, "depth": 9}
									if obj[9]<=2.0:
										# {"feature": "Age", "instances": 15, "metric_value": 0.4636, "depth": 10}
										if obj[4]>0:
											# {"feature": "Gender", "instances": 11, "metric_value": 0.4949, "depth": 11}
											if obj[3]<=0:
												# {"feature": "Children", "instances": 9, "metric_value": 0.4921, "depth": 12}
												if obj[5]<=0:
													# {"feature": "Direction_same", "instances": 7, "metric_value": 0.4898, "depth": 13}
													if obj[11]<=0:
														return 'False'
													else: return 'False'
												elif obj[5]>0:
													# {"feature": "Direction_same", "instances": 2, "metric_value": 0.5, "depth": 13}
													if obj[11]<=0:
														return 'False'
													else: return 'False'
												else: return 'False'
											elif obj[3]>0:
												# {"feature": "Children", "instances": 2, "metric_value": 0.5, "depth": 12}
												if obj[5]<=0:
													# {"feature": "Direction_same", "instances": 2, "metric_value": 0.5, "depth": 13}
													if obj[11]<=0:
														return 'True'
													else: return 'True'
												else: return 'True'
											else: return 'True'
										elif obj[4]<=0:
											# {"feature": "Gender", "instances": 4, "metric_value": 0.3333, "depth": 11}
											if obj[3]>0:
												# {"feature": "Children", "instances": 3, "metric_value": 0.3333, "depth": 12}
												if obj[5]<=0:
													# {"feature": "Direction_same", "instances": 2, "metric_value": 0.5, "depth": 13}
													if obj[11]<=0:
														return 'True'
													else: return 'True'
												elif obj[5]>0:
													return 'True'
												else: return 'True'
											elif obj[3]<=0:
												return 'True'
											else: return 'True'
										else: return 'True'
									elif obj[9]>2.0:
										# {"feature": "Gender", "instances": 8, "metric_value": 0.1667, "depth": 10}
										if obj[3]<=0:
											return 'True'
										elif obj[3]>0:
											# {"feature": "Age", "instances": 3, "metric_value": 0.3333, "depth": 11}
											if obj[4]>2:
												# {"feature": "Children", "instances": 2, "metric_value": 0.5, "depth": 12}
												if obj[5]<=0:
													# {"feature": "Direction_same", "instances": 2, "metric_value": 0.5, "depth": 13}
													if obj[11]<=0:
														return 'False'
													else: return 'False'
												else: return 'False'
											elif obj[4]<=2:
												return 'False'
											else: return 'False'
										else: return 'False'
									else: return 'True'
								elif obj[6]<=0:
									# {"feature": "Direction_same", "instances": 10, "metric_value": 0.0, "depth": 9}
									if obj[11]<=0:
										return 'True'
									elif obj[11]>0:
										return 'False'
									else: return 'False'
								else: return 'True'
							elif obj[7]<=4:
								# {"feature": "Coffeehouse", "instances": 11, "metric_value": 0.3697, "depth": 8}
								if obj[9]>1.0:
									# {"feature": "Education", "instances": 6, "metric_value": 0.1667, "depth": 9}
									if obj[6]>0:
										return 'False'
									elif obj[6]<=0:
										# {"feature": "Gender", "instances": 2, "metric_value": 0.0, "depth": 10}
										if obj[3]>0:
											return 'False'
										elif obj[3]<=0:
											return 'True'
										else: return 'True'
									else: return 'False'
								elif obj[9]<=1.0:
									# {"feature": "Age", "instances": 5, "metric_value": 0.3, "depth": 9}
									if obj[4]>0:
										# {"feature": "Gender", "instances": 4, "metric_value": 0.3333, "depth": 10}
										if obj[3]<=0:
											# {"feature": "Children", "instances": 3, "metric_value": 0.3333, "depth": 11}
											if obj[5]<=0:
												# {"feature": "Education", "instances": 2, "metric_value": 0.5, "depth": 12}
												if obj[6]<=0:
													# {"feature": "Direction_same", "instances": 2, "metric_value": 0.5, "depth": 13}
													if obj[11]<=0:
														return 'True'
													else: return 'True'
												else: return 'True'
											elif obj[5]>0:
												return 'True'
											else: return 'True'
										elif obj[3]>0:
											return 'True'
										else: return 'True'
									elif obj[4]<=0:
										return 'False'
									else: return 'False'
								else: return 'True'
							else: return 'False'
						else: return 'True'
					elif obj[0]>1:
						# {"feature": "Age", "instances": 8, "metric_value": 0.3, "depth": 6}
						if obj[4]>0:
							# {"feature": "Education", "instances": 5, "metric_value": 0.3, "depth": 7}
							if obj[6]>0:
								# {"feature": "Occupation", "instances": 4, "metric_value": 0.0, "depth": 8}
								if obj[7]>5:
									return 'True'
								elif obj[7]<=5:
									return 'False'
								else: return 'False'
							elif obj[6]<=0:
								return 'False'
							else: return 'False'
						elif obj[4]<=0:
							return 'False'
						else: return 'False'
					else: return 'False'
				else: return 'True'
			elif obj[10]>1.0:
				# {"feature": "Education", "instances": 315, "metric_value": 0.417, "depth": 4}
				if obj[6]>1:
					# {"feature": "Time", "instances": 197, "metric_value": 0.451, "depth": 5}
					if obj[1]>0:
						# {"feature": "Passanger", "instances": 150, "metric_value": 0.4737, "depth": 6}
						if obj[0]<=2:
							# {"feature": "Coffeehouse", "instances": 119, "metric_value": 0.462, "depth": 7}
							if obj[9]<=3.0:
								# {"feature": "Occupation", "instances": 94, "metric_value": 0.4693, "depth": 8}
								if obj[7]<=17:
									# {"feature": "Age", "instances": 82, "metric_value": 0.4832, "depth": 9}
									if obj[4]>0:
										# {"feature": "Distance", "instances": 70, "metric_value": 0.4695, "depth": 10}
										if obj[12]>1:
											# {"feature": "Direction_same", "instances": 43, "metric_value": 0.4213, "depth": 11}
											if obj[11]<=0:
												# {"feature": "Children", "instances": 39, "metric_value": 0.4217, "depth": 12}
												if obj[5]<=0:
													# {"feature": "Gender", "instances": 30, "metric_value": 0.4444, "depth": 13}
													if obj[3]>0:
														return 'False'
													elif obj[3]<=0:
														return 'False'
													else: return 'False'
												elif obj[5]>0:
													# {"feature": "Gender", "instances": 9, "metric_value": 0.3444, "depth": 13}
													if obj[3]<=0:
														return 'False'
													elif obj[3]>0:
														return 'False'
													else: return 'False'
												else: return 'False'
											elif obj[11]>0:
												# {"feature": "Gender", "instances": 4, "metric_value": 0.3333, "depth": 12}
												if obj[3]>0:
													# {"feature": "Children", "instances": 3, "metric_value": 0.4444, "depth": 13}
													if obj[5]<=0:
														return 'True'
													else: return 'True'
												elif obj[3]<=0:
													return 'True'
												else: return 'True'
											else: return 'True'
										elif obj[12]<=1:
											# {"feature": "Children", "instances": 27, "metric_value": 0.4701, "depth": 11}
											if obj[5]<=0:
												# {"feature": "Gender", "instances": 26, "metric_value": 0.455, "depth": 12}
												if obj[3]>0:
													# {"feature": "Direction_same", "instances": 15, "metric_value": 0.4974, "depth": 13}
													if obj[11]<=0:
														return 'False'
													elif obj[11]>0:
														return 'True'
													else: return 'True'
												elif obj[3]<=0:
													# {"feature": "Direction_same", "instances": 11, "metric_value": 0.3967, "depth": 13}
													if obj[11]<=0:
														return 'True'
													else: return 'True'
												else: return 'True'
											elif obj[5]>0:
												return 'False'
											else: return 'False'
										else: return 'True'
									elif obj[4]<=0:
										# {"feature": "Children", "instances": 12, "metric_value": 0.3704, "depth": 10}
										if obj[5]<=0:
											# {"feature": "Distance", "instances": 9, "metric_value": 0.381, "depth": 11}
											if obj[12]<=2:
												# {"feature": "Gender", "instances": 7, "metric_value": 0.4048, "depth": 12}
												if obj[3]>0:
													# {"feature": "Direction_same", "instances": 4, "metric_value": 0.3333, "depth": 13}
													if obj[11]<=0:
														return 'False'
													elif obj[11]>0:
														return 'False'
													else: return 'False'
												elif obj[3]<=0:
													# {"feature": "Direction_same", "instances": 3, "metric_value": 0.3333, "depth": 13}
													if obj[11]<=0:
														return 'False'
													elif obj[11]>0:
														return 'True'
													else: return 'True'
												else: return 'True'
											elif obj[12]>2:
												return 'True'
											else: return 'True'
										elif obj[5]>0:
											return 'True'
										else: return 'True'
									else: return 'True'
								elif obj[7]>17:
									# {"feature": "Age", "instances": 12, "metric_value": 0.2222, "depth": 9}
									if obj[4]>2:
										# {"feature": "Direction_same", "instances": 6, "metric_value": 0.4, "depth": 10}
										if obj[11]<=0:
											# {"feature": "Distance", "instances": 5, "metric_value": 0.4, "depth": 11}
											if obj[12]<=2:
												# {"feature": "Gender", "instances": 4, "metric_value": 0.5, "depth": 12}
												if obj[3]<=1:
													# {"feature": "Children", "instances": 4, "metric_value": 0.5, "depth": 13}
													if obj[5]<=1:
														return 'True'
													else: return 'True'
												else: return 'True'
											elif obj[12]>2:
												return 'True'
											else: return 'True'
										elif obj[11]>0:
											return 'True'
										else: return 'True'
									elif obj[4]<=2:
										return 'True'
									else: return 'True'
								else: return 'True'
							elif obj[9]>3.0:
								# {"feature": "Direction_same", "instances": 25, "metric_value": 0.2087, "depth": 8}
								if obj[11]<=0:
									# {"feature": "Children", "instances": 23, "metric_value": 0.1957, "depth": 9}
									if obj[5]<=0:
										# {"feature": "Distance", "instances": 12, "metric_value": 0.3429, "depth": 10}
										if obj[12]>1:
											# {"feature": "Occupation", "instances": 7, "metric_value": 0.1905, "depth": 11}
											if obj[7]<=1:
												return 'True'
											elif obj[7]>1:
												# {"feature": "Age", "instances": 3, "metric_value": 0.3333, "depth": 12}
												if obj[4]<=1:
													# {"feature": "Gender", "instances": 2, "metric_value": 0.5, "depth": 13}
													if obj[3]<=0:
														return 'True'
													else: return 'True'
												elif obj[4]>1:
													return 'True'
												else: return 'True'
											else: return 'True'
										elif obj[12]<=1:
											# {"feature": "Gender", "instances": 5, "metric_value": 0.4667, "depth": 11}
											if obj[3]>0:
												# {"feature": "Age", "instances": 3, "metric_value": 0.3333, "depth": 12}
												if obj[4]>1:
													# {"feature": "Occupation", "instances": 2, "metric_value": 0.5, "depth": 13}
													if obj[7]<=16:
														return 'True'
													else: return 'True'
												elif obj[4]<=1:
													return 'True'
												else: return 'True'
											elif obj[3]<=0:
												# {"feature": "Age", "instances": 2, "metric_value": 0.5, "depth": 12}
												if obj[4]<=1:
													# {"feature": "Occupation", "instances": 2, "metric_value": 0.5, "depth": 13}
													if obj[7]<=1:
														return 'True'
													else: return 'True'
												else: return 'True'
											else: return 'True'
										else: return 'True'
									elif obj[5]>0:
										return 'True'
									else: return 'True'
								elif obj[11]>0:
									return 'False'
								else: return 'False'
							else: return 'True'
						elif obj[0]>2:
							# {"feature": "Coffeehouse", "instances": 31, "metric_value": 0.2184, "depth": 7}
							if obj[9]<=3.0:
								# {"feature": "Occupation", "instances": 26, "metric_value": 0.1918, "depth": 8}
								if obj[7]<=17:
									# {"feature": "Age", "instances": 23, "metric_value": 0.083, "depth": 9}
									if obj[4]<=5:
										# {"feature": "Gender", "instances": 22, "metric_value": 0.0844, "depth": 10}
										if obj[3]<=0:
											# {"feature": "Children", "instances": 14, "metric_value": 0.131, "depth": 11}
											if obj[5]<=0:
												# {"feature": "Distance", "instances": 12, "metric_value": 0.15, "depth": 12}
												if obj[12]>1:
													# {"feature": "Direction_same", "instances": 10, "metric_value": 0.18, "depth": 13}
													if obj[11]<=0:
														return 'True'
													else: return 'True'
												elif obj[12]<=1:
													return 'True'
												else: return 'True'
											elif obj[5]>0:
												return 'True'
											else: return 'True'
										elif obj[3]>0:
											return 'True'
										else: return 'True'
									elif obj[4]>5:
										return 'False'
									else: return 'False'
								elif obj[7]>17:
									# {"feature": "Gender", "instances": 3, "metric_value": 0.3333, "depth": 9}
									if obj[3]>0:
										# {"feature": "Age", "instances": 2, "metric_value": 0.5, "depth": 10}
										if obj[4]<=3:
											# {"feature": "Children", "instances": 2, "metric_value": 0.5, "depth": 11}
											if obj[5]<=1:
												# {"feature": "Direction_same", "instances": 2, "metric_value": 0.5, "depth": 12}
												if obj[11]<=0:
													# {"feature": "Distance", "instances": 2, "metric_value": 0.5, "depth": 13}
													if obj[12]<=2:
														return 'False'
													else: return 'False'
												else: return 'False'
											else: return 'False'
										else: return 'False'
									elif obj[3]<=0:
										return 'False'
									else: return 'False'
								else: return 'False'
							elif obj[9]>3.0:
								return 'False'
							else: return 'False'
						else: return 'True'
					elif obj[1]<=0:
						# {"feature": "Direction_same", "instances": 47, "metric_value": 0.3225, "depth": 6}
						if obj[11]<=0:
							# {"feature": "Age", "instances": 25, "metric_value": 0.4109, "depth": 7}
							if obj[4]>1:
								# {"feature": "Occupation", "instances": 14, "metric_value": 0.4167, "depth": 8}
								if obj[7]>4:
									# {"feature": "Coffeehouse", "instances": 12, "metric_value": 0.4381, "depth": 9}
									if obj[9]>1.0:
										# {"feature": "Children", "instances": 7, "metric_value": 0.3429, "depth": 10}
										if obj[5]<=0:
											# {"feature": "Passanger", "instances": 5, "metric_value": 0.4667, "depth": 11}
											if obj[0]<=0:
												# {"feature": "Gender", "instances": 3, "metric_value": 0.3333, "depth": 12}
												if obj[3]>0:
													# {"feature": "Distance", "instances": 2, "metric_value": 0.5, "depth": 13}
													if obj[12]<=2:
														return 'False'
													else: return 'False'
												elif obj[3]<=0:
													return 'True'
												else: return 'True'
											elif obj[0]>0:
												# {"feature": "Gender", "instances": 2, "metric_value": 0.5, "depth": 12}
												if obj[3]<=0:
													# {"feature": "Distance", "instances": 2, "metric_value": 0.5, "depth": 13}
													if obj[12]<=2:
														return 'False'
													else: return 'False'
												else: return 'False'
											else: return 'False'
										elif obj[5]>0:
											return 'True'
										else: return 'True'
									elif obj[9]<=1.0:
										# {"feature": "Gender", "instances": 5, "metric_value": 0.2667, "depth": 10}
										if obj[3]<=0:
											# {"feature": "Passanger", "instances": 3, "metric_value": 0.3333, "depth": 11}
											if obj[0]>0:
												# {"feature": "Children", "instances": 2, "metric_value": 0.0, "depth": 12}
												if obj[5]<=0:
													return 'False'
												elif obj[5]>0:
													return 'True'
												else: return 'True'
											elif obj[0]<=0:
												return 'True'
											else: return 'True'
										elif obj[3]>0:
											return 'False'
										else: return 'False'
									else: return 'False'
								elif obj[7]<=4:
									return 'False'
								else: return 'False'
							elif obj[4]<=1:
								# {"feature": "Coffeehouse", "instances": 11, "metric_value": 0.2525, "depth": 8}
								if obj[9]>1.0:
									# {"feature": "Passanger", "instances": 9, "metric_value": 0.1111, "depth": 9}
									if obj[0]>0:
										return 'True'
									elif obj[0]<=0:
										# {"feature": "Gender", "instances": 2, "metric_value": 0.0, "depth": 10}
										if obj[3]<=0:
											return 'False'
										elif obj[3]>0:
											return 'True'
										else: return 'True'
									else: return 'False'
								elif obj[9]<=1.0:
									# {"feature": "Passanger", "instances": 2, "metric_value": 0.0, "depth": 9}
									if obj[0]<=0:
										return 'True'
									elif obj[0]>0:
										return 'False'
									else: return 'False'
								else: return 'True'
							else: return 'True'
						elif obj[11]>0:
							# {"feature": "Occupation", "instances": 22, "metric_value": 0.0909, "depth": 7}
							if obj[7]<=16:
								return 'True'
							elif obj[7]>16:
								# {"feature": "Age", "instances": 4, "metric_value": 0.3333, "depth": 8}
								if obj[4]<=2:
									# {"feature": "Gender", "instances": 3, "metric_value": 0.3333, "depth": 9}
									if obj[3]<=0:
										# {"feature": "Coffeehouse", "instances": 2, "metric_value": 0.0, "depth": 10}
										if obj[9]>0.0:
											return 'False'
										elif obj[9]<=0.0:
											return 'True'
										else: return 'True'
									elif obj[3]>0:
										return 'True'
									else: return 'True'
								elif obj[4]>2:
									return 'False'
								else: return 'False'
							else: return 'False'
						else: return 'True'
					else: return 'True'
				elif obj[6]<=1:
					# {"feature": "Occupation", "instances": 118, "metric_value": 0.3338, "depth": 5}
					if obj[7]>7:
						# {"feature": "Time", "instances": 64, "metric_value": 0.2462, "depth": 6}
						if obj[1]<=2:
							# {"feature": "Coffeehouse", "instances": 38, "metric_value": 0.1373, "depth": 7}
							if obj[9]<=2.0:
								# {"feature": "Age", "instances": 23, "metric_value": 0.1581, "depth": 8}
								if obj[4]<=6:
									# {"feature": "Direction_same", "instances": 22, "metric_value": 0.1212, "depth": 9}
									if obj[11]<=0:
										return 'True'
									elif obj[11]>0:
										# {"feature": "Gender", "instances": 6, "metric_value": 0.3333, "depth": 10}
										if obj[3]<=0:
											# {"feature": "Passanger", "instances": 4, "metric_value": 0.5, "depth": 11}
											if obj[0]<=1:
												# {"feature": "Children", "instances": 4, "metric_value": 0.5, "depth": 12}
												if obj[5]<=0:
													# {"feature": "Distance", "instances": 2, "metric_value": 0.5, "depth": 13}
													if obj[12]<=1:
														return 'True'
													else: return 'True'
												elif obj[5]>0:
													# {"feature": "Distance", "instances": 2, "metric_value": 0.5, "depth": 13}
													if obj[12]<=1:
														return 'True'
													else: return 'True'
												else: return 'True'
											else: return 'True'
										elif obj[3]>0:
											return 'True'
										else: return 'True'
									else: return 'True'
								elif obj[4]>6:
									return 'False'
								else: return 'False'
							elif obj[9]>2.0:
								return 'True'
							else: return 'True'
						elif obj[1]>2:
							# {"feature": "Passanger", "instances": 26, "metric_value": 0.3401, "depth": 7}
							if obj[0]<=2:
								# {"feature": "Direction_same", "instances": 19, "metric_value": 0.4145, "depth": 8}
								if obj[11]<=0:
									# {"feature": "Children", "instances": 16, "metric_value": 0.4219, "depth": 9}
									if obj[5]>0:
										# {"feature": "Coffeehouse", "instances": 8, "metric_value": 0.3571, "depth": 10}
										if obj[9]>0.0:
											# {"feature": "Distance", "instances": 7, "metric_value": 0.2381, "depth": 11}
											if obj[12]<=2:
												# {"feature": "Age", "instances": 6, "metric_value": 0.2222, "depth": 12}
												if obj[4]>0:
													# {"feature": "Gender", "instances": 3, "metric_value": 0.0, "depth": 13}
													if obj[3]>0:
														return 'False'
													elif obj[3]<=0:
														return 'True'
													else: return 'True'
												elif obj[4]<=0:
													return 'False'
												else: return 'False'
											elif obj[12]>2:
												return 'True'
											else: return 'True'
										elif obj[9]<=0.0:
											return 'True'
										else: return 'True'
									elif obj[5]<=0:
										# {"feature": "Age", "instances": 8, "metric_value": 0.3333, "depth": 10}
										if obj[4]<=6:
											# {"feature": "Coffeehouse", "instances": 6, "metric_value": 0.1667, "depth": 11}
											if obj[9]>0.0:
												return 'True'
											elif obj[9]<=0.0:
												# {"feature": "Gender", "instances": 2, "metric_value": 0.5, "depth": 12}
												if obj[3]<=0:
													# {"feature": "Distance", "instances": 2, "metric_value": 0.5, "depth": 13}
													if obj[12]<=1:
														return 'False'
													else: return 'False'
												else: return 'False'
											else: return 'False'
										elif obj[4]>6:
											# {"feature": "Gender", "instances": 2, "metric_value": 0.0, "depth": 11}
											if obj[3]>0:
												return 'True'
											elif obj[3]<=0:
												return 'False'
											else: return 'False'
										else: return 'True'
									else: return 'True'
								elif obj[11]>0:
									return 'True'
								else: return 'True'
							elif obj[0]>2:
								return 'True'
							else: return 'True'
						else: return 'True'
					elif obj[7]<=7:
						# {"feature": "Coffeehouse", "instances": 54, "metric_value": 0.3991, "depth": 6}
						if obj[9]>0.0:
							# {"feature": "Age", "instances": 49, "metric_value": 0.4281, "depth": 7}
							if obj[4]<=4:
								# {"feature": "Passanger", "instances": 41, "metric_value": 0.3847, "depth": 8}
								if obj[0]<=2:
									# {"feature": "Time", "instances": 35, "metric_value": 0.4288, "depth": 9}
									if obj[1]>0:
										# {"feature": "Direction_same", "instances": 18, "metric_value": 0.4575, "depth": 10}
										if obj[11]<=0:
											# {"feature": "Distance", "instances": 17, "metric_value": 0.4759, "depth": 11}
											if obj[12]<=2:
												# {"feature": "Gender", "instances": 11, "metric_value": 0.3697, "depth": 12}
												if obj[3]<=0:
													# {"feature": "Children", "instances": 6, "metric_value": 0.2778, "depth": 13}
													if obj[5]<=0:
														return 'True'
													else: return 'True'
												elif obj[3]>0:
													# {"feature": "Children", "instances": 5, "metric_value": 0.4667, "depth": 13}
													if obj[5]<=0:
														return 'False'
													elif obj[5]>0:
														return 'True'
													else: return 'True'
												else: return 'False'
											elif obj[12]>2:
												# {"feature": "Gender", "instances": 6, "metric_value": 0.0, "depth": 12}
												if obj[3]>0:
													return 'True'
												elif obj[3]<=0:
													return 'False'
												else: return 'False'
											else: return 'True'
										elif obj[11]>0:
											return 'False'
										else: return 'False'
									elif obj[1]<=0:
										# {"feature": "Distance", "instances": 17, "metric_value": 0.3252, "depth": 10}
										if obj[12]<=1:
											# {"feature": "Gender", "instances": 9, "metric_value": 0.1778, "depth": 11}
											if obj[3]<=0:
												# {"feature": "Children", "instances": 5, "metric_value": 0.3, "depth": 12}
												if obj[5]<=0:
													# {"feature": "Direction_same", "instances": 4, "metric_value": 0.375, "depth": 13}
													if obj[11]<=1:
														return 'True'
													else: return 'True'
												elif obj[5]>0:
													return 'True'
												else: return 'True'
											elif obj[3]>0:
												return 'True'
											else: return 'True'
										elif obj[12]>1:
											# {"feature": "Children", "instances": 8, "metric_value": 0.3571, "depth": 11}
											if obj[5]<=0:
												# {"feature": "Gender", "instances": 7, "metric_value": 0.4048, "depth": 12}
												if obj[3]<=0:
													# {"feature": "Direction_same", "instances": 4, "metric_value": 0.375, "depth": 13}
													if obj[11]<=0:
														return 'True'
													else: return 'True'
												elif obj[3]>0:
													# {"feature": "Direction_same", "instances": 3, "metric_value": 0.4444, "depth": 13}
													if obj[11]<=0:
														return 'True'
													else: return 'True'
												else: return 'True'
											elif obj[5]>0:
												return 'False'
											else: return 'False'
										else: return 'True'
									else: return 'True'
								elif obj[0]>2:
									return 'True'
								else: return 'True'
							elif obj[4]>4:
								# {"feature": "Passanger", "instances": 8, "metric_value": 0.3333, "depth": 8}
								if obj[0]<=1:
									# {"feature": "Time", "instances": 6, "metric_value": 0.2222, "depth": 9}
									if obj[1]<=1:
										# {"feature": "Direction_same", "instances": 3, "metric_value": 0.3333, "depth": 10}
										if obj[11]>0:
											# {"feature": "Gender", "instances": 2, "metric_value": 0.5, "depth": 11}
											if obj[3]<=0:
												# {"feature": "Children", "instances": 2, "metric_value": 0.5, "depth": 12}
												if obj[5]<=0:
													# {"feature": "Distance", "instances": 2, "metric_value": 0.5, "depth": 13}
													if obj[12]<=1:
														return 'True'
													else: return 'True'
												else: return 'True'
											else: return 'True'
										elif obj[11]<=0:
											return 'False'
										else: return 'False'
									elif obj[1]>1:
										return 'True'
									else: return 'True'
								elif obj[0]>1:
									return 'False'
								else: return 'False'
							else: return 'True'
						elif obj[9]<=0.0:
							return 'True'
						else: return 'True'
					else: return 'True'
				else: return 'True'
			else: return 'True'
		else: return 'True'
	else: return 'False'
