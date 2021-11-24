def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Gender, obj[4]: Age, obj[5]: Education, obj[6]: Occupation, obj[7]: Bar, obj[8]: Coffeehouse, obj[9]: Restaurant20to50, obj[10]: Direction_same, obj[11]: Distance
	# {"feature": "Coupon", "instances": 8147, "metric_value": 0.4722, "depth": 1}
	if obj[2]>1:
		# {"feature": "Coffeehouse", "instances": 5903, "metric_value": 0.4569, "depth": 2}
		if obj[8]<=1.0:
			# {"feature": "Passanger", "instances": 3018, "metric_value": 0.4857, "depth": 3}
			if obj[0]<=1:
				# {"feature": "Distance", "instances": 1928, "metric_value": 0.4872, "depth": 4}
				if obj[11]<=1:
					# {"feature": "Time", "instances": 1066, "metric_value": 0.4791, "depth": 5}
					if obj[1]>0:
						# {"feature": "Direction_same", "instances": 704, "metric_value": 0.457, "depth": 6}
						if obj[10]>0:
							# {"feature": "Occupation", "instances": 360, "metric_value": 0.4901, "depth": 7}
							if obj[6]<=20.37285734786367:
								# {"feature": "Bar", "instances": 337, "metric_value": 0.4933, "depth": 8}
								if obj[7]<=1.0:
									# {"feature": "Age", "instances": 270, "metric_value": 0.4871, "depth": 9}
									if obj[4]>0:
										# {"feature": "Restaurant20to50", "instances": 226, "metric_value": 0.4909, "depth": 10}
										if obj[9]<=2.0:
											# {"feature": "Education", "instances": 219, "metric_value": 0.4965, "depth": 11}
											if obj[5]<=3:
												# {"feature": "Gender", "instances": 193, "metric_value": 0.4987, "depth": 12}
												if obj[3]>0:
													return 'False'
												elif obj[3]<=0:
													return 'True'
												else: return 'True'
											elif obj[5]>3:
												# {"feature": "Gender", "instances": 26, "metric_value": 0.4719, "depth": 12}
												if obj[3]>0:
													return 'True'
												elif obj[3]<=0:
													return 'True'
												else: return 'True'
											else: return 'True'
										elif obj[9]>2.0:
											# {"feature": "Education", "instances": 7, "metric_value": 0.1905, "depth": 11}
											if obj[5]<=3:
												return 'True'
											elif obj[5]>3:
												# {"feature": "Gender", "instances": 3, "metric_value": 0.4444, "depth": 12}
												if obj[3]<=0:
													return 'True'
												else: return 'True'
											else: return 'True'
										else: return 'True'
									elif obj[4]<=0:
										# {"feature": "Gender", "instances": 44, "metric_value": 0.4106, "depth": 10}
										if obj[3]<=0:
											# {"feature": "Education", "instances": 24, "metric_value": 0.4365, "depth": 11}
											if obj[5]<=3:
												# {"feature": "Restaurant20to50", "instances": 21, "metric_value": 0.4714, "depth": 12}
												if obj[9]<=2.0:
													return 'True'
												elif obj[9]>2.0:
													return 'False'
												else: return 'False'
											elif obj[5]>3:
												return 'True'
											else: return 'True'
										elif obj[3]>0:
											# {"feature": "Education", "instances": 20, "metric_value": 0.3, "depth": 11}
											if obj[5]<=1:
												# {"feature": "Restaurant20to50", "instances": 16, "metric_value": 0.3667, "depth": 12}
												if obj[9]<=1.0:
													return 'True'
												elif obj[9]>1.0:
													return 'True'
												else: return 'True'
											elif obj[5]>1:
												return 'True'
											else: return 'True'
										else: return 'True'
									else: return 'True'
								elif obj[7]>1.0:
									# {"feature": "Age", "instances": 67, "metric_value": 0.4228, "depth": 9}
									if obj[4]<=4:
										# {"feature": "Restaurant20to50", "instances": 57, "metric_value": 0.4511, "depth": 10}
										if obj[9]>-1.0:
											# {"feature": "Education", "instances": 56, "metric_value": 0.4497, "depth": 11}
											if obj[5]<=2:
												# {"feature": "Gender", "instances": 54, "metric_value": 0.4542, "depth": 12}
												if obj[3]<=0:
													return 'False'
												elif obj[3]>0:
													return 'False'
												else: return 'False'
											elif obj[5]>2:
												return 'False'
											else: return 'False'
										elif obj[9]<=-1.0:
											return 'True'
										else: return 'True'
									elif obj[4]>4:
										# {"feature": "Gender", "instances": 10, "metric_value": 0.15, "depth": 10}
										if obj[3]<=0:
											return 'True'
										elif obj[3]>0:
											# {"feature": "Education", "instances": 4, "metric_value": 0.375, "depth": 11}
											if obj[5]<=0:
												# {"feature": "Restaurant20to50", "instances": 4, "metric_value": 0.375, "depth": 12}
												if obj[9]<=2.0:
													return 'True'
												else: return 'True'
											else: return 'True'
										else: return 'True'
									else: return 'True'
								else: return 'False'
							elif obj[6]>20.37285734786367:
								# {"feature": "Age", "instances": 23, "metric_value": 0.2977, "depth": 8}
								if obj[4]>2:
									# {"feature": "Gender", "instances": 13, "metric_value": 0.1026, "depth": 9}
									if obj[3]<=0:
										return 'True'
									elif obj[3]>0:
										# {"feature": "Education", "instances": 3, "metric_value": 0.3333, "depth": 10}
										if obj[5]<=0:
											# {"feature": "Bar", "instances": 2, "metric_value": 0.5, "depth": 11}
											if obj[7]<=0.0:
												# {"feature": "Restaurant20to50", "instances": 2, "metric_value": 0.5, "depth": 12}
												if obj[9]<=1.0:
													return 'True'
												else: return 'True'
											else: return 'True'
										elif obj[5]>0:
											return 'True'
										else: return 'True'
									else: return 'True'
								elif obj[4]<=2:
									# {"feature": "Gender", "instances": 10, "metric_value": 0.4167, "depth": 9}
									if obj[3]<=0:
										# {"feature": "Bar", "instances": 6, "metric_value": 0.4, "depth": 10}
										if obj[7]<=3.0:
											# {"feature": "Education", "instances": 5, "metric_value": 0.4667, "depth": 11}
											if obj[5]>0:
												# {"feature": "Restaurant20to50", "instances": 3, "metric_value": 0.4444, "depth": 12}
												if obj[9]<=1.0:
													return 'True'
												else: return 'True'
											elif obj[5]<=0:
												# {"feature": "Restaurant20to50", "instances": 2, "metric_value": 0.5, "depth": 12}
												if obj[9]<=1.0:
													return 'True'
												else: return 'True'
											else: return 'True'
										elif obj[7]>3.0:
											return 'True'
										else: return 'True'
									elif obj[3]>0:
										# {"feature": "Education", "instances": 4, "metric_value": 0.25, "depth": 10}
										if obj[5]<=0:
											# {"feature": "Bar", "instances": 2, "metric_value": 0.5, "depth": 11}
											if obj[7]<=0.0:
												# {"feature": "Restaurant20to50", "instances": 2, "metric_value": 0.5, "depth": 12}
												if obj[9]<=1.0:
													return 'False'
												else: return 'False'
											else: return 'False'
										elif obj[5]>0:
											return 'False'
										else: return 'False'
									else: return 'False'
								else: return 'False'
							else: return 'True'
						elif obj[10]<=0:
							# {"feature": "Bar", "instances": 344, "metric_value": 0.4136, "depth": 7}
							if obj[7]<=2.0:
								# {"feature": "Occupation", "instances": 314, "metric_value": 0.4005, "depth": 8}
								if obj[6]<=16.766183412132953:
									# {"feature": "Age", "instances": 296, "metric_value": 0.39, "depth": 9}
									if obj[4]<=6:
										# {"feature": "Gender", "instances": 281, "metric_value": 0.3993, "depth": 10}
										if obj[3]<=0:
											# {"feature": "Restaurant20to50", "instances": 146, "metric_value": 0.4353, "depth": 11}
											if obj[9]>-1.0:
												# {"feature": "Education", "instances": 142, "metric_value": 0.4443, "depth": 12}
												if obj[5]<=2:
													return 'True'
												elif obj[5]>2:
													return 'True'
												else: return 'True'
											elif obj[9]<=-1.0:
												return 'True'
											else: return 'True'
										elif obj[3]>0:
											# {"feature": "Education", "instances": 135, "metric_value": 0.3526, "depth": 11}
											if obj[5]<=3:
												# {"feature": "Restaurant20to50", "instances": 122, "metric_value": 0.3601, "depth": 12}
												if obj[9]>-1.0:
													return 'True'
												elif obj[9]<=-1.0:
													return 'True'
												else: return 'True'
											elif obj[5]>3:
												# {"feature": "Restaurant20to50", "instances": 13, "metric_value": 0.2393, "depth": 12}
												if obj[9]<=1.0:
													return 'True'
												elif obj[9]>1.0:
													return 'True'
												else: return 'True'
											else: return 'True'
										else: return 'True'
									elif obj[4]>6:
										# {"feature": "Education", "instances": 15, "metric_value": 0.1067, "depth": 10}
										if obj[5]>0:
											return 'True'
										elif obj[5]<=0:
											# {"feature": "Restaurant20to50", "instances": 5, "metric_value": 0.2, "depth": 11}
											if obj[9]>1.0:
												return 'True'
											elif obj[9]<=1.0:
												# {"feature": "Gender", "instances": 2, "metric_value": 0.5, "depth": 12}
												if obj[3]<=1:
													return 'True'
												else: return 'True'
											else: return 'True'
										else: return 'True'
									else: return 'True'
								elif obj[6]>16.766183412132953:
									# {"feature": "Restaurant20to50", "instances": 18, "metric_value": 0.3571, "depth": 9}
									if obj[9]>0.0:
										# {"feature": "Age", "instances": 14, "metric_value": 0.4048, "depth": 10}
										if obj[4]<=2:
											# {"feature": "Education", "instances": 8, "metric_value": 0.4286, "depth": 11}
											if obj[5]<=2:
												# {"feature": "Gender", "instances": 7, "metric_value": 0.4857, "depth": 12}
												if obj[3]<=0:
													return 'True'
												elif obj[3]>0:
													return 'False'
												else: return 'False'
											elif obj[5]>2:
												return 'False'
											else: return 'False'
										elif obj[4]>2:
											# {"feature": "Gender", "instances": 6, "metric_value": 0.2222, "depth": 11}
											if obj[3]<=0:
												# {"feature": "Education", "instances": 3, "metric_value": 0.0, "depth": 12}
												if obj[5]<=0:
													return 'True'
												elif obj[5]>0:
													return 'False'
												else: return 'False'
											elif obj[3]>0:
												return 'True'
											else: return 'True'
										else: return 'True'
									elif obj[9]<=0.0:
										return 'False'
									else: return 'False'
								else: return 'True'
							elif obj[7]>2.0:
								# {"feature": "Age", "instances": 30, "metric_value": 0.3627, "depth": 8}
								if obj[4]>0:
									# {"feature": "Education", "instances": 25, "metric_value": 0.3476, "depth": 9}
									if obj[5]>0:
										# {"feature": "Gender", "instances": 17, "metric_value": 0.249, "depth": 10}
										if obj[3]<=0:
											# {"feature": "Occupation", "instances": 12, "metric_value": 0.1111, "depth": 11}
											if obj[6]>1:
												return 'True'
											elif obj[6]<=1:
												# {"feature": "Restaurant20to50", "instances": 3, "metric_value": 0.0, "depth": 12}
												if obj[9]>1.0:
													return 'True'
												elif obj[9]<=1.0:
													return 'False'
												else: return 'False'
											else: return 'True'
										elif obj[3]>0:
											# {"feature": "Restaurant20to50", "instances": 5, "metric_value": 0.2667, "depth": 11}
											if obj[9]>0.0:
												# {"feature": "Occupation", "instances": 3, "metric_value": 0.3333, "depth": 12}
												if obj[6]<=2:
													return 'True'
												elif obj[6]>2:
													return 'False'
												else: return 'False'
											elif obj[9]<=0.0:
												return 'True'
											else: return 'True'
										else: return 'True'
									elif obj[5]<=0:
										# {"feature": "Gender", "instances": 8, "metric_value": 0.3667, "depth": 10}
										if obj[3]<=0:
											# {"feature": "Occupation", "instances": 5, "metric_value": 0.2667, "depth": 11}
											if obj[6]>4:
												# {"feature": "Restaurant20to50", "instances": 3, "metric_value": 0.4444, "depth": 12}
												if obj[9]<=1.0:
													return 'False'
												else: return 'False'
											elif obj[6]<=4:
												return 'False'
											else: return 'False'
										elif obj[3]>0:
											# {"feature": "Occupation", "instances": 3, "metric_value": 0.4444, "depth": 11}
											if obj[6]<=12:
												# {"feature": "Restaurant20to50", "instances": 3, "metric_value": 0.4444, "depth": 12}
												if obj[9]<=2.0:
													return 'True'
												else: return 'True'
											else: return 'True'
										else: return 'True'
									else: return 'False'
								elif obj[4]<=0:
									return 'False'
								else: return 'False'
							else: return 'True'
						else: return 'True'
					elif obj[1]<=0:
						# {"feature": "Restaurant20to50", "instances": 362, "metric_value": 0.4901, "depth": 6}
						if obj[9]<=2.0:
							# {"feature": "Gender", "instances": 355, "metric_value": 0.491, "depth": 7}
							if obj[3]>0:
								# {"feature": "Education", "instances": 182, "metric_value": 0.4812, "depth": 8}
								if obj[5]<=3:
									# {"feature": "Age", "instances": 161, "metric_value": 0.4797, "depth": 9}
									if obj[4]>1:
										# {"feature": "Occupation", "instances": 90, "metric_value": 0.4552, "depth": 10}
										if obj[6]<=20:
											# {"feature": "Bar", "instances": 87, "metric_value": 0.4619, "depth": 11}
											if obj[7]<=2.0:
												# {"feature": "Direction_same", "instances": 86, "metric_value": 0.4671, "depth": 12}
												if obj[10]<=0:
													return 'False'
												elif obj[10]>0:
													return 'False'
												else: return 'False'
											elif obj[7]>2.0:
												return 'True'
											else: return 'True'
										elif obj[6]>20:
											return 'False'
										else: return 'False'
									elif obj[4]<=1:
										# {"feature": "Occupation", "instances": 71, "metric_value": 0.4712, "depth": 10}
										if obj[6]<=6:
											# {"feature": "Direction_same", "instances": 44, "metric_value": 0.4042, "depth": 11}
											if obj[10]<=0:
												# {"feature": "Bar", "instances": 26, "metric_value": 0.3399, "depth": 12}
												if obj[7]>0.0:
													return 'False'
												elif obj[7]<=0.0:
													return 'False'
												else: return 'False'
											elif obj[10]>0:
												# {"feature": "Bar", "instances": 18, "metric_value": 0.3981, "depth": 12}
												if obj[7]<=1.0:
													return 'True'
												elif obj[7]>1.0:
													return 'False'
												else: return 'False'
											else: return 'True'
										elif obj[6]>6:
											# {"feature": "Bar", "instances": 27, "metric_value": 0.4532, "depth": 11}
											if obj[7]<=1.0:
												# {"feature": "Direction_same", "instances": 22, "metric_value": 0.4817, "depth": 12}
												if obj[10]<=0:
													return 'True'
												elif obj[10]>0:
													return 'True'
												else: return 'True'
											elif obj[7]>1.0:
												# {"feature": "Direction_same", "instances": 5, "metric_value": 0.3, "depth": 12}
												if obj[10]>0:
													return 'True'
												elif obj[10]<=0:
													return 'True'
												else: return 'True'
											else: return 'True'
										else: return 'True'
									else: return 'False'
								elif obj[5]>3:
									# {"feature": "Age", "instances": 21, "metric_value": 0.375, "depth": 9}
									if obj[4]<=4:
										# {"feature": "Occupation", "instances": 16, "metric_value": 0.4271, "depth": 10}
										if obj[6]>1:
											# {"feature": "Bar", "instances": 12, "metric_value": 0.3333, "depth": 11}
											if obj[7]>0.0:
												# {"feature": "Direction_same", "instances": 8, "metric_value": 0.5, "depth": 12}
												if obj[10]<=0:
													return 'True'
												elif obj[10]>0:
													return 'False'
												else: return 'False'
											elif obj[7]<=0.0:
												return 'True'
											else: return 'True'
										elif obj[6]<=1:
											# {"feature": "Bar", "instances": 4, "metric_value": 0.3333, "depth": 11}
											if obj[7]>0.0:
												# {"feature": "Direction_same", "instances": 3, "metric_value": 0.3333, "depth": 12}
												if obj[10]>0:
													return 'False'
												elif obj[10]<=0:
													return 'False'
												else: return 'False'
											elif obj[7]<=0.0:
												return 'False'
											else: return 'False'
										else: return 'False'
									elif obj[4]>4:
										return 'True'
									else: return 'True'
								else: return 'True'
							elif obj[3]<=0:
								# {"feature": "Education", "instances": 173, "metric_value": 0.4646, "depth": 8}
								if obj[5]>1:
									# {"feature": "Bar", "instances": 99, "metric_value": 0.4817, "depth": 9}
									if obj[7]<=2.0:
										# {"feature": "Occupation", "instances": 92, "metric_value": 0.4849, "depth": 10}
										if obj[6]>4:
											# {"feature": "Age", "instances": 78, "metric_value": 0.4875, "depth": 11}
											if obj[4]>0:
												# {"feature": "Direction_same", "instances": 60, "metric_value": 0.4852, "depth": 12}
												if obj[10]<=0:
													return 'False'
												elif obj[10]>0:
													return 'False'
												else: return 'False'
											elif obj[4]<=0:
												# {"feature": "Direction_same", "instances": 18, "metric_value": 0.4691, "depth": 12}
												if obj[10]>0:
													return 'True'
												elif obj[10]<=0:
													return 'True'
												else: return 'True'
											else: return 'True'
										elif obj[6]<=4:
											# {"feature": "Age", "instances": 14, "metric_value": 0.3393, "depth": 11}
											if obj[4]<=4:
												# {"feature": "Direction_same", "instances": 8, "metric_value": 0.1875, "depth": 12}
												if obj[10]>0:
													return 'True'
												elif obj[10]<=0:
													return 'True'
												else: return 'True'
											elif obj[4]>4:
												# {"feature": "Direction_same", "instances": 6, "metric_value": 0.4, "depth": 12}
												if obj[10]<=0:
													return 'True'
												elif obj[10]>0:
													return 'False'
												else: return 'False'
											else: return 'False'
										else: return 'True'
									elif obj[7]>2.0:
										# {"feature": "Age", "instances": 7, "metric_value": 0.2143, "depth": 10}
										if obj[4]<=1:
											# {"feature": "Occupation", "instances": 4, "metric_value": 0.3333, "depth": 11}
											if obj[6]>1:
												# {"feature": "Direction_same", "instances": 3, "metric_value": 0.3333, "depth": 12}
												if obj[10]<=0:
													return 'True'
												elif obj[10]>0:
													return 'False'
												else: return 'False'
											elif obj[6]<=1:
												return 'False'
											else: return 'False'
										elif obj[4]>1:
											return 'False'
										else: return 'False'
									else: return 'False'
								elif obj[5]<=1:
									# {"feature": "Occupation", "instances": 74, "metric_value": 0.3902, "depth": 9}
									if obj[6]<=18:
										# {"feature": "Age", "instances": 64, "metric_value": 0.4418, "depth": 10}
										if obj[4]<=4:
											# {"feature": "Bar", "instances": 50, "metric_value": 0.4653, "depth": 11}
											if obj[7]>-1.0:
												# {"feature": "Direction_same", "instances": 49, "metric_value": 0.4714, "depth": 12}
												if obj[10]<=0:
													return 'True'
												elif obj[10]>0:
													return 'True'
												else: return 'True'
											elif obj[7]<=-1.0:
												return 'True'
											else: return 'True'
										elif obj[4]>4:
											# {"feature": "Bar", "instances": 14, "metric_value": 0.2251, "depth": 11}
											if obj[7]<=1.0:
												# {"feature": "Direction_same", "instances": 11, "metric_value": 0.1515, "depth": 12}
												if obj[10]>0:
													return 'True'
												elif obj[10]<=0:
													return 'True'
												else: return 'True'
											elif obj[7]>1.0:
												# {"feature": "Direction_same", "instances": 3, "metric_value": 0.4444, "depth": 12}
												if obj[10]<=0:
													return 'False'
												else: return 'False'
											else: return 'False'
										else: return 'True'
									elif obj[6]>18:
										return 'True'
									else: return 'True'
								else: return 'True'
							else: return 'True'
						elif obj[9]>2.0:
							return 'True'
						else: return 'True'
					else: return 'True'
				elif obj[11]>1:
					# {"feature": "Time", "instances": 862, "metric_value": 0.4813, "depth": 5}
					if obj[1]<=3:
						# {"feature": "Direction_same", "instances": 705, "metric_value": 0.4721, "depth": 6}
						if obj[10]<=0:
							# {"feature": "Education", "instances": 528, "metric_value": 0.4597, "depth": 7}
							if obj[5]<=3:
								# {"feature": "Bar", "instances": 481, "metric_value": 0.4536, "depth": 8}
								if obj[7]<=2.0:
									# {"feature": "Gender", "instances": 450, "metric_value": 0.4577, "depth": 9}
									if obj[3]>0:
										# {"feature": "Restaurant20to50", "instances": 233, "metric_value": 0.4326, "depth": 10}
										if obj[9]<=3.0:
											# {"feature": "Age", "instances": 232, "metric_value": 0.4311, "depth": 11}
											if obj[4]>1:
												# {"feature": "Occupation", "instances": 143, "metric_value": 0.3977, "depth": 12}
												if obj[6]>1:
													return 'False'
												elif obj[6]<=1:
													return 'False'
												else: return 'False'
											elif obj[4]<=1:
												# {"feature": "Occupation", "instances": 89, "metric_value": 0.4621, "depth": 12}
												if obj[6]<=12:
													return 'False'
												elif obj[6]>12:
													return 'False'
												else: return 'False'
											else: return 'False'
										elif obj[9]>3.0:
											return 'True'
										else: return 'True'
									elif obj[3]<=0:
										# {"feature": "Age", "instances": 217, "metric_value": 0.4701, "depth": 10}
										if obj[4]<=6:
											# {"feature": "Occupation", "instances": 206, "metric_value": 0.483, "depth": 11}
											if obj[6]<=23.401594048862115:
												# {"feature": "Restaurant20to50", "instances": 204, "metric_value": 0.4859, "depth": 12}
												if obj[9]>-1.0:
													return 'False'
												elif obj[9]<=-1.0:
													return 'False'
												else: return 'False'
											elif obj[6]>23.401594048862115:
												return 'False'
											else: return 'False'
										elif obj[4]>6:
											# {"feature": "Occupation", "instances": 11, "metric_value": 0.1364, "depth": 11}
											if obj[6]<=11:
												return 'False'
											elif obj[6]>11:
												# {"feature": "Restaurant20to50", "instances": 4, "metric_value": 0.25, "depth": 12}
												if obj[9]<=0.0:
													return 'False'
												elif obj[9]>0.0:
													return 'False'
												else: return 'False'
											else: return 'False'
										else: return 'False'
									else: return 'False'
								elif obj[7]>2.0:
									# {"feature": "Occupation", "instances": 31, "metric_value": 0.3387, "depth": 9}
									if obj[6]<=17:
										# {"feature": "Age", "instances": 28, "metric_value": 0.3704, "depth": 10}
										if obj[4]<=4:
											# {"feature": "Restaurant20to50", "instances": 27, "metric_value": 0.3792, "depth": 11}
											if obj[9]>0.0:
												# {"feature": "Gender", "instances": 21, "metric_value": 0.3968, "depth": 12}
												if obj[3]<=0:
													return 'False'
												elif obj[3]>0:
													return 'False'
												else: return 'False'
											elif obj[9]<=0.0:
												# {"feature": "Gender", "instances": 6, "metric_value": 0.1667, "depth": 12}
												if obj[3]<=0:
													return 'False'
												elif obj[3]>0:
													return 'False'
												else: return 'False'
											else: return 'False'
										elif obj[4]>4:
											return 'False'
										else: return 'False'
									elif obj[6]>17:
										return 'False'
									else: return 'False'
								else: return 'False'
							elif obj[5]>3:
								# {"feature": "Age", "instances": 47, "metric_value": 0.4763, "depth": 8}
								if obj[4]<=4:
									# {"feature": "Restaurant20to50", "instances": 39, "metric_value": 0.4657, "depth": 9}
									if obj[9]>-1.0:
										# {"feature": "Bar", "instances": 37, "metric_value": 0.4556, "depth": 10}
										if obj[7]<=1.0:
											# {"feature": "Occupation", "instances": 28, "metric_value": 0.4219, "depth": 11}
											if obj[6]<=7:
												# {"feature": "Gender", "instances": 19, "metric_value": 0.3872, "depth": 12}
												if obj[3]<=0:
													return 'True'
												elif obj[3]>0:
													return 'True'
												else: return 'True'
											elif obj[6]>7:
												# {"feature": "Gender", "instances": 9, "metric_value": 0.4444, "depth": 12}
												if obj[3]>0:
													return 'False'
												elif obj[3]<=0:
													return 'False'
												else: return 'False'
											else: return 'False'
										elif obj[7]>1.0:
											# {"feature": "Occupation", "instances": 9, "metric_value": 0.2667, "depth": 11}
											if obj[6]>9:
												# {"feature": "Gender", "instances": 5, "metric_value": 0.48, "depth": 12}
												if obj[3]<=0:
													return 'True'
												else: return 'True'
											elif obj[6]<=9:
												return 'False'
											else: return 'False'
										else: return 'False'
									elif obj[9]<=-1.0:
										return 'False'
									else: return 'False'
								elif obj[4]>4:
									# {"feature": "Occupation", "instances": 8, "metric_value": 0.3, "depth": 9}
									if obj[6]<=1:
										# {"feature": "Gender", "instances": 5, "metric_value": 0.48, "depth": 10}
										if obj[3]<=1:
											# {"feature": "Bar", "instances": 5, "metric_value": 0.48, "depth": 11}
											if obj[7]<=0.0:
												# {"feature": "Restaurant20to50", "instances": 5, "metric_value": 0.48, "depth": 12}
												if obj[9]<=0.0:
													return 'False'
												else: return 'False'
											else: return 'False'
										else: return 'False'
									elif obj[6]>1:
										return 'False'
									else: return 'False'
								else: return 'False'
							else: return 'False'
						elif obj[10]>0:
							# {"feature": "Education", "instances": 177, "metric_value": 0.4858, "depth": 7}
							if obj[5]<=2:
								# {"feature": "Occupation", "instances": 144, "metric_value": 0.4859, "depth": 8}
								if obj[6]<=14.164944200311755:
									# {"feature": "Bar", "instances": 123, "metric_value": 0.4902, "depth": 9}
									if obj[7]>-1.0:
										# {"feature": "Restaurant20to50", "instances": 121, "metric_value": 0.4909, "depth": 10}
										if obj[9]<=2.0:
											# {"feature": "Age", "instances": 119, "metric_value": 0.4941, "depth": 11}
											if obj[4]>0:
												# {"feature": "Gender", "instances": 93, "metric_value": 0.4999, "depth": 12}
												if obj[3]<=0:
													return 'False'
												elif obj[3]>0:
													return 'False'
												else: return 'False'
											elif obj[4]<=0:
												# {"feature": "Gender", "instances": 26, "metric_value": 0.3669, "depth": 12}
												if obj[3]<=0:
													return 'True'
												elif obj[3]>0:
													return 'False'
												else: return 'False'
											else: return 'True'
										elif obj[9]>2.0:
											return 'True'
										else: return 'True'
									elif obj[7]<=-1.0:
										return 'False'
									else: return 'False'
								elif obj[6]>14.164944200311755:
									# {"feature": "Bar", "instances": 21, "metric_value": 0.3429, "depth": 9}
									if obj[7]>0.0:
										# {"feature": "Restaurant20to50", "instances": 15, "metric_value": 0.3636, "depth": 10}
										if obj[9]<=1.0:
											# {"feature": "Age", "instances": 11, "metric_value": 0.3636, "depth": 11}
											if obj[4]<=4:
												# {"feature": "Gender", "instances": 9, "metric_value": 0.4, "depth": 12}
												if obj[3]>0:
													return 'False'
												elif obj[3]<=0:
													return 'True'
												else: return 'True'
											elif obj[4]>4:
												return 'True'
											else: return 'True'
										elif obj[9]>1.0:
											return 'True'
										else: return 'True'
									elif obj[7]<=0.0:
										return 'True'
									else: return 'True'
								else: return 'True'
							elif obj[5]>2:
								# {"feature": "Restaurant20to50", "instances": 33, "metric_value": 0.3663, "depth": 8}
								if obj[9]<=1.0:
									# {"feature": "Occupation", "instances": 26, "metric_value": 0.3067, "depth": 9}
									if obj[6]>3:
										# {"feature": "Age", "instances": 17, "metric_value": 0.1925, "depth": 10}
										if obj[4]>1:
											# {"feature": "Bar", "instances": 11, "metric_value": 0.2922, "depth": 11}
											if obj[7]>0.0:
												# {"feature": "Gender", "instances": 7, "metric_value": 0.2286, "depth": 12}
												if obj[3]<=0:
													return 'False'
												elif obj[3]>0:
													return 'False'
												else: return 'False'
											elif obj[7]<=0.0:
												# {"feature": "Gender", "instances": 4, "metric_value": 0.3333, "depth": 12}
												if obj[3]>0:
													return 'False'
												elif obj[3]<=0:
													return 'False'
												else: return 'False'
											else: return 'False'
										elif obj[4]<=1:
											return 'False'
										else: return 'False'
									elif obj[6]<=3:
										# {"feature": "Age", "instances": 9, "metric_value": 0.4444, "depth": 10}
										if obj[4]>1:
											# {"feature": "Bar", "instances": 8, "metric_value": 0.4286, "depth": 11}
											if obj[7]<=0.0:
												# {"feature": "Gender", "instances": 7, "metric_value": 0.4857, "depth": 12}
												if obj[3]>0:
													return 'False'
												elif obj[3]<=0:
													return 'False'
												else: return 'False'
											elif obj[7]>0.0:
												return 'True'
											else: return 'True'
										elif obj[4]<=1:
											return 'False'
										else: return 'False'
									else: return 'False'
								elif obj[9]>1.0:
									# {"feature": "Age", "instances": 7, "metric_value": 0.2381, "depth": 9}
									if obj[4]>0:
										# {"feature": "Gender", "instances": 6, "metric_value": 0.1667, "depth": 10}
										if obj[3]<=0:
											return 'True'
										elif obj[3]>0:
											# {"feature": "Occupation", "instances": 2, "metric_value": 0.0, "depth": 11}
											if obj[6]>12:
												return 'True'
											elif obj[6]<=12:
												return 'False'
											else: return 'False'
										else: return 'True'
									elif obj[4]<=0:
										return 'False'
									else: return 'False'
								else: return 'True'
							else: return 'False'
						else: return 'True'
					elif obj[1]>3:
						# {"feature": "Age", "instances": 157, "metric_value": 0.4687, "depth": 6}
						if obj[4]<=4:
							# {"feature": "Occupation", "instances": 126, "metric_value": 0.4834, "depth": 7}
							if obj[6]<=8.73015873015873:
								# {"feature": "Bar", "instances": 67, "metric_value": 0.4636, "depth": 8}
								if obj[7]<=3.0:
									# {"feature": "Education", "instances": 66, "metric_value": 0.4657, "depth": 9}
									if obj[5]<=1:
										# {"feature": "Restaurant20to50", "instances": 36, "metric_value": 0.419, "depth": 10}
										if obj[9]>-1.0:
											# {"feature": "Gender", "instances": 35, "metric_value": 0.431, "depth": 11}
											if obj[3]>0:
												# {"feature": "Direction_same", "instances": 19, "metric_value": 0.4321, "depth": 12}
												if obj[10]<=0:
													return 'True'
												else: return 'True'
											elif obj[3]<=0:
												# {"feature": "Direction_same", "instances": 16, "metric_value": 0.4297, "depth": 12}
												if obj[10]<=0:
													return 'True'
												else: return 'True'
											else: return 'True'
										elif obj[9]<=-1.0:
											return 'False'
										else: return 'False'
									elif obj[5]>1:
										# {"feature": "Restaurant20to50", "instances": 30, "metric_value": 0.4494, "depth": 10}
										if obj[9]>0.0:
											# {"feature": "Gender", "instances": 27, "metric_value": 0.4937, "depth": 11}
											if obj[3]<=0:
												# {"feature": "Direction_same", "instances": 20, "metric_value": 0.495, "depth": 12}
												if obj[10]<=0:
													return 'True'
												else: return 'True'
											elif obj[3]>0:
												# {"feature": "Direction_same", "instances": 7, "metric_value": 0.4898, "depth": 12}
												if obj[10]<=0:
													return 'False'
												else: return 'False'
											else: return 'False'
										elif obj[9]<=0.0:
											return 'True'
										else: return 'True'
									else: return 'True'
								elif obj[7]>3.0:
									return 'False'
								else: return 'False'
							elif obj[6]>8.73015873015873:
								# {"feature": "Bar", "instances": 59, "metric_value": 0.4588, "depth": 8}
								if obj[7]<=1.0:
									# {"feature": "Gender", "instances": 42, "metric_value": 0.458, "depth": 9}
									if obj[3]>0:
										# {"feature": "Restaurant20to50", "instances": 21, "metric_value": 0.3556, "depth": 10}
										if obj[9]<=1.0:
											# {"feature": "Education", "instances": 15, "metric_value": 0.497, "depth": 11}
											if obj[5]>1:
												# {"feature": "Direction_same", "instances": 11, "metric_value": 0.4959, "depth": 12}
												if obj[10]<=0:
													return 'True'
												else: return 'True'
											elif obj[5]<=1:
												# {"feature": "Direction_same", "instances": 4, "metric_value": 0.5, "depth": 12}
												if obj[10]<=0:
													return 'False'
												else: return 'False'
											else: return 'False'
										elif obj[9]>1.0:
											return 'False'
										else: return 'False'
									elif obj[3]<=0:
										# {"feature": "Education", "instances": 21, "metric_value": 0.4074, "depth": 10}
										if obj[5]<=2:
											# {"feature": "Restaurant20to50", "instances": 18, "metric_value": 0.4375, "depth": 11}
											if obj[9]<=1.0:
												# {"feature": "Direction_same", "instances": 16, "metric_value": 0.4922, "depth": 12}
												if obj[10]<=0:
													return 'True'
												else: return 'True'
											elif obj[9]>1.0:
												return 'True'
											else: return 'True'
										elif obj[5]>2:
											return 'True'
										else: return 'True'
									else: return 'True'
								elif obj[7]>1.0:
									# {"feature": "Restaurant20to50", "instances": 17, "metric_value": 0.3137, "depth": 9}
									if obj[9]<=1.0:
										# {"feature": "Education", "instances": 12, "metric_value": 0.4167, "depth": 10}
										if obj[5]<=0:
											# {"feature": "Gender", "instances": 8, "metric_value": 0.375, "depth": 11}
											if obj[3]<=0:
												# {"feature": "Direction_same", "instances": 8, "metric_value": 0.375, "depth": 12}
												if obj[10]<=0:
													return 'False'
												else: return 'False'
											else: return 'False'
										elif obj[5]>0:
											# {"feature": "Gender", "instances": 4, "metric_value": 0.5, "depth": 11}
											if obj[3]<=0:
												# {"feature": "Direction_same", "instances": 4, "metric_value": 0.5, "depth": 12}
												if obj[10]<=0:
													return 'False'
												else: return 'False'
											else: return 'False'
										else: return 'False'
									elif obj[9]>1.0:
										return 'False'
									else: return 'False'
								else: return 'False'
							else: return 'False'
						elif obj[4]>4:
							# {"feature": "Occupation", "instances": 31, "metric_value": 0.28, "depth": 7}
							if obj[6]>4:
								# {"feature": "Bar", "instances": 24, "metric_value": 0.1667, "depth": 8}
								if obj[7]<=0.0:
									return 'True'
								elif obj[7]>0.0:
									# {"feature": "Education", "instances": 9, "metric_value": 0.3333, "depth": 9}
									if obj[5]<=2:
										# {"feature": "Restaurant20to50", "instances": 6, "metric_value": 0.25, "depth": 10}
										if obj[9]<=1.0:
											# {"feature": "Gender", "instances": 4, "metric_value": 0.375, "depth": 11}
											if obj[3]<=0:
												# {"feature": "Direction_same", "instances": 4, "metric_value": 0.375, "depth": 12}
												if obj[10]<=0:
													return 'False'
												else: return 'False'
											else: return 'False'
										elif obj[9]>1.0:
											return 'True'
										else: return 'True'
									elif obj[5]>2:
										return 'True'
									else: return 'True'
								else: return 'True'
							elif obj[6]<=4:
								# {"feature": "Education", "instances": 7, "metric_value": 0.2286, "depth": 8}
								if obj[5]>0:
									# {"feature": "Gender", "instances": 5, "metric_value": 0.2, "depth": 9}
									if obj[3]<=0:
										return 'False'
									elif obj[3]>0:
										# {"feature": "Restaurant20to50", "instances": 2, "metric_value": 0.0, "depth": 10}
										if obj[9]>1.0:
											return 'False'
										elif obj[9]<=1.0:
											return 'True'
										else: return 'True'
									else: return 'False'
								elif obj[5]<=0:
									return 'True'
								else: return 'True'
							else: return 'False'
						else: return 'True'
					else: return 'True'
				else: return 'False'
			elif obj[0]>1:
				# {"feature": "Occupation", "instances": 1090, "metric_value": 0.458, "depth": 4}
				if obj[6]>1.7265574939131305:
					# {"feature": "Distance", "instances": 900, "metric_value": 0.469, "depth": 5}
					if obj[11]>1:
						# {"feature": "Time", "instances": 600, "metric_value": 0.4548, "depth": 6}
						if obj[1]>0:
							# {"feature": "Education", "instances": 477, "metric_value": 0.4657, "depth": 7}
							if obj[5]>1:
								# {"feature": "Age", "instances": 249, "metric_value": 0.4794, "depth": 8}
								if obj[4]<=2:
									# {"feature": "Bar", "instances": 144, "metric_value": 0.4592, "depth": 9}
									if obj[7]<=0.0:
										# {"feature": "Restaurant20to50", "instances": 93, "metric_value": 0.4782, "depth": 10}
										if obj[9]<=1.0:
											# {"feature": "Gender", "instances": 71, "metric_value": 0.4908, "depth": 11}
											if obj[3]>0:
												# {"feature": "Direction_same", "instances": 37, "metric_value": 0.4967, "depth": 12}
												if obj[10]<=0:
													return 'True'
												else: return 'True'
											elif obj[3]<=0:
												# {"feature": "Direction_same", "instances": 34, "metric_value": 0.4844, "depth": 12}
												if obj[10]<=0:
													return 'True'
												else: return 'True'
											else: return 'True'
										elif obj[9]>1.0:
											# {"feature": "Gender", "instances": 22, "metric_value": 0.4227, "depth": 11}
											if obj[3]<=0:
												# {"feature": "Direction_same", "instances": 12, "metric_value": 0.375, "depth": 12}
												if obj[10]<=0:
													return 'True'
												else: return 'True'
											elif obj[3]>0:
												# {"feature": "Direction_same", "instances": 10, "metric_value": 0.48, "depth": 12}
												if obj[10]<=0:
													return 'True'
												else: return 'True'
											else: return 'True'
										else: return 'True'
									elif obj[7]>0.0:
										# {"feature": "Restaurant20to50", "instances": 51, "metric_value": 0.3908, "depth": 10}
										if obj[9]>0.0:
											# {"feature": "Gender", "instances": 44, "metric_value": 0.3727, "depth": 11}
											if obj[3]<=0:
												# {"feature": "Direction_same", "instances": 23, "metric_value": 0.3403, "depth": 12}
												if obj[10]<=0:
													return 'True'
												else: return 'True'
											elif obj[3]>0:
												# {"feature": "Direction_same", "instances": 21, "metric_value": 0.4082, "depth": 12}
												if obj[10]<=0:
													return 'True'
												else: return 'True'
											else: return 'True'
										elif obj[9]<=0.0:
											# {"feature": "Gender", "instances": 7, "metric_value": 0.4762, "depth": 11}
											if obj[3]>0:
												# {"feature": "Direction_same", "instances": 4, "metric_value": 0.5, "depth": 12}
												if obj[10]<=0:
													return 'True'
												else: return 'True'
											elif obj[3]<=0:
												# {"feature": "Direction_same", "instances": 3, "metric_value": 0.4444, "depth": 12}
												if obj[10]<=0:
													return 'False'
												else: return 'False'
											else: return 'False'
										else: return 'False'
									else: return 'True'
								elif obj[4]>2:
									# {"feature": "Bar", "instances": 105, "metric_value": 0.4819, "depth": 9}
									if obj[7]>0.0:
										# {"feature": "Gender", "instances": 68, "metric_value": 0.4905, "depth": 10}
										if obj[3]<=0:
											# {"feature": "Restaurant20to50", "instances": 39, "metric_value": 0.4656, "depth": 11}
											if obj[9]<=2.0:
												# {"feature": "Direction_same", "instances": 38, "metric_value": 0.4778, "depth": 12}
												if obj[10]<=0:
													return 'False'
												else: return 'False'
											elif obj[9]>2.0:
												return 'True'
											else: return 'True'
										elif obj[3]>0:
											# {"feature": "Restaurant20to50", "instances": 29, "metric_value": 0.47, "depth": 11}
											if obj[9]>1.0:
												# {"feature": "Direction_same", "instances": 15, "metric_value": 0.48, "depth": 12}
												if obj[10]<=0:
													return 'False'
												else: return 'False'
											elif obj[9]<=1.0:
												# {"feature": "Direction_same", "instances": 14, "metric_value": 0.4592, "depth": 12}
												if obj[10]<=0:
													return 'True'
												else: return 'True'
											else: return 'True'
										else: return 'True'
									elif obj[7]<=0.0:
										# {"feature": "Gender", "instances": 37, "metric_value": 0.4401, "depth": 10}
										if obj[3]<=0:
											# {"feature": "Restaurant20to50", "instances": 24, "metric_value": 0.4778, "depth": 11}
											if obj[9]<=1.0:
												# {"feature": "Direction_same", "instances": 15, "metric_value": 0.4978, "depth": 12}
												if obj[10]<=0:
													return 'True'
												else: return 'True'
											elif obj[9]>1.0:
												# {"feature": "Direction_same", "instances": 9, "metric_value": 0.4444, "depth": 12}
												if obj[10]<=0:
													return 'True'
												else: return 'True'
											else: return 'True'
										elif obj[3]>0:
											# {"feature": "Restaurant20to50", "instances": 13, "metric_value": 0.348, "depth": 11}
											if obj[9]>0.0:
												# {"feature": "Direction_same", "instances": 7, "metric_value": 0.4082, "depth": 12}
												if obj[10]<=0:
													return 'True'
												else: return 'True'
											elif obj[9]<=0.0:
												# {"feature": "Direction_same", "instances": 6, "metric_value": 0.2778, "depth": 12}
												if obj[10]<=0:
													return 'True'
												else: return 'True'
											else: return 'True'
										else: return 'True'
									else: return 'True'
								else: return 'True'
							elif obj[5]<=1:
								# {"feature": "Bar", "instances": 228, "metric_value": 0.4389, "depth": 8}
								if obj[7]<=0.0:
									# {"feature": "Restaurant20to50", "instances": 114, "metric_value": 0.4611, "depth": 9}
									if obj[9]>0.0:
										# {"feature": "Age", "instances": 77, "metric_value": 0.4798, "depth": 10}
										if obj[4]>0:
											# {"feature": "Gender", "instances": 68, "metric_value": 0.4821, "depth": 11}
											if obj[3]>0:
												# {"feature": "Direction_same", "instances": 44, "metric_value": 0.4742, "depth": 12}
												if obj[10]<=0:
													return 'True'
												else: return 'True'
											elif obj[3]<=0:
												# {"feature": "Direction_same", "instances": 24, "metric_value": 0.4965, "depth": 12}
												if obj[10]<=0:
													return 'True'
												else: return 'True'
											else: return 'True'
										elif obj[4]<=0:
											# {"feature": "Gender", "instances": 9, "metric_value": 0.3333, "depth": 11}
											if obj[3]<=0:
												# {"feature": "Direction_same", "instances": 6, "metric_value": 0.2778, "depth": 12}
												if obj[10]<=0:
													return 'False'
												else: return 'False'
											elif obj[3]>0:
												# {"feature": "Direction_same", "instances": 3, "metric_value": 0.4444, "depth": 12}
												if obj[10]<=0:
													return 'True'
												else: return 'True'
											else: return 'True'
										else: return 'False'
									elif obj[9]<=0.0:
										# {"feature": "Age", "instances": 37, "metric_value": 0.3475, "depth": 10}
										if obj[4]>0:
											# {"feature": "Gender", "instances": 28, "metric_value": 0.4556, "depth": 11}
											if obj[3]>0:
												# {"feature": "Direction_same", "instances": 18, "metric_value": 0.4753, "depth": 12}
												if obj[10]<=0:
													return 'True'
												else: return 'True'
											elif obj[3]<=0:
												# {"feature": "Direction_same", "instances": 10, "metric_value": 0.42, "depth": 12}
												if obj[10]<=0:
													return 'True'
												else: return 'True'
											else: return 'True'
										elif obj[4]<=0:
											return 'True'
										else: return 'True'
									else: return 'True'
								elif obj[7]>0.0:
									# {"feature": "Age", "instances": 114, "metric_value": 0.3972, "depth": 9}
									if obj[4]<=4:
										# {"feature": "Restaurant20to50", "instances": 99, "metric_value": 0.4158, "depth": 10}
										if obj[9]>0.0:
											# {"feature": "Gender", "instances": 80, "metric_value": 0.3895, "depth": 11}
											if obj[3]>0:
												# {"feature": "Direction_same", "instances": 41, "metric_value": 0.4497, "depth": 12}
												if obj[10]<=0:
													return 'True'
												else: return 'True'
											elif obj[3]<=0:
												# {"feature": "Direction_same", "instances": 39, "metric_value": 0.3261, "depth": 12}
												if obj[10]<=0:
													return 'True'
												else: return 'True'
											else: return 'True'
										elif obj[9]<=0.0:
											# {"feature": "Gender", "instances": 19, "metric_value": 0.4164, "depth": 11}
											if obj[3]<=0:
												# {"feature": "Direction_same", "instances": 10, "metric_value": 0.48, "depth": 12}
												if obj[10]<=0:
													return 'False'
												else: return 'False'
											elif obj[3]>0:
												# {"feature": "Direction_same", "instances": 9, "metric_value": 0.3457, "depth": 12}
												if obj[10]<=0:
													return 'True'
												else: return 'True'
											else: return 'True'
										else: return 'True'
									elif obj[4]>4:
										# {"feature": "Restaurant20to50", "instances": 15, "metric_value": 0.2212, "depth": 10}
										if obj[9]<=1.0:
											# {"feature": "Gender", "instances": 11, "metric_value": 0.1558, "depth": 11}
											if obj[3]>0:
												# {"feature": "Direction_same", "instances": 7, "metric_value": 0.2449, "depth": 12}
												if obj[10]<=0:
													return 'True'
												else: return 'True'
											elif obj[3]<=0:
												return 'True'
											else: return 'True'
										elif obj[9]>1.0:
											# {"feature": "Gender", "instances": 4, "metric_value": 0.3333, "depth": 11}
											if obj[3]<=0:
												# {"feature": "Direction_same", "instances": 3, "metric_value": 0.4444, "depth": 12}
												if obj[10]<=0:
													return 'True'
												else: return 'True'
											elif obj[3]>0:
												return 'True'
											else: return 'True'
										else: return 'True'
									else: return 'True'
								else: return 'True'
							else: return 'True'
						elif obj[1]<=0:
							# {"feature": "Age", "instances": 123, "metric_value": 0.3875, "depth": 7}
							if obj[4]<=3:
								# {"feature": "Education", "instances": 77, "metric_value": 0.4331, "depth": 8}
								if obj[5]>0:
									# {"feature": "Restaurant20to50", "instances": 45, "metric_value": 0.3867, "depth": 9}
									if obj[9]<=2.0:
										# {"feature": "Bar", "instances": 40, "metric_value": 0.3725, "depth": 10}
										if obj[7]<=2.0:
											# {"feature": "Gender", "instances": 34, "metric_value": 0.3887, "depth": 11}
											if obj[3]>0:
												# {"feature": "Direction_same", "instances": 20, "metric_value": 0.375, "depth": 12}
												if obj[10]<=0:
													return 'True'
												else: return 'True'
											elif obj[3]<=0:
												# {"feature": "Direction_same", "instances": 14, "metric_value": 0.4082, "depth": 12}
												if obj[10]<=0:
													return 'True'
												else: return 'True'
											else: return 'True'
										elif obj[7]>2.0:
											# {"feature": "Gender", "instances": 6, "metric_value": 0.25, "depth": 11}
											if obj[3]<=0:
												# {"feature": "Direction_same", "instances": 4, "metric_value": 0.375, "depth": 12}
												if obj[10]<=0:
													return 'True'
												else: return 'True'
											elif obj[3]>0:
												return 'True'
											else: return 'True'
										else: return 'True'
									elif obj[9]>2.0:
										# {"feature": "Gender", "instances": 5, "metric_value": 0.4667, "depth": 10}
										if obj[3]<=0:
											# {"feature": "Bar", "instances": 3, "metric_value": 0.3333, "depth": 11}
											if obj[7]<=0.0:
												# {"feature": "Direction_same", "instances": 2, "metric_value": 0.5, "depth": 12}
												if obj[10]<=0:
													return 'True'
												else: return 'True'
											elif obj[7]>0.0:
												return 'True'
											else: return 'True'
										elif obj[3]>0:
											# {"feature": "Bar", "instances": 2, "metric_value": 0.5, "depth": 11}
											if obj[7]<=2.0:
												# {"feature": "Direction_same", "instances": 2, "metric_value": 0.5, "depth": 12}
												if obj[10]<=0:
													return 'False'
												else: return 'False'
											else: return 'False'
										else: return 'False'
									else: return 'True'
								elif obj[5]<=0:
									# {"feature": "Bar", "instances": 32, "metric_value": 0.4266, "depth": 9}
									if obj[7]>0.0:
										# {"feature": "Restaurant20to50", "instances": 18, "metric_value": 0.3889, "depth": 10}
										if obj[9]>-1.0:
											# {"feature": "Gender", "instances": 16, "metric_value": 0.3667, "depth": 11}
											if obj[3]>0:
												# {"feature": "Direction_same", "instances": 10, "metric_value": 0.32, "depth": 12}
												if obj[10]<=0:
													return 'True'
												else: return 'True'
											elif obj[3]<=0:
												# {"feature": "Direction_same", "instances": 6, "metric_value": 0.4444, "depth": 12}
												if obj[10]<=0:
													return 'True'
												else: return 'True'
											else: return 'True'
										elif obj[9]<=-1.0:
											# {"feature": "Gender", "instances": 2, "metric_value": 0.5, "depth": 11}
											if obj[3]<=1:
												# {"feature": "Direction_same", "instances": 2, "metric_value": 0.5, "depth": 12}
												if obj[10]<=0:
													return 'True'
												else: return 'True'
											else: return 'True'
										else: return 'True'
									elif obj[7]<=0.0:
										# {"feature": "Restaurant20to50", "instances": 14, "metric_value": 0.2338, "depth": 10}
										if obj[9]<=1.0:
											# {"feature": "Gender", "instances": 11, "metric_value": 0.2727, "depth": 11}
											if obj[3]>0:
												# {"feature": "Direction_same", "instances": 8, "metric_value": 0.375, "depth": 12}
												if obj[10]<=0:
													return 'False'
												else: return 'False'
											elif obj[3]<=0:
												return 'False'
											else: return 'False'
										elif obj[9]>1.0:
											return 'True'
										else: return 'True'
									else: return 'False'
								else: return 'True'
							elif obj[4]>3:
								# {"feature": "Restaurant20to50", "instances": 46, "metric_value": 0.2668, "depth": 8}
								if obj[9]>0.0:
									# {"feature": "Bar", "instances": 30, "metric_value": 0.1571, "depth": 9}
									if obj[7]<=2.0:
										# {"feature": "Gender", "instances": 28, "metric_value": 0.1261, "depth": 10}
										if obj[3]<=0:
											# {"feature": "Education", "instances": 17, "metric_value": 0.1991, "depth": 11}
											if obj[5]>1:
												# {"feature": "Direction_same", "instances": 13, "metric_value": 0.2604, "depth": 12}
												if obj[10]<=0:
													return 'True'
												else: return 'True'
											elif obj[5]<=1:
												return 'True'
											else: return 'True'
										elif obj[3]>0:
											return 'True'
										else: return 'True'
									elif obj[7]>2.0:
										# {"feature": "Gender", "instances": 2, "metric_value": 0.0, "depth": 10}
										if obj[3]>0:
											return 'False'
										elif obj[3]<=0:
											return 'True'
										else: return 'True'
									else: return 'False'
								elif obj[9]<=0.0:
									# {"feature": "Education", "instances": 16, "metric_value": 0.4018, "depth": 9}
									if obj[5]<=2:
										# {"feature": "Bar", "instances": 14, "metric_value": 0.4167, "depth": 10}
										if obj[7]<=1.0:
											# {"feature": "Gender", "instances": 12, "metric_value": 0.4381, "depth": 11}
											if obj[3]>0:
												# {"feature": "Direction_same", "instances": 7, "metric_value": 0.4082, "depth": 12}
												if obj[10]<=0:
													return 'True'
												else: return 'True'
											elif obj[3]<=0:
												# {"feature": "Direction_same", "instances": 5, "metric_value": 0.48, "depth": 12}
												if obj[10]<=0:
													return 'False'
												else: return 'False'
											else: return 'False'
										elif obj[7]>1.0:
											return 'True'
										else: return 'True'
									elif obj[5]>2:
										return 'True'
									else: return 'True'
								else: return 'True'
							else: return 'True'
						else: return 'True'
					elif obj[11]<=1:
						# {"feature": "Time", "instances": 300, "metric_value": 0.4853, "depth": 6}
						if obj[1]<=2:
							# {"feature": "Education", "instances": 185, "metric_value": 0.4876, "depth": 7}
							if obj[5]>1:
								# {"feature": "Bar", "instances": 99, "metric_value": 0.4708, "depth": 8}
								if obj[7]>-1.0:
									# {"feature": "Age", "instances": 95, "metric_value": 0.4704, "depth": 9}
									if obj[4]<=4:
										# {"feature": "Restaurant20to50", "instances": 78, "metric_value": 0.4589, "depth": 10}
										if obj[9]<=2.0:
											# {"feature": "Gender", "instances": 74, "metric_value": 0.4505, "depth": 11}
											if obj[3]<=0:
												# {"feature": "Direction_same", "instances": 41, "metric_value": 0.414, "depth": 12}
												if obj[10]<=0:
													return 'False'
												else: return 'False'
											elif obj[3]>0:
												# {"feature": "Direction_same", "instances": 33, "metric_value": 0.4959, "depth": 12}
												if obj[10]<=0:
													return 'False'
												else: return 'False'
											else: return 'False'
										elif obj[9]>2.0:
											# {"feature": "Gender", "instances": 4, "metric_value": 0.25, "depth": 11}
											if obj[3]<=0:
												return 'True'
											elif obj[3]>0:
												# {"feature": "Direction_same", "instances": 2, "metric_value": 0.5, "depth": 12}
												if obj[10]<=0:
													return 'True'
												else: return 'True'
											else: return 'True'
										else: return 'True'
									elif obj[4]>4:
										# {"feature": "Restaurant20to50", "instances": 17, "metric_value": 0.4373, "depth": 10}
										if obj[9]>0.0:
											# {"feature": "Gender", "instances": 12, "metric_value": 0.4792, "depth": 11}
											if obj[3]<=0:
												# {"feature": "Direction_same", "instances": 8, "metric_value": 0.4688, "depth": 12}
												if obj[10]<=0:
													return 'True'
												else: return 'True'
											elif obj[3]>0:
												# {"feature": "Direction_same", "instances": 4, "metric_value": 0.5, "depth": 12}
												if obj[10]<=0:
													return 'False'
												else: return 'False'
											else: return 'False'
										elif obj[9]<=0.0:
											# {"feature": "Gender", "instances": 5, "metric_value": 0.3, "depth": 11}
											if obj[3]<=0:
												# {"feature": "Direction_same", "instances": 4, "metric_value": 0.375, "depth": 12}
												if obj[10]<=0:
													return 'True'
												else: return 'True'
											elif obj[3]>0:
												return 'True'
											else: return 'True'
										else: return 'True'
									else: return 'True'
								elif obj[7]<=-1.0:
									return 'True'
								else: return 'True'
							elif obj[5]<=1:
								# {"feature": "Bar", "instances": 86, "metric_value": 0.4403, "depth": 8}
								if obj[7]>-1.0:
									# {"feature": "Age", "instances": 79, "metric_value": 0.4233, "depth": 9}
									if obj[4]<=3:
										# {"feature": "Restaurant20to50", "instances": 40, "metric_value": 0.3312, "depth": 10}
										if obj[9]>0.0:
											# {"feature": "Gender", "instances": 33, "metric_value": 0.2944, "depth": 11}
											if obj[3]>0:
												# {"feature": "Direction_same", "instances": 20, "metric_value": 0.255, "depth": 12}
												if obj[10]<=0:
													return 'True'
												else: return 'True'
											elif obj[3]<=0:
												# {"feature": "Direction_same", "instances": 13, "metric_value": 0.355, "depth": 12}
												if obj[10]<=0:
													return 'True'
												else: return 'True'
											else: return 'True'
										elif obj[9]<=0.0:
											# {"feature": "Gender", "instances": 7, "metric_value": 0.4762, "depth": 11}
											if obj[3]<=0:
												# {"feature": "Direction_same", "instances": 4, "metric_value": 0.5, "depth": 12}
												if obj[10]<=0:
													return 'False'
												else: return 'False'
											elif obj[3]>0:
												# {"feature": "Direction_same", "instances": 3, "metric_value": 0.4444, "depth": 12}
												if obj[10]<=0:
													return 'True'
												else: return 'True'
											else: return 'True'
										else: return 'True'
									elif obj[4]>3:
										# {"feature": "Restaurant20to50", "instances": 39, "metric_value": 0.4932, "depth": 10}
										if obj[9]<=1.0:
											# {"feature": "Gender", "instances": 31, "metric_value": 0.4991, "depth": 11}
											if obj[3]<=0:
												# {"feature": "Direction_same", "instances": 17, "metric_value": 0.4983, "depth": 12}
												if obj[10]<=0:
													return 'False'
												else: return 'False'
											elif obj[3]>0:
												# {"feature": "Direction_same", "instances": 14, "metric_value": 0.5, "depth": 12}
												if obj[10]<=0:
													return 'False'
												else: return 'False'
											else: return 'False'
										elif obj[9]>1.0:
											# {"feature": "Gender", "instances": 8, "metric_value": 0.4375, "depth": 11}
											if obj[3]>0:
												# {"feature": "Direction_same", "instances": 4, "metric_value": 0.5, "depth": 12}
												if obj[10]<=0:
													return 'False'
												else: return 'False'
											elif obj[3]<=0:
												# {"feature": "Direction_same", "instances": 4, "metric_value": 0.375, "depth": 12}
												if obj[10]<=0:
													return 'True'
												else: return 'True'
											else: return 'True'
										else: return 'True'
									else: return 'True'
								elif obj[7]<=-1.0:
									# {"feature": "Gender", "instances": 7, "metric_value": 0.1905, "depth": 9}
									if obj[3]<=0:
										return 'False'
									elif obj[3]>0:
										# {"feature": "Restaurant20to50", "instances": 3, "metric_value": 0.0, "depth": 10}
										if obj[9]>-1.0:
											return 'False'
										elif obj[9]<=-1.0:
											return 'True'
										else: return 'True'
									else: return 'False'
								else: return 'False'
							else: return 'True'
						elif obj[1]>2:
							# {"feature": "Bar", "instances": 115, "metric_value": 0.449, "depth": 7}
							if obj[7]<=0.0:
								# {"feature": "Age", "instances": 60, "metric_value": 0.3915, "depth": 8}
								if obj[4]>0:
									# {"feature": "Education", "instances": 55, "metric_value": 0.408, "depth": 9}
									if obj[5]<=3:
										# {"feature": "Restaurant20to50", "instances": 50, "metric_value": 0.4392, "depth": 10}
										if obj[9]<=2.0:
											# {"feature": "Gender", "instances": 48, "metric_value": 0.4516, "depth": 11}
											if obj[3]<=0:
												# {"feature": "Direction_same", "instances": 29, "metric_value": 0.4281, "depth": 12}
												if obj[10]<=0:
													return 'True'
												else: return 'True'
											elif obj[3]>0:
												# {"feature": "Direction_same", "instances": 19, "metric_value": 0.4875, "depth": 12}
												if obj[10]<=0:
													return 'True'
												else: return 'True'
											else: return 'True'
										elif obj[9]>2.0:
											return 'True'
										else: return 'True'
									elif obj[5]>3:
										return 'True'
									else: return 'True'
								elif obj[4]<=0:
									return 'True'
								else: return 'True'
							elif obj[7]>0.0:
								# {"feature": "Restaurant20to50", "instances": 55, "metric_value": 0.4628, "depth": 8}
								if obj[9]<=1.0:
									# {"feature": "Age", "instances": 36, "metric_value": 0.4216, "depth": 9}
									if obj[4]>0:
										# {"feature": "Education", "instances": 28, "metric_value": 0.3929, "depth": 10}
										if obj[5]<=2:
											# {"feature": "Gender", "instances": 24, "metric_value": 0.3741, "depth": 11}
											if obj[3]<=0:
												# {"feature": "Direction_same", "instances": 13, "metric_value": 0.355, "depth": 12}
												if obj[10]<=0:
													return 'True'
												else: return 'True'
											elif obj[3]>0:
												# {"feature": "Direction_same", "instances": 11, "metric_value": 0.3967, "depth": 12}
												if obj[10]<=0:
													return 'True'
												else: return 'True'
											else: return 'True'
										elif obj[5]>2:
											# {"feature": "Gender", "instances": 4, "metric_value": 0.0, "depth": 11}
											if obj[3]<=0:
												return 'False'
											elif obj[3]>0:
												return 'True'
											else: return 'True'
										else: return 'False'
									elif obj[4]<=0:
										# {"feature": "Gender", "instances": 8, "metric_value": 0.1875, "depth": 10}
										if obj[3]>0:
											return 'False'
										elif obj[3]<=0:
											# {"feature": "Education", "instances": 4, "metric_value": 0.25, "depth": 11}
											if obj[5]>0:
												# {"feature": "Direction_same", "instances": 2, "metric_value": 0.5, "depth": 12}
												if obj[10]<=0:
													return 'False'
												else: return 'False'
											elif obj[5]<=0:
												return 'True'
											else: return 'True'
										else: return 'True'
									else: return 'False'
								elif obj[9]>1.0:
									# {"feature": "Age", "instances": 19, "metric_value": 0.3158, "depth": 9}
									if obj[4]>1:
										# {"feature": "Education", "instances": 16, "metric_value": 0.3, "depth": 10}
										if obj[5]>1:
											# {"feature": "Gender", "instances": 10, "metric_value": 0.1714, "depth": 11}
											if obj[3]<=0:
												# {"feature": "Direction_same", "instances": 7, "metric_value": 0.2449, "depth": 12}
												if obj[10]<=0:
													return 'False'
												else: return 'False'
											elif obj[3]>0:
												return 'False'
											else: return 'False'
										elif obj[5]<=1:
											# {"feature": "Gender", "instances": 6, "metric_value": 0.5, "depth": 11}
											if obj[3]<=0:
												# {"feature": "Direction_same", "instances": 4, "metric_value": 0.5, "depth": 12}
												if obj[10]<=0:
													return 'True'
												else: return 'True'
											elif obj[3]>0:
												# {"feature": "Direction_same", "instances": 2, "metric_value": 0.5, "depth": 12}
												if obj[10]<=0:
													return 'True'
												else: return 'True'
											else: return 'True'
										else: return 'True'
									elif obj[4]<=1:
										return 'True'
									else: return 'True'
								else: return 'False'
							else: return 'True'
						else: return 'True'
					else: return 'True'
				elif obj[6]<=1.7265574939131305:
					# {"feature": "Age", "instances": 190, "metric_value": 0.3859, "depth": 5}
					if obj[4]>1:
						# {"feature": "Bar", "instances": 110, "metric_value": 0.415, "depth": 6}
						if obj[7]<=1.0:
							# {"feature": "Time", "instances": 91, "metric_value": 0.4502, "depth": 7}
							if obj[1]<=2:
								# {"feature": "Education", "instances": 51, "metric_value": 0.4808, "depth": 8}
								if obj[5]>0:
									# {"feature": "Restaurant20to50", "instances": 26, "metric_value": 0.4583, "depth": 9}
									if obj[9]<=1.0:
										# {"feature": "Distance", "instances": 24, "metric_value": 0.4778, "depth": 10}
										if obj[11]<=1:
											# {"feature": "Gender", "instances": 15, "metric_value": 0.4933, "depth": 11}
											if obj[3]>0:
												# {"feature": "Direction_same", "instances": 10, "metric_value": 0.5, "depth": 12}
												if obj[10]<=0:
													return 'True'
												else: return 'True'
											elif obj[3]<=0:
												# {"feature": "Direction_same", "instances": 5, "metric_value": 0.48, "depth": 12}
												if obj[10]<=0:
													return 'True'
												else: return 'True'
											else: return 'True'
										elif obj[11]>1:
											# {"feature": "Gender", "instances": 9, "metric_value": 0.4286, "depth": 11}
											if obj[3]>0:
												# {"feature": "Direction_same", "instances": 7, "metric_value": 0.4082, "depth": 12}
												if obj[10]<=0:
													return 'False'
												else: return 'False'
											elif obj[3]<=0:
												# {"feature": "Direction_same", "instances": 2, "metric_value": 0.5, "depth": 12}
												if obj[10]<=0:
													return 'True'
												else: return 'True'
											else: return 'True'
										else: return 'False'
									elif obj[9]>1.0:
										return 'True'
									else: return 'True'
								elif obj[5]<=0:
									# {"feature": "Restaurant20to50", "instances": 25, "metric_value": 0.4029, "depth": 9}
									if obj[9]<=1.0:
										# {"feature": "Gender", "instances": 21, "metric_value": 0.4063, "depth": 10}
										if obj[3]>0:
											# {"feature": "Distance", "instances": 15, "metric_value": 0.3692, "depth": 11}
											if obj[11]>1:
												# {"feature": "Direction_same", "instances": 13, "metric_value": 0.426, "depth": 12}
												if obj[10]<=0:
													return 'True'
												else: return 'True'
											elif obj[11]<=1:
												return 'True'
											else: return 'True'
										elif obj[3]<=0:
											# {"feature": "Distance", "instances": 6, "metric_value": 0.4167, "depth": 11}
											if obj[11]>1:
												# {"feature": "Direction_same", "instances": 4, "metric_value": 0.375, "depth": 12}
												if obj[10]<=0:
													return 'True'
												else: return 'True'
											elif obj[11]<=1:
												# {"feature": "Direction_same", "instances": 2, "metric_value": 0.5, "depth": 12}
												if obj[10]<=0:
													return 'False'
												else: return 'False'
											else: return 'False'
										else: return 'True'
									elif obj[9]>1.0:
										# {"feature": "Distance", "instances": 4, "metric_value": 0.3333, "depth": 10}
										if obj[11]>1:
											# {"feature": "Gender", "instances": 3, "metric_value": 0.4444, "depth": 11}
											if obj[3]<=1:
												# {"feature": "Direction_same", "instances": 3, "metric_value": 0.4444, "depth": 12}
												if obj[10]<=0:
													return 'False'
												else: return 'False'
											else: return 'False'
										elif obj[11]<=1:
											return 'False'
										else: return 'False'
									else: return 'False'
								else: return 'True'
							elif obj[1]>2:
								# {"feature": "Education", "instances": 40, "metric_value": 0.3486, "depth": 8}
								if obj[5]<=3:
									# {"feature": "Gender", "instances": 36, "metric_value": 0.3305, "depth": 9}
									if obj[3]>0:
										# {"feature": "Distance", "instances": 25, "metric_value": 0.3947, "depth": 10}
										if obj[11]>1:
											# {"feature": "Restaurant20to50", "instances": 17, "metric_value": 0.3529, "depth": 11}
											if obj[9]>0.0:
												# {"feature": "Direction_same", "instances": 16, "metric_value": 0.375, "depth": 12}
												if obj[10]<=0:
													return 'True'
												else: return 'True'
											elif obj[9]<=0.0:
												return 'True'
											else: return 'True'
										elif obj[11]<=1:
											# {"feature": "Restaurant20to50", "instances": 8, "metric_value": 0.4583, "depth": 11}
											if obj[9]<=1.0:
												# {"feature": "Direction_same", "instances": 6, "metric_value": 0.4444, "depth": 12}
												if obj[10]<=0:
													return 'True'
												else: return 'True'
											elif obj[9]>1.0:
												# {"feature": "Direction_same", "instances": 2, "metric_value": 0.5, "depth": 12}
												if obj[10]<=0:
													return 'True'
												else: return 'True'
											else: return 'True'
										else: return 'True'
									elif obj[3]<=0:
										# {"feature": "Restaurant20to50", "instances": 11, "metric_value": 0.1591, "depth": 10}
										if obj[9]>0.0:
											# {"feature": "Distance", "instances": 8, "metric_value": 0.2083, "depth": 11}
											if obj[11]>1:
												# {"feature": "Direction_same", "instances": 6, "metric_value": 0.2778, "depth": 12}
												if obj[10]<=0:
													return 'True'
												else: return 'True'
											elif obj[11]<=1:
												return 'True'
											else: return 'True'
										elif obj[9]<=0.0:
											return 'True'
										else: return 'True'
									else: return 'True'
								elif obj[5]>3:
									# {"feature": "Distance", "instances": 4, "metric_value": 0.25, "depth": 9}
									if obj[11]<=1:
										# {"feature": "Gender", "instances": 2, "metric_value": 0.5, "depth": 10}
										if obj[3]<=1:
											# {"feature": "Restaurant20to50", "instances": 2, "metric_value": 0.5, "depth": 11}
											if obj[9]<=0.0:
												# {"feature": "Direction_same", "instances": 2, "metric_value": 0.5, "depth": 12}
												if obj[10]<=0:
													return 'True'
												else: return 'True'
											else: return 'True'
										else: return 'True'
									elif obj[11]>1:
										return 'False'
									else: return 'False'
								else: return 'False'
							else: return 'True'
						elif obj[7]>1.0:
							# {"feature": "Time", "instances": 19, "metric_value": 0.1849, "depth": 7}
							if obj[1]<=3:
								# {"feature": "Distance", "instances": 13, "metric_value": 0.1026, "depth": 8}
								if obj[11]>1:
									return 'True'
								elif obj[11]<=1:
									# {"feature": "Gender", "instances": 3, "metric_value": 0.3333, "depth": 9}
									if obj[3]>0:
										# {"feature": "Education", "instances": 2, "metric_value": 0.5, "depth": 10}
										if obj[5]<=4:
											# {"feature": "Restaurant20to50", "instances": 2, "metric_value": 0.5, "depth": 11}
											if obj[9]<=1.0:
												# {"feature": "Direction_same", "instances": 2, "metric_value": 0.5, "depth": 12}
												if obj[10]<=0:
													return 'False'
												else: return 'False'
											else: return 'False'
										else: return 'False'
									elif obj[3]<=0:
										return 'True'
									else: return 'True'
								else: return 'True'
							elif obj[1]>3:
								# {"feature": "Gender", "instances": 6, "metric_value": 0.2222, "depth": 8}
								if obj[3]>0:
									return 'True'
								elif obj[3]<=0:
									# {"feature": "Distance", "instances": 3, "metric_value": 0.3333, "depth": 9}
									if obj[11]>1:
										# {"feature": "Education", "instances": 2, "metric_value": 0.5, "depth": 10}
										if obj[5]<=0:
											# {"feature": "Restaurant20to50", "instances": 2, "metric_value": 0.5, "depth": 11}
											if obj[9]<=1.0:
												# {"feature": "Direction_same", "instances": 2, "metric_value": 0.5, "depth": 12}
												if obj[10]<=0:
													return 'True'
												else: return 'True'
											else: return 'True'
										else: return 'True'
									elif obj[11]<=1:
										return 'True'
									else: return 'True'
								else: return 'True'
							else: return 'True'
						else: return 'True'
					elif obj[4]<=1:
						# {"feature": "Education", "instances": 80, "metric_value": 0.3123, "depth": 6}
						if obj[5]<=3:
							# {"feature": "Distance", "instances": 73, "metric_value": 0.3391, "depth": 7}
							if obj[11]>1:
								# {"feature": "Bar", "instances": 43, "metric_value": 0.2826, "depth": 8}
								if obj[7]<=2.0:
									# {"feature": "Gender", "instances": 39, "metric_value": 0.2544, "depth": 9}
									if obj[3]>0:
										# {"feature": "Restaurant20to50", "instances": 26, "metric_value": 0.293, "depth": 10}
										if obj[9]<=1.0:
											# {"feature": "Time", "instances": 21, "metric_value": 0.3492, "depth": 11}
											if obj[1]<=2:
												# {"feature": "Direction_same", "instances": 12, "metric_value": 0.2778, "depth": 12}
												if obj[10]<=0:
													return 'True'
												else: return 'True'
											elif obj[1]>2:
												# {"feature": "Direction_same", "instances": 9, "metric_value": 0.4444, "depth": 12}
												if obj[10]<=0:
													return 'True'
												else: return 'True'
											else: return 'True'
										elif obj[9]>1.0:
											return 'True'
										else: return 'True'
									elif obj[3]<=0:
										# {"feature": "Time", "instances": 13, "metric_value": 0.1231, "depth": 10}
										if obj[1]>2:
											return 'True'
										elif obj[1]<=2:
											# {"feature": "Restaurant20to50", "instances": 5, "metric_value": 0.3, "depth": 11}
											if obj[9]>1.0:
												# {"feature": "Direction_same", "instances": 4, "metric_value": 0.375, "depth": 12}
												if obj[10]<=0:
													return 'True'
												else: return 'True'
											elif obj[9]<=1.0:
												return 'True'
											else: return 'True'
										else: return 'True'
									else: return 'True'
								elif obj[7]>2.0:
									# {"feature": "Time", "instances": 4, "metric_value": 0.0, "depth": 9}
									if obj[1]<=3:
										return 'True'
									elif obj[1]>3:
										return 'False'
									else: return 'False'
								else: return 'True'
							elif obj[11]<=1:
								# {"feature": "Bar", "instances": 30, "metric_value": 0.3367, "depth": 8}
								if obj[7]>0.0:
									# {"feature": "Restaurant20to50", "instances": 20, "metric_value": 0.2278, "depth": 9}
									if obj[9]>0.0:
										# {"feature": "Time", "instances": 18, "metric_value": 0.188, "depth": 10}
										if obj[1]<=2:
											# {"feature": "Gender", "instances": 13, "metric_value": 0.2601, "depth": 11}
											if obj[3]<=0:
												# {"feature": "Direction_same", "instances": 7, "metric_value": 0.2449, "depth": 12}
												if obj[10]<=0:
													return 'True'
												else: return 'True'
											elif obj[3]>0:
												# {"feature": "Direction_same", "instances": 6, "metric_value": 0.2778, "depth": 12}
												if obj[10]<=0:
													return 'True'
												else: return 'True'
											else: return 'True'
										elif obj[1]>2:
											return 'True'
										else: return 'True'
									elif obj[9]<=0.0:
										# {"feature": "Time", "instances": 2, "metric_value": 0.0, "depth": 10}
										if obj[1]<=0:
											return 'False'
										elif obj[1]>0:
											return 'True'
										else: return 'True'
									else: return 'False'
								elif obj[7]<=0.0:
									# {"feature": "Time", "instances": 10, "metric_value": 0.4444, "depth": 9}
									if obj[1]>0:
										# {"feature": "Restaurant20to50", "instances": 9, "metric_value": 0.4167, "depth": 10}
										if obj[9]<=1.0:
											# {"feature": "Gender", "instances": 8, "metric_value": 0.4286, "depth": 11}
											if obj[3]>0:
												# {"feature": "Direction_same", "instances": 7, "metric_value": 0.4898, "depth": 12}
												if obj[10]<=0:
													return 'True'
												else: return 'True'
											elif obj[3]<=0:
												return 'True'
											else: return 'True'
										elif obj[9]>1.0:
											return 'False'
										else: return 'False'
									elif obj[1]<=0:
										return 'False'
									else: return 'False'
								else: return 'False'
							else: return 'True'
						elif obj[5]>3:
							return 'True'
						else: return 'True'
					else: return 'True'
				else: return 'True'
			else: return 'True'
		elif obj[8]>1.0:
			# {"feature": "Distance", "instances": 2885, "metric_value": 0.412, "depth": 3}
			if obj[11]<=2:
				# {"feature": "Passanger", "instances": 2614, "metric_value": 0.4001, "depth": 4}
				if obj[0]<=2:
					# {"feature": "Occupation", "instances": 1699, "metric_value": 0.4228, "depth": 5}
					if obj[6]<=18.185882392956827:
						# {"feature": "Direction_same", "instances": 1580, "metric_value": 0.4321, "depth": 6}
						if obj[10]<=0:
							# {"feature": "Time", "instances": 1024, "metric_value": 0.4381, "depth": 7}
							if obj[1]>1:
								# {"feature": "Age", "instances": 553, "metric_value": 0.3955, "depth": 8}
								if obj[4]>0:
									# {"feature": "Bar", "instances": 472, "metric_value": 0.3798, "depth": 9}
									if obj[7]<=1.0:
										# {"feature": "Gender", "instances": 289, "metric_value": 0.3396, "depth": 10}
										if obj[3]>0:
											# {"feature": "Restaurant20to50", "instances": 171, "metric_value": 0.4008, "depth": 11}
											if obj[9]<=2.0:
												# {"feature": "Education", "instances": 153, "metric_value": 0.4132, "depth": 12}
												if obj[5]>1:
													return 'True'
												elif obj[5]<=1:
													return 'True'
												else: return 'True'
											elif obj[9]>2.0:
												# {"feature": "Education", "instances": 18, "metric_value": 0.2708, "depth": 12}
												if obj[5]<=2:
													return 'True'
												elif obj[5]>2:
													return 'True'
												else: return 'True'
											else: return 'True'
										elif obj[3]<=0:
											# {"feature": "Education", "instances": 118, "metric_value": 0.2441, "depth": 11}
											if obj[5]<=2:
												# {"feature": "Restaurant20to50", "instances": 92, "metric_value": 0.2644, "depth": 12}
												if obj[9]>0.0:
													return 'True'
												elif obj[9]<=0.0:
													return 'True'
												else: return 'True'
											elif obj[5]>2:
												# {"feature": "Restaurant20to50", "instances": 26, "metric_value": 0.1377, "depth": 12}
												if obj[9]>0.0:
													return 'True'
												elif obj[9]<=0.0:
													return 'True'
												else: return 'True'
											else: return 'True'
										else: return 'True'
									elif obj[7]>1.0:
										# {"feature": "Education", "instances": 183, "metric_value": 0.4199, "depth": 10}
										if obj[5]>1:
											# {"feature": "Restaurant20to50", "instances": 136, "metric_value": 0.3896, "depth": 11}
											if obj[9]<=3.0:
												# {"feature": "Gender", "instances": 128, "metric_value": 0.3803, "depth": 12}
												if obj[3]<=0:
													return 'True'
												elif obj[3]>0:
													return 'True'
												else: return 'True'
											elif obj[9]>3.0:
												# {"feature": "Gender", "instances": 8, "metric_value": 0.4667, "depth": 12}
												if obj[3]<=0:
													return 'False'
												elif obj[3]>0:
													return 'True'
												else: return 'True'
											else: return 'True'
										elif obj[5]<=1:
											# {"feature": "Gender", "instances": 47, "metric_value": 0.466, "depth": 11}
											if obj[3]<=0:
												# {"feature": "Restaurant20to50", "instances": 27, "metric_value": 0.4103, "depth": 12}
												if obj[9]>0.0:
													return 'True'
												elif obj[9]<=0.0:
													return 'False'
												else: return 'False'
											elif obj[3]>0:
												# {"feature": "Restaurant20to50", "instances": 20, "metric_value": 0.4917, "depth": 12}
												if obj[9]<=1.0:
													return 'False'
												elif obj[9]>1.0:
													return 'False'
												else: return 'False'
											else: return 'False'
										else: return 'True'
									else: return 'True'
								elif obj[4]<=0:
									# {"feature": "Education", "instances": 81, "metric_value": 0.4418, "depth": 9}
									if obj[5]<=3:
										# {"feature": "Bar", "instances": 70, "metric_value": 0.4695, "depth": 10}
										if obj[7]>0.0:
											# {"feature": "Restaurant20to50", "instances": 48, "metric_value": 0.4407, "depth": 11}
											if obj[9]<=3.0:
												# {"feature": "Gender", "instances": 45, "metric_value": 0.4567, "depth": 12}
												if obj[3]>0:
													return 'True'
												elif obj[3]<=0:
													return 'True'
												else: return 'True'
											elif obj[9]>3.0:
												return 'True'
											else: return 'True'
										elif obj[7]<=0.0:
											# {"feature": "Restaurant20to50", "instances": 22, "metric_value": 0.3326, "depth": 11}
											if obj[9]<=1.0:
												# {"feature": "Gender", "instances": 13, "metric_value": 0.4256, "depth": 12}
												if obj[3]>0:
													return 'True'
												elif obj[3]<=0:
													return 'True'
												else: return 'True'
											elif obj[9]>1.0:
												# {"feature": "Gender", "instances": 9, "metric_value": 0.1975, "depth": 12}
												if obj[3]<=1:
													return 'False'
												else: return 'False'
											else: return 'False'
										else: return 'False'
									elif obj[5]>3:
										# {"feature": "Gender", "instances": 11, "metric_value": 0.1364, "depth": 10}
										if obj[3]>0:
											return 'True'
										elif obj[3]<=0:
											# {"feature": "Bar", "instances": 4, "metric_value": 0.375, "depth": 11}
											if obj[7]<=0.0:
												# {"feature": "Restaurant20to50", "instances": 4, "metric_value": 0.375, "depth": 12}
												if obj[9]<=1.0:
													return 'True'
												else: return 'True'
											else: return 'True'
										else: return 'True'
									else: return 'True'
								else: return 'True'
							elif obj[1]<=1:
								# {"feature": "Bar", "instances": 471, "metric_value": 0.4804, "depth": 8}
								if obj[7]>0.0:
									# {"feature": "Education", "instances": 331, "metric_value": 0.489, "depth": 9}
									if obj[5]<=3:
										# {"feature": "Restaurant20to50", "instances": 309, "metric_value": 0.4916, "depth": 10}
										if obj[9]>-1.0:
											# {"feature": "Age", "instances": 306, "metric_value": 0.493, "depth": 11}
											if obj[4]>0:
												# {"feature": "Gender", "instances": 273, "metric_value": 0.4934, "depth": 12}
												if obj[3]>0:
													return 'True'
												elif obj[3]<=0:
													return 'True'
												else: return 'True'
											elif obj[4]<=0:
												# {"feature": "Gender", "instances": 33, "metric_value": 0.484, "depth": 12}
												if obj[3]>0:
													return 'False'
												elif obj[3]<=0:
													return 'False'
												else: return 'False'
											else: return 'False'
										elif obj[9]<=-1.0:
											return 'True'
										else: return 'True'
									elif obj[5]>3:
										# {"feature": "Age", "instances": 22, "metric_value": 0.3732, "depth": 10}
										if obj[4]<=3:
											# {"feature": "Restaurant20to50", "instances": 19, "metric_value": 0.4316, "depth": 11}
											if obj[9]>3.0:
												# {"feature": "Gender", "instances": 10, "metric_value": 0.42, "depth": 12}
												if obj[3]<=0:
													return 'True'
												else: return 'True'
											elif obj[9]<=3.0:
												# {"feature": "Gender", "instances": 9, "metric_value": 0.4444, "depth": 12}
												if obj[3]<=0:
													return 'True'
												elif obj[3]>0:
													return 'True'
												else: return 'True'
											else: return 'True'
										elif obj[4]>3:
											return 'True'
										else: return 'True'
									else: return 'True'
								elif obj[7]<=0.0:
									# {"feature": "Age", "instances": 140, "metric_value": 0.4392, "depth": 9}
									if obj[4]>2:
										# {"feature": "Gender", "instances": 81, "metric_value": 0.4694, "depth": 10}
										if obj[3]>0:
											# {"feature": "Education", "instances": 52, "metric_value": 0.4414, "depth": 11}
											if obj[5]<=2:
												# {"feature": "Restaurant20to50", "instances": 42, "metric_value": 0.4179, "depth": 12}
												if obj[9]>-1.0:
													return 'True'
												elif obj[9]<=-1.0:
													return 'True'
												else: return 'True'
											elif obj[5]>2:
												# {"feature": "Restaurant20to50", "instances": 10, "metric_value": 0.48, "depth": 12}
												if obj[9]>1.0:
													return 'False'
												elif obj[9]<=1.0:
													return 'True'
												else: return 'True'
											else: return 'True'
										elif obj[3]<=0:
											# {"feature": "Education", "instances": 29, "metric_value": 0.4803, "depth": 11}
											if obj[5]<=3:
												# {"feature": "Restaurant20to50", "instances": 28, "metric_value": 0.4671, "depth": 12}
												if obj[9]>0.0:
													return 'True'
												elif obj[9]<=0.0:
													return 'False'
												else: return 'False'
											elif obj[5]>3:
												return 'True'
											else: return 'True'
										else: return 'False'
									elif obj[4]<=2:
										# {"feature": "Restaurant20to50", "instances": 59, "metric_value": 0.361, "depth": 10}
										if obj[9]<=2.0:
											# {"feature": "Education", "instances": 56, "metric_value": 0.3497, "depth": 11}
											if obj[5]<=3:
												# {"feature": "Gender", "instances": 48, "metric_value": 0.3296, "depth": 12}
												if obj[3]>0:
													return 'True'
												elif obj[3]<=0:
													return 'True'
												else: return 'True'
											elif obj[5]>3:
												# {"feature": "Gender", "instances": 8, "metric_value": 0.3571, "depth": 12}
												if obj[3]>0:
													return 'True'
												elif obj[3]<=0:
													return 'False'
												else: return 'False'
											else: return 'True'
										elif obj[9]>2.0:
											# {"feature": "Gender", "instances": 3, "metric_value": 0.0, "depth": 11}
											if obj[3]>0:
												return 'False'
											elif obj[3]<=0:
												return 'True'
											else: return 'True'
										else: return 'False'
									else: return 'True'
								else: return 'True'
							else: return 'True'
						elif obj[10]>0:
							# {"feature": "Time", "instances": 556, "metric_value": 0.3922, "depth": 7}
							if obj[1]<=1:
								# {"feature": "Education", "instances": 451, "metric_value": 0.3659, "depth": 8}
								if obj[5]>1:
									# {"feature": "Restaurant20to50", "instances": 273, "metric_value": 0.3959, "depth": 9}
									if obj[9]<=1.0:
										# {"feature": "Age", "instances": 157, "metric_value": 0.4229, "depth": 10}
										if obj[4]>1:
											# {"feature": "Bar", "instances": 105, "metric_value": 0.402, "depth": 11}
											if obj[7]<=2.0:
												# {"feature": "Gender", "instances": 88, "metric_value": 0.3856, "depth": 12}
												if obj[3]>0:
													return 'True'
												elif obj[3]<=0:
													return 'True'
												else: return 'True'
											elif obj[7]>2.0:
												# {"feature": "Gender", "instances": 17, "metric_value": 0.4706, "depth": 12}
												if obj[3]<=0:
													return 'True'
												elif obj[3]>0:
													return 'True'
												else: return 'True'
											else: return 'True'
										elif obj[4]<=1:
											# {"feature": "Bar", "instances": 52, "metric_value": 0.4354, "depth": 11}
											if obj[7]>0.0:
												# {"feature": "Gender", "instances": 30, "metric_value": 0.3873, "depth": 12}
												if obj[3]<=0:
													return 'True'
												elif obj[3]>0:
													return 'True'
												else: return 'True'
											elif obj[7]<=0.0:
												# {"feature": "Gender", "instances": 22, "metric_value": 0.4935, "depth": 12}
												if obj[3]>0:
													return 'True'
												elif obj[3]<=0:
													return 'True'
												else: return 'True'
											else: return 'True'
										else: return 'True'
									elif obj[9]>1.0:
										# {"feature": "Bar", "instances": 116, "metric_value": 0.3455, "depth": 10}
										if obj[7]>0.0:
											# {"feature": "Age", "instances": 96, "metric_value": 0.3124, "depth": 11}
											if obj[4]<=4:
												# {"feature": "Gender", "instances": 76, "metric_value": 0.3463, "depth": 12}
												if obj[3]>0:
													return 'True'
												elif obj[3]<=0:
													return 'True'
												else: return 'True'
											elif obj[4]>4:
												# {"feature": "Gender", "instances": 20, "metric_value": 0.1667, "depth": 12}
												if obj[3]<=0:
													return 'True'
												elif obj[3]>0:
													return 'True'
												else: return 'True'
											else: return 'True'
										elif obj[7]<=0.0:
											# {"feature": "Age", "instances": 20, "metric_value": 0.4484, "depth": 11}
											if obj[4]<=4:
												# {"feature": "Gender", "instances": 13, "metric_value": 0.4126, "depth": 12}
												if obj[3]>0:
													return 'True'
												elif obj[3]<=0:
													return 'True'
												else: return 'True'
											elif obj[4]>4:
												# {"feature": "Gender", "instances": 7, "metric_value": 0.4898, "depth": 12}
												if obj[3]<=1:
													return 'False'
												else: return 'False'
											else: return 'False'
										else: return 'True'
									else: return 'True'
								elif obj[5]<=1:
									# {"feature": "Age", "instances": 178, "metric_value": 0.3119, "depth": 9}
									if obj[4]>0:
										# {"feature": "Bar", "instances": 161, "metric_value": 0.3267, "depth": 10}
										if obj[7]<=3.0:
											# {"feature": "Restaurant20to50", "instances": 155, "metric_value": 0.3162, "depth": 11}
											if obj[9]>0.0:
												# {"feature": "Gender", "instances": 132, "metric_value": 0.2974, "depth": 12}
												if obj[3]>0:
													return 'True'
												elif obj[3]<=0:
													return 'True'
												else: return 'True'
											elif obj[9]<=0.0:
												# {"feature": "Gender", "instances": 23, "metric_value": 0.4099, "depth": 12}
												if obj[3]<=0:
													return 'True'
												elif obj[3]>0:
													return 'True'
												else: return 'True'
											else: return 'True'
										elif obj[7]>3.0:
											# {"feature": "Restaurant20to50", "instances": 6, "metric_value": 0.25, "depth": 11}
											if obj[9]<=1.0:
												# {"feature": "Gender", "instances": 4, "metric_value": 0.3333, "depth": 12}
												if obj[3]>0:
													return 'True'
												elif obj[3]<=0:
													return 'True'
												else: return 'True'
											elif obj[9]>1.0:
												return 'False'
											else: return 'False'
										else: return 'False'
									elif obj[4]<=0:
										# {"feature": "Gender", "instances": 17, "metric_value": 0.0882, "depth": 10}
										if obj[3]>0:
											return 'True'
										elif obj[3]<=0:
											# {"feature": "Bar", "instances": 4, "metric_value": 0.25, "depth": 11}
											if obj[7]<=2.0:
												# {"feature": "Restaurant20to50", "instances": 2, "metric_value": 0.0, "depth": 12}
												if obj[9]<=1.0:
													return 'False'
												elif obj[9]>1.0:
													return 'True'
												else: return 'True'
											elif obj[7]>2.0:
												return 'True'
											else: return 'True'
										else: return 'True'
									else: return 'True'
								else: return 'True'
							elif obj[1]>1:
								# {"feature": "Restaurant20to50", "instances": 105, "metric_value": 0.4749, "depth": 8}
								if obj[9]<=2.0:
									# {"feature": "Education", "instances": 90, "metric_value": 0.4651, "depth": 9}
									if obj[5]<=3:
										# {"feature": "Age", "instances": 86, "metric_value": 0.4826, "depth": 10}
										if obj[4]<=6:
											# {"feature": "Gender", "instances": 85, "metric_value": 0.4841, "depth": 11}
											if obj[3]<=0:
												# {"feature": "Bar", "instances": 45, "metric_value": 0.4876, "depth": 12}
												if obj[7]>0.0:
													return 'True'
												elif obj[7]<=0.0:
													return 'False'
												else: return 'False'
											elif obj[3]>0:
												# {"feature": "Bar", "instances": 40, "metric_value": 0.4632, "depth": 12}
												if obj[7]<=2.0:
													return 'True'
												elif obj[7]>2.0:
													return 'True'
												else: return 'True'
											else: return 'True'
										elif obj[4]>6:
											return 'True'
										else: return 'True'
									elif obj[5]>3:
										return 'True'
									else: return 'True'
								elif obj[9]>2.0:
									# {"feature": "Bar", "instances": 15, "metric_value": 0.3636, "depth": 9}
									if obj[7]>1.0:
										# {"feature": "Age", "instances": 11, "metric_value": 0.2727, "depth": 10}
										if obj[4]<=1:
											# {"feature": "Education", "instances": 8, "metric_value": 0.3, "depth": 11}
											if obj[5]<=2:
												# {"feature": "Gender", "instances": 5, "metric_value": 0.4, "depth": 12}
												if obj[3]<=0:
													return 'False'
												elif obj[3]>0:
													return 'False'
												else: return 'False'
											elif obj[5]>2:
												return 'False'
											else: return 'False'
										elif obj[4]>1:
											return 'True'
										else: return 'True'
									elif obj[7]<=1.0:
										return 'False'
									else: return 'False'
								else: return 'False'
							else: return 'True'
						else: return 'True'
					elif obj[6]>18.185882392956827:
						# {"feature": "Age", "instances": 119, "metric_value": 0.2638, "depth": 6}
						if obj[4]<=6:
							# {"feature": "Education", "instances": 111, "metric_value": 0.2413, "depth": 7}
							if obj[5]>0:
								# {"feature": "Time", "instances": 71, "metric_value": 0.2853, "depth": 8}
								if obj[1]>0:
									# {"feature": "Gender", "instances": 51, "metric_value": 0.3153, "depth": 9}
									if obj[3]>0:
										# {"feature": "Bar", "instances": 36, "metric_value": 0.1852, "depth": 10}
										if obj[7]>0.0:
											return 'True'
										elif obj[7]<=0.0:
											# {"feature": "Direction_same", "instances": 15, "metric_value": 0.4405, "depth": 11}
											if obj[10]<=0:
												# {"feature": "Restaurant20to50", "instances": 8, "metric_value": 0.4688, "depth": 12}
												if obj[9]<=1.0:
													return 'True'
												else: return 'True'
											elif obj[10]>0:
												# {"feature": "Restaurant20to50", "instances": 7, "metric_value": 0.4082, "depth": 12}
												if obj[9]<=1.0:
													return 'True'
												else: return 'True'
											else: return 'True'
										else: return 'True'
									elif obj[3]<=0:
										# {"feature": "Bar", "instances": 15, "metric_value": 0.3556, "depth": 10}
										if obj[7]<=2.0:
											# {"feature": "Restaurant20to50", "instances": 12, "metric_value": 0.4381, "depth": 11}
											if obj[9]<=1.0:
												# {"feature": "Direction_same", "instances": 7, "metric_value": 0.4048, "depth": 12}
												if obj[10]<=0:
													return 'True'
												elif obj[10]>0:
													return 'True'
												else: return 'True'
											elif obj[9]>1.0:
												# {"feature": "Direction_same", "instances": 5, "metric_value": 0.48, "depth": 12}
												if obj[10]<=0:
													return 'True'
												else: return 'True'
											else: return 'True'
										elif obj[7]>2.0:
											return 'False'
										else: return 'False'
									else: return 'True'
								elif obj[1]<=0:
									# {"feature": "Bar", "instances": 20, "metric_value": 0.0857, "depth": 9}
									if obj[7]>0.0:
										return 'True'
									elif obj[7]<=0.0:
										# {"feature": "Direction_same", "instances": 7, "metric_value": 0.2286, "depth": 10}
										if obj[10]<=0:
											# {"feature": "Gender", "instances": 5, "metric_value": 0.32, "depth": 11}
											if obj[3]<=1:
												# {"feature": "Restaurant20to50", "instances": 5, "metric_value": 0.32, "depth": 12}
												if obj[9]<=1.0:
													return 'True'
												else: return 'True'
											else: return 'True'
										elif obj[10]>0:
											return 'True'
										else: return 'True'
									else: return 'True'
								else: return 'True'
							elif obj[5]<=0:
								# {"feature": "Time", "instances": 40, "metric_value": 0.1234, "depth": 8}
								if obj[1]>0:
									# {"feature": "Restaurant20to50", "instances": 32, "metric_value": 0.0547, "depth": 9}
									if obj[9]>0.0:
										return 'True'
									elif obj[9]<=0.0:
										# {"feature": "Direction_same", "instances": 8, "metric_value": 0.2, "depth": 10}
										if obj[10]<=0:
											# {"feature": "Gender", "instances": 5, "metric_value": 0.32, "depth": 11}
											if obj[3]<=0:
												# {"feature": "Bar", "instances": 5, "metric_value": 0.32, "depth": 12}
												if obj[7]<=2.0:
													return 'True'
												else: return 'True'
											else: return 'True'
										elif obj[10]>0:
											return 'True'
										else: return 'True'
									else: return 'True'
								elif obj[1]<=0:
									# {"feature": "Restaurant20to50", "instances": 8, "metric_value": 0.3571, "depth": 9}
									if obj[9]>0.0:
										# {"feature": "Bar", "instances": 7, "metric_value": 0.3714, "depth": 10}
										if obj[7]<=0.0:
											# {"feature": "Direction_same", "instances": 5, "metric_value": 0.2667, "depth": 11}
											if obj[10]<=0:
												# {"feature": "Gender", "instances": 3, "metric_value": 0.4444, "depth": 12}
												if obj[3]<=1:
													return 'True'
												else: return 'True'
											elif obj[10]>0:
												return 'True'
											else: return 'True'
										elif obj[7]>0.0:
											# {"feature": "Direction_same", "instances": 2, "metric_value": 0.0, "depth": 11}
											if obj[10]>0:
												return 'False'
											elif obj[10]<=0:
												return 'True'
											else: return 'True'
										else: return 'False'
									elif obj[9]<=0.0:
										return 'True'
									else: return 'True'
								else: return 'True'
							else: return 'True'
						elif obj[4]>6:
							# {"feature": "Direction_same", "instances": 8, "metric_value": 0.375, "depth": 7}
							if obj[10]<=0:
								# {"feature": "Time", "instances": 4, "metric_value": 0.25, "depth": 8}
								if obj[1]>1:
									# {"feature": "Gender", "instances": 2, "metric_value": 0.5, "depth": 9}
									if obj[3]<=0:
										# {"feature": "Education", "instances": 2, "metric_value": 0.5, "depth": 10}
										if obj[5]<=0:
											# {"feature": "Bar", "instances": 2, "metric_value": 0.5, "depth": 11}
											if obj[7]<=3.0:
												# {"feature": "Restaurant20to50", "instances": 2, "metric_value": 0.5, "depth": 12}
												if obj[9]<=2.0:
													return 'True'
												else: return 'True'
											else: return 'True'
										else: return 'True'
									else: return 'True'
								elif obj[1]<=1:
									return 'True'
								else: return 'True'
							elif obj[10]>0:
								# {"feature": "Time", "instances": 4, "metric_value": 0.3333, "depth": 8}
								if obj[1]>0:
									# {"feature": "Gender", "instances": 3, "metric_value": 0.4444, "depth": 9}
									if obj[3]<=0:
										# {"feature": "Education", "instances": 3, "metric_value": 0.4444, "depth": 10}
										if obj[5]<=0:
											# {"feature": "Bar", "instances": 3, "metric_value": 0.4444, "depth": 11}
											if obj[7]<=3.0:
												# {"feature": "Restaurant20to50", "instances": 3, "metric_value": 0.4444, "depth": 12}
												if obj[9]<=2.0:
													return 'False'
												else: return 'False'
											else: return 'False'
										else: return 'False'
									else: return 'False'
								elif obj[1]<=0:
									return 'False'
								else: return 'False'
							else: return 'False'
						else: return 'True'
					else: return 'True'
				elif obj[0]>2:
					# {"feature": "Bar", "instances": 915, "metric_value": 0.3493, "depth": 5}
					if obj[7]<=3.0:
						# {"feature": "Time", "instances": 854, "metric_value": 0.3376, "depth": 6}
						if obj[1]<=2:
							# {"feature": "Age", "instances": 516, "metric_value": 0.2995, "depth": 7}
							if obj[4]<=5:
								# {"feature": "Occupation", "instances": 443, "metric_value": 0.2772, "depth": 8}
								if obj[6]>1:
									# {"feature": "Restaurant20to50", "instances": 394, "metric_value": 0.2966, "depth": 9}
									if obj[9]<=2.0:
										# {"feature": "Education", "instances": 360, "metric_value": 0.2768, "depth": 10}
										if obj[5]<=3:
											# {"feature": "Gender", "instances": 333, "metric_value": 0.2989, "depth": 11}
											if obj[3]<=0:
												# {"feature": "Direction_same", "instances": 168, "metric_value": 0.3157, "depth": 12}
												if obj[10]<=0:
													return 'True'
												else: return 'True'
											elif obj[3]>0:
												# {"feature": "Direction_same", "instances": 165, "metric_value": 0.2818, "depth": 12}
												if obj[10]<=0:
													return 'True'
												else: return 'True'
											else: return 'True'
										elif obj[5]>3:
											return 'True'
										else: return 'True'
									elif obj[9]>2.0:
										# {"feature": "Education", "instances": 34, "metric_value": 0.4452, "depth": 10}
										if obj[5]<=2:
											# {"feature": "Gender", "instances": 22, "metric_value": 0.4831, "depth": 11}
											if obj[3]<=0:
												# {"feature": "Direction_same", "instances": 15, "metric_value": 0.48, "depth": 12}
												if obj[10]<=0:
													return 'True'
												else: return 'True'
											elif obj[3]>0:
												# {"feature": "Direction_same", "instances": 7, "metric_value": 0.4898, "depth": 12}
												if obj[10]<=0:
													return 'True'
												else: return 'True'
											else: return 'True'
										elif obj[5]>2:
											# {"feature": "Gender", "instances": 12, "metric_value": 0.3125, "depth": 11}
											if obj[3]>0:
												# {"feature": "Direction_same", "instances": 8, "metric_value": 0.4688, "depth": 12}
												if obj[10]<=0:
													return 'True'
												else: return 'True'
											elif obj[3]<=0:
												return 'True'
											else: return 'True'
										else: return 'True'
									else: return 'True'
								elif obj[6]<=1:
									# {"feature": "Education", "instances": 49, "metric_value": 0.0583, "depth": 9}
									if obj[5]<=2:
										return 'True'
									elif obj[5]>2:
										# {"feature": "Restaurant20to50", "instances": 7, "metric_value": 0.2857, "depth": 10}
										if obj[9]<=1.0:
											# {"feature": "Gender", "instances": 4, "metric_value": 0.3333, "depth": 11}
											if obj[3]<=0:
												# {"feature": "Direction_same", "instances": 3, "metric_value": 0.4444, "depth": 12}
												if obj[10]<=0:
													return 'True'
												else: return 'True'
											elif obj[3]>0:
												return 'False'
											else: return 'False'
										elif obj[9]>1.0:
											return 'True'
										else: return 'True'
									else: return 'True'
								else: return 'True'
							elif obj[4]>5:
								# {"feature": "Occupation", "instances": 73, "metric_value": 0.4002, "depth": 8}
								if obj[6]<=13:
									# {"feature": "Restaurant20to50", "instances": 69, "metric_value": 0.4148, "depth": 9}
									if obj[9]>1.0:
										# {"feature": "Education", "instances": 37, "metric_value": 0.365, "depth": 10}
										if obj[5]>0:
											# {"feature": "Gender", "instances": 31, "metric_value": 0.3484, "depth": 11}
											if obj[3]<=0:
												# {"feature": "Direction_same", "instances": 16, "metric_value": 0.375, "depth": 12}
												if obj[10]<=0:
													return 'True'
												else: return 'True'
											elif obj[3]>0:
												# {"feature": "Direction_same", "instances": 15, "metric_value": 0.32, "depth": 12}
												if obj[10]<=0:
													return 'True'
												else: return 'True'
											else: return 'True'
										elif obj[5]<=0:
											# {"feature": "Gender", "instances": 6, "metric_value": 0.4444, "depth": 11}
											if obj[3]<=0:
												# {"feature": "Direction_same", "instances": 6, "metric_value": 0.4444, "depth": 12}
												if obj[10]<=0:
													return 'True'
												else: return 'True'
											else: return 'True'
										else: return 'True'
									elif obj[9]<=1.0:
										# {"feature": "Education", "instances": 32, "metric_value": 0.45, "depth": 10}
										if obj[5]<=2:
											# {"feature": "Gender", "instances": 27, "metric_value": 0.4242, "depth": 11}
											if obj[3]<=0:
												# {"feature": "Direction_same", "instances": 16, "metric_value": 0.375, "depth": 12}
												if obj[10]<=0:
													return 'True'
												else: return 'True'
											elif obj[3]>0:
												# {"feature": "Direction_same", "instances": 11, "metric_value": 0.4959, "depth": 12}
												if obj[10]<=0:
													return 'True'
												else: return 'True'
											else: return 'True'
										elif obj[5]>2:
											# {"feature": "Gender", "instances": 5, "metric_value": 0.3, "depth": 11}
											if obj[3]<=0:
												# {"feature": "Direction_same", "instances": 4, "metric_value": 0.375, "depth": 12}
												if obj[10]<=0:
													return 'False'
												else: return 'False'
											elif obj[3]>0:
												return 'True'
											else: return 'True'
										else: return 'False'
									else: return 'True'
								elif obj[6]>13:
									return 'True'
								else: return 'True'
							else: return 'True'
						elif obj[1]>2:
							# {"feature": "Age", "instances": 338, "metric_value": 0.3803, "depth": 7}
							if obj[4]<=3:
								# {"feature": "Education", "instances": 199, "metric_value": 0.4276, "depth": 8}
								if obj[5]<=2:
									# {"feature": "Occupation", "instances": 127, "metric_value": 0.3844, "depth": 9}
									if obj[6]>6:
										# {"feature": "Restaurant20to50", "instances": 67, "metric_value": 0.3116, "depth": 10}
										if obj[9]>0.0:
											# {"feature": "Gender", "instances": 66, "metric_value": 0.3141, "depth": 11}
											if obj[3]>0:
												# {"feature": "Direction_same", "instances": 41, "metric_value": 0.2832, "depth": 12}
												if obj[10]<=0:
													return 'True'
												else: return 'True'
											elif obj[3]<=0:
												# {"feature": "Direction_same", "instances": 25, "metric_value": 0.3648, "depth": 12}
												if obj[10]<=0:
													return 'True'
												else: return 'True'
											else: return 'True'
										elif obj[9]<=0.0:
											return 'False'
										else: return 'False'
									elif obj[6]<=6:
										# {"feature": "Gender", "instances": 60, "metric_value": 0.4159, "depth": 10}
										if obj[3]>0:
											# {"feature": "Restaurant20to50", "instances": 41, "metric_value": 0.4754, "depth": 11}
											if obj[9]<=2.0:
												# {"feature": "Direction_same", "instances": 38, "metric_value": 0.4778, "depth": 12}
												if obj[10]<=0:
													return 'True'
												else: return 'True'
											elif obj[9]>2.0:
												# {"feature": "Direction_same", "instances": 3, "metric_value": 0.4444, "depth": 12}
												if obj[10]<=0:
													return 'False'
												else: return 'False'
											else: return 'False'
										elif obj[3]<=0:
											# {"feature": "Restaurant20to50", "instances": 19, "metric_value": 0.2368, "depth": 11}
											if obj[9]<=1.0:
												# {"feature": "Direction_same", "instances": 12, "metric_value": 0.375, "depth": 12}
												if obj[10]<=0:
													return 'True'
												else: return 'True'
											elif obj[9]>1.0:
												return 'True'
											else: return 'True'
										else: return 'True'
									else: return 'True'
								elif obj[5]>2:
									# {"feature": "Occupation", "instances": 72, "metric_value": 0.4556, "depth": 9}
									if obj[6]<=9:
										# {"feature": "Restaurant20to50", "instances": 53, "metric_value": 0.4846, "depth": 10}
										if obj[9]>0.0:
											# {"feature": "Gender", "instances": 46, "metric_value": 0.4836, "depth": 11}
											if obj[3]>0:
												# {"feature": "Direction_same", "instances": 28, "metric_value": 0.477, "depth": 12}
												if obj[10]<=0:
													return 'False'
												else: return 'False'
											elif obj[3]<=0:
												# {"feature": "Direction_same", "instances": 18, "metric_value": 0.4938, "depth": 12}
												if obj[10]<=0:
													return 'True'
												else: return 'True'
											else: return 'True'
										elif obj[9]<=0.0:
											# {"feature": "Gender", "instances": 7, "metric_value": 0.4048, "depth": 11}
											if obj[3]>0:
												# {"feature": "Direction_same", "instances": 4, "metric_value": 0.375, "depth": 12}
												if obj[10]<=0:
													return 'True'
												else: return 'True'
											elif obj[3]<=0:
												# {"feature": "Direction_same", "instances": 3, "metric_value": 0.4444, "depth": 12}
												if obj[10]<=0:
													return 'True'
												else: return 'True'
											else: return 'True'
										else: return 'True'
									elif obj[6]>9:
										# {"feature": "Restaurant20to50", "instances": 19, "metric_value": 0.3158, "depth": 10}
										if obj[9]<=2.0:
											# {"feature": "Gender", "instances": 16, "metric_value": 0.373, "depth": 11}
											if obj[3]<=0:
												# {"feature": "Direction_same", "instances": 9, "metric_value": 0.3457, "depth": 12}
												if obj[10]<=0:
													return 'True'
												else: return 'True'
											elif obj[3]>0:
												# {"feature": "Direction_same", "instances": 7, "metric_value": 0.4082, "depth": 12}
												if obj[10]<=0:
													return 'True'
												else: return 'True'
											else: return 'True'
										elif obj[9]>2.0:
											return 'True'
										else: return 'True'
									else: return 'True'
								else: return 'True'
							elif obj[4]>3:
								# {"feature": "Restaurant20to50", "instances": 139, "metric_value": 0.2823, "depth": 8}
								if obj[9]>0.0:
									# {"feature": "Gender", "instances": 117, "metric_value": 0.2421, "depth": 9}
									if obj[3]<=0:
										# {"feature": "Education", "instances": 60, "metric_value": 0.3, "depth": 10}
										if obj[5]>1:
											# {"feature": "Occupation", "instances": 30, "metric_value": 0.3801, "depth": 11}
											if obj[6]<=7:
												# {"feature": "Direction_same", "instances": 17, "metric_value": 0.2907, "depth": 12}
												if obj[10]<=0:
													return 'True'
												else: return 'True'
											elif obj[6]>7:
												# {"feature": "Direction_same", "instances": 13, "metric_value": 0.497, "depth": 12}
												if obj[10]<=0:
													return 'True'
												else: return 'True'
											else: return 'True'
										elif obj[5]<=1:
											# {"feature": "Occupation", "instances": 30, "metric_value": 0.1727, "depth": 11}
											if obj[6]<=7:
												# {"feature": "Direction_same", "instances": 22, "metric_value": 0.2355, "depth": 12}
												if obj[10]<=0:
													return 'True'
												else: return 'True'
											elif obj[6]>7:
												return 'True'
											else: return 'True'
										else: return 'True'
									elif obj[3]>0:
										# {"feature": "Occupation", "instances": 57, "metric_value": 0.1496, "depth": 10}
										if obj[6]>3:
											# {"feature": "Education", "instances": 34, "metric_value": 0.232, "depth": 11}
											if obj[5]>1:
												# {"feature": "Direction_same", "instances": 18, "metric_value": 0.1049, "depth": 12}
												if obj[10]<=0:
													return 'True'
												else: return 'True'
											elif obj[5]<=1:
												# {"feature": "Direction_same", "instances": 16, "metric_value": 0.375, "depth": 12}
												if obj[10]<=0:
													return 'True'
												else: return 'True'
											else: return 'True'
										elif obj[6]<=3:
											return 'True'
										else: return 'True'
									else: return 'True'
								elif obj[9]<=0.0:
									# {"feature": "Occupation", "instances": 22, "metric_value": 0.3697, "depth": 9}
									if obj[6]>5:
										# {"feature": "Gender", "instances": 12, "metric_value": 0.2593, "depth": 10}
										if obj[3]<=0:
											# {"feature": "Education", "instances": 9, "metric_value": 0.1778, "depth": 11}
											if obj[5]>0:
												# {"feature": "Direction_same", "instances": 5, "metric_value": 0.32, "depth": 12}
												if obj[10]<=0:
													return 'True'
												else: return 'True'
											elif obj[5]<=0:
												return 'True'
											else: return 'True'
										elif obj[3]>0:
											# {"feature": "Education", "instances": 3, "metric_value": 0.3333, "depth": 11}
											if obj[5]<=0:
												# {"feature": "Direction_same", "instances": 2, "metric_value": 0.5, "depth": 12}
												if obj[10]<=0:
													return 'True'
												else: return 'True'
											elif obj[5]>0:
												return 'True'
											else: return 'True'
										else: return 'True'
									elif obj[6]<=5:
										# {"feature": "Education", "instances": 10, "metric_value": 0.3167, "depth": 10}
										if obj[5]<=0:
											# {"feature": "Gender", "instances": 6, "metric_value": 0.1667, "depth": 11}
											if obj[3]>0:
												return 'False'
											elif obj[3]<=0:
												# {"feature": "Direction_same", "instances": 2, "metric_value": 0.5, "depth": 12}
												if obj[10]<=0:
													return 'True'
												else: return 'True'
											else: return 'True'
										elif obj[5]>0:
											# {"feature": "Gender", "instances": 4, "metric_value": 0.25, "depth": 11}
											if obj[3]>0:
												return 'True'
											elif obj[3]<=0:
												# {"feature": "Direction_same", "instances": 2, "metric_value": 0.5, "depth": 12}
												if obj[10]<=0:
													return 'False'
												else: return 'False'
											else: return 'False'
										else: return 'True'
									else: return 'False'
								else: return 'True'
							else: return 'True'
						else: return 'True'
					elif obj[7]>3.0:
						# {"feature": "Time", "instances": 61, "metric_value": 0.4287, "depth": 6}
						if obj[1]>0:
							# {"feature": "Occupation", "instances": 49, "metric_value": 0.4074, "depth": 7}
							if obj[6]<=12:
								# {"feature": "Age", "instances": 36, "metric_value": 0.3333, "depth": 8}
								if obj[4]>0:
									# {"feature": "Education", "instances": 27, "metric_value": 0.4386, "depth": 9}
									if obj[5]>0:
										# {"feature": "Gender", "instances": 19, "metric_value": 0.4613, "depth": 10}
										if obj[3]<=0:
											# {"feature": "Restaurant20to50", "instances": 17, "metric_value": 0.4563, "depth": 11}
											if obj[9]>1.0:
												# {"feature": "Direction_same", "instances": 11, "metric_value": 0.4628, "depth": 12}
												if obj[10]<=0:
													return 'True'
												else: return 'True'
											elif obj[9]<=1.0:
												# {"feature": "Direction_same", "instances": 6, "metric_value": 0.4444, "depth": 12}
												if obj[10]<=0:
													return 'True'
												else: return 'True'
											else: return 'True'
										elif obj[3]>0:
											# {"feature": "Restaurant20to50", "instances": 2, "metric_value": 0.5, "depth": 11}
											if obj[9]<=4.0:
												# {"feature": "Direction_same", "instances": 2, "metric_value": 0.5, "depth": 12}
												if obj[10]<=0:
													return 'True'
												else: return 'True'
											else: return 'True'
										else: return 'True'
									elif obj[5]<=0:
										# {"feature": "Restaurant20to50", "instances": 8, "metric_value": 0.3333, "depth": 10}
										if obj[9]>0.0:
											# {"feature": "Gender", "instances": 6, "metric_value": 0.2778, "depth": 11}
											if obj[3]<=1:
												# {"feature": "Direction_same", "instances": 6, "metric_value": 0.2778, "depth": 12}
												if obj[10]<=0:
													return 'True'
												else: return 'True'
											else: return 'True'
										elif obj[9]<=0.0:
											# {"feature": "Gender", "instances": 2, "metric_value": 0.5, "depth": 11}
											if obj[3]<=1:
												# {"feature": "Direction_same", "instances": 2, "metric_value": 0.5, "depth": 12}
												if obj[10]<=0:
													return 'True'
												else: return 'True'
											else: return 'True'
										else: return 'True'
									else: return 'True'
								elif obj[4]<=0:
									return 'True'
								else: return 'True'
							elif obj[6]>12:
								# {"feature": "Gender", "instances": 13, "metric_value": 0.3916, "depth": 8}
								if obj[3]<=0:
									# {"feature": "Age", "instances": 11, "metric_value": 0.4606, "depth": 9}
									if obj[4]>1:
										# {"feature": "Education", "instances": 6, "metric_value": 0.4444, "depth": 10}
										if obj[5]<=0:
											# {"feature": "Restaurant20to50", "instances": 6, "metric_value": 0.4444, "depth": 11}
											if obj[9]<=1.0:
												# {"feature": "Direction_same", "instances": 6, "metric_value": 0.4444, "depth": 12}
												if obj[10]<=0:
													return 'True'
												else: return 'True'
											else: return 'True'
										else: return 'True'
									elif obj[4]<=1:
										# {"feature": "Education", "instances": 5, "metric_value": 0.48, "depth": 10}
										if obj[5]<=0:
											# {"feature": "Restaurant20to50", "instances": 5, "metric_value": 0.48, "depth": 11}
											if obj[9]<=4.0:
												# {"feature": "Direction_same", "instances": 5, "metric_value": 0.48, "depth": 12}
												if obj[10]<=0:
													return 'True'
												else: return 'True'
											else: return 'True'
										else: return 'True'
									else: return 'True'
								elif obj[3]>0:
									return 'False'
								else: return 'False'
							else: return 'True'
						elif obj[1]<=0:
							# {"feature": "Occupation", "instances": 12, "metric_value": 0.3333, "depth": 7}
							if obj[6]<=12:
								# {"feature": "Age", "instances": 8, "metric_value": 0.3333, "depth": 8}
								if obj[4]>0:
									# {"feature": "Gender", "instances": 6, "metric_value": 0.2667, "depth": 9}
									if obj[3]<=0:
										# {"feature": "Education", "instances": 5, "metric_value": 0.3, "depth": 10}
										if obj[5]>2:
											# {"feature": "Restaurant20to50", "instances": 4, "metric_value": 0.375, "depth": 11}
											if obj[9]<=4.0:
												# {"feature": "Direction_same", "instances": 4, "metric_value": 0.375, "depth": 12}
												if obj[10]<=0:
													return 'False'
												else: return 'False'
											else: return 'False'
										elif obj[5]<=2:
											return 'False'
										else: return 'False'
									elif obj[3]>0:
										return 'True'
									else: return 'True'
								elif obj[4]<=0:
									return 'True'
								else: return 'True'
							elif obj[6]>12:
								return 'False'
							else: return 'False'
						else: return 'False'
					else: return 'True'
				else: return 'True'
			elif obj[11]>2:
				# {"feature": "Age", "instances": 271, "metric_value": 0.4868, "depth": 4}
				if obj[4]<=5:
					# {"feature": "Passanger", "instances": 232, "metric_value": 0.4871, "depth": 5}
					if obj[0]>0:
						# {"feature": "Education", "instances": 223, "metric_value": 0.4918, "depth": 6}
						if obj[5]>1:
							# {"feature": "Occupation", "instances": 138, "metric_value": 0.4876, "depth": 7}
							if obj[6]<=16:
								# {"feature": "Bar", "instances": 122, "metric_value": 0.4891, "depth": 8}
								if obj[7]<=3.0:
									# {"feature": "Restaurant20to50", "instances": 118, "metric_value": 0.4822, "depth": 9}
									if obj[9]<=2.0:
										# {"feature": "Time", "instances": 108, "metric_value": 0.496, "depth": 10}
										if obj[1]>0:
											# {"feature": "Gender", "instances": 93, "metric_value": 0.4982, "depth": 11}
											if obj[3]>0:
												# {"feature": "Direction_same", "instances": 52, "metric_value": 0.497, "depth": 12}
												if obj[10]<=0:
													return 'False'
												else: return 'False'
											elif obj[3]<=0:
												# {"feature": "Direction_same", "instances": 41, "metric_value": 0.4997, "depth": 12}
												if obj[10]<=0:
													return 'False'
												else: return 'False'
											else: return 'False'
										elif obj[1]<=0:
											# {"feature": "Gender", "instances": 15, "metric_value": 0.4571, "depth": 11}
											if obj[3]<=0:
												# {"feature": "Direction_same", "instances": 8, "metric_value": 0.5, "depth": 12}
												if obj[10]<=0:
													return 'True'
												else: return 'True'
											elif obj[3]>0:
												# {"feature": "Direction_same", "instances": 7, "metric_value": 0.4082, "depth": 12}
												if obj[10]<=0:
													return 'False'
												else: return 'False'
											else: return 'False'
										else: return 'False'
									elif obj[9]>2.0:
										# {"feature": "Time", "instances": 10, "metric_value": 0.1333, "depth": 10}
										if obj[1]<=1:
											return 'False'
										elif obj[1]>1:
											# {"feature": "Gender", "instances": 3, "metric_value": 0.0, "depth": 11}
											if obj[3]<=0:
												return 'True'
											elif obj[3]>0:
												return 'False'
											else: return 'False'
										else: return 'True'
									else: return 'False'
								elif obj[7]>3.0:
									# {"feature": "Time", "instances": 4, "metric_value": 0.3333, "depth": 9}
									if obj[1]<=1:
										# {"feature": "Restaurant20to50", "instances": 3, "metric_value": 0.3333, "depth": 10}
										if obj[9]>1.0:
											# {"feature": "Gender", "instances": 2, "metric_value": 0.5, "depth": 11}
											if obj[3]<=0:
												# {"feature": "Direction_same", "instances": 2, "metric_value": 0.5, "depth": 12}
												if obj[10]<=0:
													return 'False'
												else: return 'False'
											else: return 'False'
										elif obj[9]<=1.0:
											return 'True'
										else: return 'True'
									elif obj[1]>1:
										return 'True'
									else: return 'True'
								else: return 'True'
							elif obj[6]>16:
								# {"feature": "Bar", "instances": 16, "metric_value": 0.4042, "depth": 8}
								if obj[7]>0.0:
									# {"feature": "Time", "instances": 10, "metric_value": 0.4, "depth": 9}
									if obj[1]>0:
										# {"feature": "Restaurant20to50", "instances": 9, "metric_value": 0.3333, "depth": 10}
										if obj[9]<=1.0:
											# {"feature": "Gender", "instances": 6, "metric_value": 0.25, "depth": 11}
											if obj[3]>0:
												# {"feature": "Direction_same", "instances": 4, "metric_value": 0.375, "depth": 12}
												if obj[10]<=0:
													return 'True'
												else: return 'True'
											elif obj[3]<=0:
												return 'True'
											else: return 'True'
										elif obj[9]>1.0:
											# {"feature": "Gender", "instances": 3, "metric_value": 0.0, "depth": 11}
											if obj[3]<=0:
												return 'False'
											elif obj[3]>0:
												return 'True'
											else: return 'True'
										else: return 'False'
									elif obj[1]<=0:
										return 'False'
									else: return 'False'
								elif obj[7]<=0.0:
									# {"feature": "Time", "instances": 6, "metric_value": 0.25, "depth": 9}
									if obj[1]>0:
										# {"feature": "Restaurant20to50", "instances": 4, "metric_value": 0.3333, "depth": 10}
										if obj[9]<=1.0:
											# {"feature": "Gender", "instances": 3, "metric_value": 0.4444, "depth": 11}
											if obj[3]<=1:
												# {"feature": "Direction_same", "instances": 3, "metric_value": 0.4444, "depth": 12}
												if obj[10]<=0:
													return 'True'
												else: return 'True'
											else: return 'True'
										elif obj[9]>1.0:
											return 'True'
										else: return 'True'
									elif obj[1]<=0:
										return 'True'
									else: return 'True'
								else: return 'True'
							else: return 'True'
						elif obj[5]<=1:
							# {"feature": "Occupation", "instances": 85, "metric_value": 0.4649, "depth": 7}
							if obj[6]>4:
								# {"feature": "Gender", "instances": 59, "metric_value": 0.481, "depth": 8}
								if obj[3]<=0:
									# {"feature": "Restaurant20to50", "instances": 34, "metric_value": 0.4361, "depth": 9}
									if obj[9]<=1.0:
										# {"feature": "Bar", "instances": 26, "metric_value": 0.4154, "depth": 10}
										if obj[7]>0.0:
											# {"feature": "Time", "instances": 16, "metric_value": 0.3, "depth": 11}
											if obj[1]>0:
												# {"feature": "Direction_same", "instances": 15, "metric_value": 0.32, "depth": 12}
												if obj[10]<=0:
													return 'True'
												else: return 'True'
											elif obj[1]<=0:
												return 'False'
											else: return 'False'
										elif obj[7]<=0.0:
											# {"feature": "Time", "instances": 10, "metric_value": 0.4, "depth": 11}
											if obj[1]>0:
												# {"feature": "Direction_same", "instances": 8, "metric_value": 0.5, "depth": 12}
												if obj[10]<=0:
													return 'False'
												else: return 'False'
											elif obj[1]<=0:
												return 'True'
											else: return 'True'
										else: return 'True'
									elif obj[9]>1.0:
										# {"feature": "Time", "instances": 8, "metric_value": 0.2083, "depth": 10}
										if obj[1]>0:
											# {"feature": "Bar", "instances": 6, "metric_value": 0.2222, "depth": 11}
											if obj[7]>0.0:
												# {"feature": "Direction_same", "instances": 3, "metric_value": 0.4444, "depth": 12}
												if obj[10]<=0:
													return 'False'
												else: return 'False'
											elif obj[7]<=0.0:
												return 'False'
											else: return 'False'
										elif obj[1]<=0:
											return 'True'
										else: return 'True'
									else: return 'False'
								elif obj[3]>0:
									# {"feature": "Time", "instances": 25, "metric_value": 0.419, "depth": 9}
									if obj[1]>0:
										# {"feature": "Restaurant20to50", "instances": 21, "metric_value": 0.4698, "depth": 10}
										if obj[9]>0.0:
											# {"feature": "Bar", "instances": 15, "metric_value": 0.44, "depth": 11}
											if obj[7]<=1.0:
												# {"feature": "Direction_same", "instances": 10, "metric_value": 0.5, "depth": 12}
												if obj[10]<=0:
													return 'False'
												else: return 'False'
											elif obj[7]>1.0:
												# {"feature": "Direction_same", "instances": 5, "metric_value": 0.32, "depth": 12}
												if obj[10]<=0:
													return 'True'
												else: return 'True'
											else: return 'True'
										elif obj[9]<=0.0:
											# {"feature": "Bar", "instances": 6, "metric_value": 0.2222, "depth": 11}
											if obj[7]<=0.0:
												# {"feature": "Direction_same", "instances": 3, "metric_value": 0.4444, "depth": 12}
												if obj[10]<=0:
													return 'True'
												else: return 'True'
											elif obj[7]>0.0:
												return 'False'
											else: return 'False'
										else: return 'False'
									elif obj[1]<=0:
										return 'False'
									else: return 'False'
								else: return 'False'
							elif obj[6]<=4:
								# {"feature": "Time", "instances": 26, "metric_value": 0.3615, "depth": 8}
								if obj[1]<=1:
									# {"feature": "Bar", "instances": 20, "metric_value": 0.3059, "depth": 9}
									if obj[7]<=2.0:
										# {"feature": "Restaurant20to50", "instances": 17, "metric_value": 0.3451, "depth": 10}
										if obj[9]<=2.0:
											# {"feature": "Gender", "instances": 15, "metric_value": 0.3909, "depth": 11}
											if obj[3]>0:
												# {"feature": "Direction_same", "instances": 11, "metric_value": 0.3967, "depth": 12}
												if obj[10]<=0:
													return 'True'
												else: return 'True'
											elif obj[3]<=0:
												# {"feature": "Direction_same", "instances": 4, "metric_value": 0.375, "depth": 12}
												if obj[10]<=0:
													return 'True'
												else: return 'True'
											else: return 'True'
										elif obj[9]>2.0:
											return 'True'
										else: return 'True'
									elif obj[7]>2.0:
										return 'True'
									else: return 'True'
								elif obj[1]>1:
									# {"feature": "Bar", "instances": 6, "metric_value": 0.4, "depth": 9}
									if obj[7]<=1.0:
										# {"feature": "Restaurant20to50", "instances": 5, "metric_value": 0.3, "depth": 10}
										if obj[9]<=2.0:
											# {"feature": "Gender", "instances": 4, "metric_value": 0.3333, "depth": 11}
											if obj[3]>0:
												# {"feature": "Direction_same", "instances": 3, "metric_value": 0.4444, "depth": 12}
												if obj[10]<=0:
													return 'False'
												else: return 'False'
											elif obj[3]<=0:
												return 'False'
											else: return 'False'
										elif obj[9]>2.0:
											return 'True'
										else: return 'True'
									elif obj[7]>1.0:
										return 'True'
									else: return 'True'
								else: return 'True'
							else: return 'True'
						else: return 'True'
					elif obj[0]<=0:
						# {"feature": "Gender", "instances": 9, "metric_value": 0.1481, "depth": 6}
						if obj[3]>0:
							return 'True'
						elif obj[3]<=0:
							# {"feature": "Occupation", "instances": 3, "metric_value": 0.0, "depth": 7}
							if obj[6]<=5:
								return 'True'
							elif obj[6]>5:
								return 'False'
							else: return 'False'
						else: return 'True'
					else: return 'True'
				elif obj[4]>5:
					# {"feature": "Education", "instances": 39, "metric_value": 0.3199, "depth": 5}
					if obj[5]>0:
						# {"feature": "Bar", "instances": 29, "metric_value": 0.2188, "depth": 6}
						if obj[7]<=1.0:
							# {"feature": "Occupation", "instances": 20, "metric_value": 0.075, "depth": 7}
							if obj[6]<=10:
								return 'False'
							elif obj[6]>10:
								# {"feature": "Restaurant20to50", "instances": 4, "metric_value": 0.3333, "depth": 8}
								if obj[9]>1.0:
									# {"feature": "Passanger", "instances": 3, "metric_value": 0.4444, "depth": 9}
									if obj[0]<=1:
										# {"feature": "Time", "instances": 3, "metric_value": 0.4444, "depth": 10}
										if obj[1]<=1:
											# {"feature": "Gender", "instances": 3, "metric_value": 0.4444, "depth": 11}
											if obj[3]<=0:
												# {"feature": "Direction_same", "instances": 3, "metric_value": 0.4444, "depth": 12}
												if obj[10]<=0:
													return 'False'
												else: return 'False'
											else: return 'False'
										else: return 'False'
									else: return 'False'
								elif obj[9]<=1.0:
									return 'False'
								else: return 'False'
							else: return 'False'
						elif obj[7]>1.0:
							# {"feature": "Occupation", "instances": 9, "metric_value": 0.3444, "depth": 7}
							if obj[6]>11:
								# {"feature": "Time", "instances": 5, "metric_value": 0.0, "depth": 8}
								if obj[1]<=1:
									return 'False'
								elif obj[1]>1:
									return 'True'
								else: return 'True'
							elif obj[6]<=11:
								# {"feature": "Gender", "instances": 4, "metric_value": 0.0, "depth": 8}
								if obj[3]<=0:
									return 'True'
								elif obj[3]>0:
									return 'False'
								else: return 'False'
							else: return 'True'
						else: return 'False'
					elif obj[5]<=0:
						# {"feature": "Time", "instances": 10, "metric_value": 0.175, "depth": 6}
						if obj[1]<=1:
							# {"feature": "Bar", "instances": 8, "metric_value": 0.1875, "depth": 7}
							if obj[7]<=0.0:
								return 'True'
							elif obj[7]>0.0:
								# {"feature": "Gender", "instances": 4, "metric_value": 0.3333, "depth": 8}
								if obj[3]<=0:
									# {"feature": "Occupation", "instances": 3, "metric_value": 0.3333, "depth": 9}
									if obj[6]<=6:
										# {"feature": "Passanger", "instances": 2, "metric_value": 0.5, "depth": 10}
										if obj[0]<=1:
											# {"feature": "Restaurant20to50", "instances": 2, "metric_value": 0.5, "depth": 11}
											if obj[9]<=1.0:
												# {"feature": "Direction_same", "instances": 2, "metric_value": 0.5, "depth": 12}
												if obj[10]<=0:
													return 'False'
												else: return 'False'
											else: return 'False'
										else: return 'False'
									elif obj[6]>6:
										return 'True'
									else: return 'True'
								elif obj[3]>0:
									return 'True'
								else: return 'True'
							else: return 'True'
						elif obj[1]>1:
							return 'False'
						else: return 'False'
					else: return 'True'
				else: return 'False'
			else: return 'True'
		else: return 'True'
	elif obj[2]<=1:
		# {"feature": "Bar", "instances": 2244, "metric_value": 0.4571, "depth": 2}
		if obj[7]<=1.0:
			# {"feature": "Passanger", "instances": 1582, "metric_value": 0.4435, "depth": 3}
			if obj[0]<=2:
				# {"feature": "Education", "instances": 1363, "metric_value": 0.4284, "depth": 4}
				if obj[5]>0:
					# {"feature": "Time", "instances": 875, "metric_value": 0.3931, "depth": 5}
					if obj[1]>0:
						# {"feature": "Gender", "instances": 584, "metric_value": 0.353, "depth": 6}
						if obj[3]>0:
							# {"feature": "Occupation", "instances": 345, "metric_value": 0.3081, "depth": 7}
							if obj[6]<=6:
								# {"feature": "Age", "instances": 198, "metric_value": 0.2489, "depth": 8}
								if obj[4]<=6:
									# {"feature": "Restaurant20to50", "instances": 189, "metric_value": 0.2332, "depth": 9}
									if obj[9]>0.0:
										# {"feature": "Distance", "instances": 159, "metric_value": 0.2603, "depth": 10}
										if obj[11]>1:
											# {"feature": "Coffeehouse", "instances": 111, "metric_value": 0.3041, "depth": 11}
											if obj[8]<=3.0:
												# {"feature": "Direction_same", "instances": 99, "metric_value": 0.3199, "depth": 12}
												if obj[10]<=0:
													return 'False'
												elif obj[10]>0:
													return 'False'
												else: return 'False'
											elif obj[8]>3.0:
												# {"feature": "Direction_same", "instances": 12, "metric_value": 0.15, "depth": 12}
												if obj[10]<=0:
													return 'False'
												elif obj[10]>0:
													return 'False'
												else: return 'False'
											else: return 'False'
										elif obj[11]<=1:
											# {"feature": "Coffeehouse", "instances": 48, "metric_value": 0.1452, "depth": 11}
											if obj[8]>1.0:
												# {"feature": "Direction_same", "instances": 31, "metric_value": 0.2168, "depth": 12}
												if obj[10]<=0:
													return 'False'
												elif obj[10]>0:
													return 'False'
												else: return 'False'
											elif obj[8]<=1.0:
												return 'False'
											else: return 'False'
										else: return 'False'
									elif obj[9]<=0.0:
										# {"feature": "Distance", "instances": 30, "metric_value": 0.0606, "depth": 10}
										if obj[11]>1:
											return 'False'
										elif obj[11]<=1:
											# {"feature": "Coffeehouse", "instances": 11, "metric_value": 0.1515, "depth": 11}
											if obj[8]<=0.0:
												# {"feature": "Direction_same", "instances": 6, "metric_value": 0.2778, "depth": 12}
												if obj[10]<=0:
													return 'False'
												else: return 'False'
											elif obj[8]>0.0:
												return 'False'
											else: return 'False'
										else: return 'False'
									else: return 'False'
								elif obj[4]>6:
									# {"feature": "Restaurant20to50", "instances": 9, "metric_value": 0.381, "depth": 9}
									if obj[9]<=0.0:
										# {"feature": "Distance", "instances": 7, "metric_value": 0.4762, "depth": 10}
										if obj[11]>1:
											# {"feature": "Coffeehouse", "instances": 4, "metric_value": 0.5, "depth": 11}
											if obj[8]>0.0:
												# {"feature": "Direction_same", "instances": 2, "metric_value": 0.5, "depth": 12}
												if obj[10]<=0:
													return 'True'
												else: return 'True'
											elif obj[8]<=0.0:
												# {"feature": "Direction_same", "instances": 2, "metric_value": 0.5, "depth": 12}
												if obj[10]<=0:
													return 'True'
												else: return 'True'
											else: return 'True'
										elif obj[11]<=1:
											# {"feature": "Coffeehouse", "instances": 3, "metric_value": 0.4444, "depth": 11}
											if obj[8]<=0.0:
												# {"feature": "Direction_same", "instances": 3, "metric_value": 0.4444, "depth": 12}
												if obj[10]<=0:
													return 'True'
												else: return 'True'
											else: return 'True'
										else: return 'True'
									elif obj[9]>0.0:
										return 'False'
									else: return 'False'
								else: return 'False'
							elif obj[6]>6:
								# {"feature": "Age", "instances": 147, "metric_value": 0.365, "depth": 8}
								if obj[4]>1:
									# {"feature": "Coffeehouse", "instances": 93, "metric_value": 0.3041, "depth": 9}
									if obj[8]<=3.0:
										# {"feature": "Restaurant20to50", "instances": 84, "metric_value": 0.3297, "depth": 10}
										if obj[9]>-1.0:
											# {"feature": "Distance", "instances": 78, "metric_value": 0.3516, "depth": 11}
											if obj[11]>1:
												# {"feature": "Direction_same", "instances": 50, "metric_value": 0.3179, "depth": 12}
												if obj[10]<=0:
													return 'False'
												elif obj[10]>0:
													return 'False'
												else: return 'False'
											elif obj[11]<=1:
												# {"feature": "Direction_same", "instances": 28, "metric_value": 0.4011, "depth": 12}
												if obj[10]<=0:
													return 'False'
												elif obj[10]>0:
													return 'True'
												else: return 'True'
											else: return 'False'
										elif obj[9]<=-1.0:
											return 'False'
										else: return 'False'
									elif obj[8]>3.0:
										return 'False'
									else: return 'False'
								elif obj[4]<=1:
									# {"feature": "Restaurant20to50", "instances": 54, "metric_value": 0.401, "depth": 9}
									if obj[9]<=1.0:
										# {"feature": "Direction_same", "instances": 46, "metric_value": 0.3849, "depth": 10}
										if obj[10]<=0:
											# {"feature": "Coffeehouse", "instances": 43, "metric_value": 0.3509, "depth": 11}
											if obj[8]<=1.0:
												# {"feature": "Distance", "instances": 22, "metric_value": 0.2288, "depth": 12}
												if obj[11]>1:
													return 'False'
												elif obj[11]<=1:
													return 'False'
												else: return 'False'
											elif obj[8]>1.0:
												# {"feature": "Distance", "instances": 21, "metric_value": 0.4512, "depth": 12}
												if obj[11]<=2:
													return 'False'
												elif obj[11]>2:
													return 'False'
												else: return 'False'
											else: return 'False'
										elif obj[10]>0:
											# {"feature": "Coffeehouse", "instances": 3, "metric_value": 0.0, "depth": 11}
											if obj[8]>0.0:
												return 'True'
											elif obj[8]<=0.0:
												return 'False'
											else: return 'False'
										else: return 'True'
									elif obj[9]>1.0:
										# {"feature": "Distance", "instances": 8, "metric_value": 0.3333, "depth": 10}
										if obj[11]<=2:
											# {"feature": "Coffeehouse", "instances": 6, "metric_value": 0.2778, "depth": 11}
											if obj[8]<=1.0:
												# {"feature": "Direction_same", "instances": 6, "metric_value": 0.2778, "depth": 12}
												if obj[10]<=0:
													return 'True'
												else: return 'True'
											else: return 'True'
										elif obj[11]>2:
											# {"feature": "Coffeehouse", "instances": 2, "metric_value": 0.0, "depth": 11}
											if obj[8]<=1.0:
												return 'False'
											elif obj[8]>1.0:
												return 'True'
											else: return 'True'
										else: return 'False'
									else: return 'True'
								else: return 'False'
							else: return 'False'
						elif obj[3]<=0:
							# {"feature": "Occupation", "instances": 239, "metric_value": 0.401, "depth": 7}
							if obj[6]<=8:
								# {"feature": "Age", "instances": 145, "metric_value": 0.4428, "depth": 8}
								if obj[4]<=5:
									# {"feature": "Restaurant20to50", "instances": 113, "metric_value": 0.4636, "depth": 9}
									if obj[9]<=1.0:
										# {"feature": "Direction_same", "instances": 72, "metric_value": 0.4303, "depth": 10}
										if obj[10]<=0:
											# {"feature": "Coffeehouse", "instances": 63, "metric_value": 0.4122, "depth": 11}
											if obj[8]<=2.0:
												# {"feature": "Distance", "instances": 55, "metric_value": 0.4368, "depth": 12}
												if obj[11]>1:
													return 'False'
												elif obj[11]<=1:
													return 'False'
												else: return 'False'
											elif obj[8]>2.0:
												# {"feature": "Distance", "instances": 8, "metric_value": 0.1875, "depth": 12}
												if obj[11]>2:
													return 'False'
												elif obj[11]<=2:
													return 'False'
												else: return 'False'
											else: return 'False'
										elif obj[10]>0:
											# {"feature": "Coffeehouse", "instances": 9, "metric_value": 0.4444, "depth": 11}
											if obj[8]<=1.0:
												# {"feature": "Distance", "instances": 6, "metric_value": 0.2667, "depth": 12}
												if obj[11]>1:
													return 'True'
												elif obj[11]<=1:
													return 'False'
												else: return 'False'
											elif obj[8]>1.0:
												# {"feature": "Distance", "instances": 3, "metric_value": 0.0, "depth": 12}
												if obj[11]>1:
													return 'False'
												elif obj[11]<=1:
													return 'True'
												else: return 'True'
											else: return 'False'
										else: return 'True'
									elif obj[9]>1.0:
										# {"feature": "Coffeehouse", "instances": 41, "metric_value": 0.4829, "depth": 10}
										if obj[8]<=2.0:
											# {"feature": "Direction_same", "instances": 40, "metric_value": 0.4771, "depth": 11}
											if obj[10]<=0:
												# {"feature": "Distance", "instances": 35, "metric_value": 0.4788, "depth": 12}
												if obj[11]>1:
													return 'False'
												elif obj[11]<=1:
													return 'True'
												else: return 'True'
											elif obj[10]>0:
												# {"feature": "Distance", "instances": 5, "metric_value": 0.3, "depth": 12}
												if obj[11]>1:
													return 'False'
												elif obj[11]<=1:
													return 'False'
												else: return 'False'
											else: return 'False'
										elif obj[8]>2.0:
											return 'True'
										else: return 'True'
									else: return 'False'
								elif obj[4]>5:
									# {"feature": "Distance", "instances": 32, "metric_value": 0.3099, "depth": 9}
									if obj[11]<=2:
										# {"feature": "Restaurant20to50", "instances": 24, "metric_value": 0.3977, "depth": 10}
										if obj[9]>0.0:
											# {"feature": "Direction_same", "instances": 22, "metric_value": 0.4136, "depth": 11}
											if obj[10]<=0:
												# {"feature": "Coffeehouse", "instances": 20, "metric_value": 0.4421, "depth": 12}
												if obj[8]<=2.0:
													return 'False'
												elif obj[8]>2.0:
													return 'False'
												else: return 'False'
											elif obj[10]>0:
												return 'False'
											else: return 'False'
										elif obj[9]<=0.0:
											return 'False'
										else: return 'False'
									elif obj[11]>2:
										return 'False'
									else: return 'False'
								else: return 'False'
							elif obj[6]>8:
								# {"feature": "Coffeehouse", "instances": 94, "metric_value": 0.3044, "depth": 8}
								if obj[8]<=1.0:
									# {"feature": "Distance", "instances": 65, "metric_value": 0.2214, "depth": 9}
									if obj[11]<=2:
										# {"feature": "Restaurant20to50", "instances": 53, "metric_value": 0.1651, "depth": 10}
										if obj[9]>0.0:
											# {"feature": "Age", "instances": 40, "metric_value": 0.2097, "depth": 11}
											if obj[4]>0:
												# {"feature": "Direction_same", "instances": 31, "metric_value": 0.27, "depth": 12}
												if obj[10]<=0:
													return 'False'
												elif obj[10]>0:
													return 'False'
												else: return 'False'
											elif obj[4]<=0:
												return 'False'
											else: return 'False'
										elif obj[9]<=0.0:
											return 'False'
										else: return 'False'
									elif obj[11]>2:
										# {"feature": "Age", "instances": 12, "metric_value": 0.3704, "depth": 10}
										if obj[4]<=4:
											# {"feature": "Restaurant20to50", "instances": 9, "metric_value": 0.3175, "depth": 11}
											if obj[9]<=1.0:
												# {"feature": "Direction_same", "instances": 7, "metric_value": 0.4082, "depth": 12}
												if obj[10]<=0:
													return 'False'
												else: return 'False'
											elif obj[9]>1.0:
												return 'True'
											else: return 'True'
										elif obj[4]>4:
											return 'False'
										else: return 'False'
									else: return 'False'
								elif obj[8]>1.0:
									# {"feature": "Age", "instances": 29, "metric_value": 0.42, "depth": 9}
									if obj[4]>2:
										# {"feature": "Distance", "instances": 15, "metric_value": 0.4103, "depth": 10}
										if obj[11]>1:
											# {"feature": "Restaurant20to50", "instances": 13, "metric_value": 0.4573, "depth": 11}
											if obj[9]>1.0:
												# {"feature": "Direction_same", "instances": 9, "metric_value": 0.4938, "depth": 12}
												if obj[10]<=0:
													return 'False'
												else: return 'False'
											elif obj[9]<=1.0:
												# {"feature": "Direction_same", "instances": 4, "metric_value": 0.375, "depth": 12}
												if obj[10]<=0:
													return 'False'
												else: return 'False'
											else: return 'False'
										elif obj[11]<=1:
											return 'True'
										else: return 'True'
									elif obj[4]<=2:
										# {"feature": "Restaurant20to50", "instances": 14, "metric_value": 0.3155, "depth": 10}
										if obj[9]>1.0:
											# {"feature": "Distance", "instances": 8, "metric_value": 0.1667, "depth": 11}
											if obj[11]>1:
												return 'False'
											elif obj[11]<=1:
												# {"feature": "Direction_same", "instances": 3, "metric_value": 0.4444, "depth": 12}
												if obj[10]<=0:
													return 'False'
												else: return 'False'
											else: return 'False'
										elif obj[9]<=1.0:
											# {"feature": "Distance", "instances": 6, "metric_value": 0.3333, "depth": 11}
											if obj[11]>1:
												# {"feature": "Direction_same", "instances": 4, "metric_value": 0.5, "depth": 12}
												if obj[10]<=0:
													return 'False'
												else: return 'False'
											elif obj[11]<=1:
												return 'False'
											else: return 'False'
										else: return 'False'
									else: return 'False'
								else: return 'False'
							else: return 'False'
						else: return 'False'
					elif obj[1]<=0:
						# {"feature": "Coffeehouse", "instances": 291, "metric_value": 0.4584, "depth": 6}
						if obj[8]<=2.0:
							# {"feature": "Occupation", "instances": 235, "metric_value": 0.4724, "depth": 7}
							if obj[6]<=13.79717461950581:
								# {"feature": "Restaurant20to50", "instances": 198, "metric_value": 0.4822, "depth": 8}
								if obj[9]>0.0:
									# {"feature": "Gender", "instances": 150, "metric_value": 0.4851, "depth": 9}
									if obj[3]<=0:
										# {"feature": "Age", "instances": 85, "metric_value": 0.4937, "depth": 10}
										if obj[4]<=5:
											# {"feature": "Direction_same", "instances": 61, "metric_value": 0.4811, "depth": 11}
											if obj[10]<=0:
												# {"feature": "Distance", "instances": 32, "metric_value": 0.4511, "depth": 12}
												if obj[11]>1:
													return 'True'
												elif obj[11]<=1:
													return 'False'
												else: return 'False'
											elif obj[10]>0:
												# {"feature": "Distance", "instances": 29, "metric_value": 0.4937, "depth": 12}
												if obj[11]<=1:
													return 'False'
												elif obj[11]>1:
													return 'False'
												else: return 'False'
											else: return 'False'
										elif obj[4]>5:
											# {"feature": "Distance", "instances": 24, "metric_value": 0.4545, "depth": 11}
											if obj[11]<=2:
												# {"feature": "Direction_same", "instances": 22, "metric_value": 0.4817, "depth": 12}
												if obj[10]<=0:
													return 'False'
												elif obj[10]>0:
													return 'True'
												else: return 'True'
											elif obj[11]>2:
												return 'False'
											else: return 'False'
										else: return 'False'
									elif obj[3]>0:
										# {"feature": "Distance", "instances": 65, "metric_value": 0.4528, "depth": 10}
										if obj[11]>1:
											# {"feature": "Direction_same", "instances": 42, "metric_value": 0.4073, "depth": 11}
											if obj[10]<=0:
												# {"feature": "Age", "instances": 38, "metric_value": 0.4271, "depth": 12}
												if obj[4]>1:
													return 'False'
												elif obj[4]<=1:
													return 'True'
												else: return 'True'
											elif obj[10]>0:
												return 'False'
											else: return 'False'
										elif obj[11]<=1:
											# {"feature": "Direction_same", "instances": 23, "metric_value": 0.4771, "depth": 11}
											if obj[10]>0:
												# {"feature": "Age", "instances": 19, "metric_value": 0.4678, "depth": 12}
												if obj[4]<=6:
													return 'True'
												elif obj[4]>6:
													return 'False'
												else: return 'False'
											elif obj[10]<=0:
												# {"feature": "Age", "instances": 4, "metric_value": 0.25, "depth": 12}
												if obj[4]>2:
													return 'False'
												elif obj[4]<=2:
													return 'False'
												else: return 'False'
											else: return 'False'
										else: return 'False'
									else: return 'False'
								elif obj[9]<=0.0:
									# {"feature": "Age", "instances": 48, "metric_value": 0.4167, "depth": 9}
									if obj[4]>1:
										# {"feature": "Gender", "instances": 32, "metric_value": 0.3157, "depth": 10}
										if obj[3]>0:
											# {"feature": "Distance", "instances": 17, "metric_value": 0.4759, "depth": 11}
											if obj[11]>1:
												# {"feature": "Direction_same", "instances": 11, "metric_value": 0.4364, "depth": 12}
												if obj[10]<=0:
													return 'False'
												elif obj[10]>0:
													return 'False'
												else: return 'False'
											elif obj[11]<=1:
												# {"feature": "Direction_same", "instances": 6, "metric_value": 0.4, "depth": 12}
												if obj[10]>0:
													return 'False'
												elif obj[10]<=0:
													return 'True'
												else: return 'True'
											else: return 'False'
										elif obj[3]<=0:
											# {"feature": "Direction_same", "instances": 15, "metric_value": 0.1185, "depth": 11}
											if obj[10]<=0:
												# {"feature": "Distance", "instances": 9, "metric_value": 0.1944, "depth": 12}
												if obj[11]<=2:
													return 'False'
												elif obj[11]>2:
													return 'False'
												else: return 'False'
											elif obj[10]>0:
												return 'False'
											else: return 'False'
										else: return 'False'
									elif obj[4]<=1:
										# {"feature": "Gender", "instances": 16, "metric_value": 0.4583, "depth": 10}
										if obj[3]>0:
											# {"feature": "Direction_same", "instances": 12, "metric_value": 0.4815, "depth": 11}
											if obj[10]<=0:
												# {"feature": "Distance", "instances": 9, "metric_value": 0.4938, "depth": 12}
												if obj[11]<=2:
													return 'False'
												else: return 'False'
											elif obj[10]>0:
												# {"feature": "Distance", "instances": 3, "metric_value": 0.4444, "depth": 12}
												if obj[11]<=1:
													return 'False'
												else: return 'False'
											else: return 'False'
										elif obj[3]<=0:
											# {"feature": "Direction_same", "instances": 4, "metric_value": 0.25, "depth": 11}
											if obj[10]<=0:
												# {"feature": "Distance", "instances": 2, "metric_value": 0.5, "depth": 12}
												if obj[11]<=2:
													return 'False'
												else: return 'False'
											elif obj[10]>0:
												return 'True'
											else: return 'True'
										else: return 'True'
									else: return 'False'
								else: return 'False'
							elif obj[6]>13.79717461950581:
								# {"feature": "Restaurant20to50", "instances": 37, "metric_value": 0.3605, "depth": 8}
								if obj[9]<=1.0:
									# {"feature": "Age", "instances": 32, "metric_value": 0.3024, "depth": 9}
									if obj[4]>0:
										# {"feature": "Gender", "instances": 31, "metric_value": 0.3099, "depth": 10}
										if obj[3]>0:
											# {"feature": "Direction_same", "instances": 18, "metric_value": 0.3426, "depth": 11}
											if obj[10]<=0:
												# {"feature": "Distance", "instances": 12, "metric_value": 0.375, "depth": 12}
												if obj[11]<=2:
													return 'False'
												elif obj[11]>2:
													return 'False'
												else: return 'False'
											elif obj[10]>0:
												# {"feature": "Distance", "instances": 6, "metric_value": 0.2667, "depth": 12}
												if obj[11]<=1:
													return 'False'
												elif obj[11]>1:
													return 'False'
												else: return 'False'
											else: return 'False'
										elif obj[3]<=0:
											# {"feature": "Distance", "instances": 13, "metric_value": 0.2564, "depth": 11}
											if obj[11]<=2:
												# {"feature": "Direction_same", "instances": 12, "metric_value": 0.2778, "depth": 12}
												if obj[10]>0:
													return 'False'
												elif obj[10]<=0:
													return 'False'
												else: return 'False'
											elif obj[11]>2:
												return 'False'
											else: return 'False'
										else: return 'False'
									elif obj[4]<=0:
										return 'True'
									else: return 'True'
								elif obj[9]>1.0:
									# {"feature": "Direction_same", "instances": 5, "metric_value": 0.2667, "depth": 9}
									if obj[10]>0:
										# {"feature": "Age", "instances": 3, "metric_value": 0.0, "depth": 10}
										if obj[4]<=2:
											return 'False'
										elif obj[4]>2:
											return 'True'
										else: return 'True'
									elif obj[10]<=0:
										return 'True'
									else: return 'True'
								else: return 'True'
							else: return 'False'
						elif obj[8]>2.0:
							# {"feature": "Direction_same", "instances": 56, "metric_value": 0.3174, "depth": 7}
							if obj[10]>0:
								# {"feature": "Age", "instances": 29, "metric_value": 0.4108, "depth": 8}
								if obj[4]>2:
									# {"feature": "Occupation", "instances": 15, "metric_value": 0.32, "depth": 9}
									if obj[6]<=7:
										# {"feature": "Restaurant20to50", "instances": 10, "metric_value": 0.4444, "depth": 10}
										if obj[9]>0.0:
											# {"feature": "Gender", "instances": 9, "metric_value": 0.4921, "depth": 11}
											if obj[3]>0:
												# {"feature": "Distance", "instances": 7, "metric_value": 0.4898, "depth": 12}
												if obj[11]<=1:
													return 'False'
												else: return 'False'
											elif obj[3]<=0:
												# {"feature": "Distance", "instances": 2, "metric_value": 0.5, "depth": 12}
												if obj[11]<=1:
													return 'True'
												else: return 'True'
											else: return 'True'
										elif obj[9]<=0.0:
											return 'False'
										else: return 'False'
									elif obj[6]>7:
										return 'True'
									else: return 'True'
								elif obj[4]<=2:
									# {"feature": "Occupation", "instances": 14, "metric_value": 0.2857, "depth": 9}
									if obj[6]<=7:
										# {"feature": "Restaurant20to50", "instances": 9, "metric_value": 0.4167, "depth": 10}
										if obj[9]>0.0:
											# {"feature": "Gender", "instances": 8, "metric_value": 0.4583, "depth": 11}
											if obj[3]>0:
												# {"feature": "Distance", "instances": 6, "metric_value": 0.4444, "depth": 12}
												if obj[11]>1:
													return 'False'
												elif obj[11]<=1:
													return 'False'
												else: return 'False'
											elif obj[3]<=0:
												# {"feature": "Distance", "instances": 2, "metric_value": 0.5, "depth": 12}
												if obj[11]<=1:
													return 'True'
												else: return 'True'
											else: return 'True'
										elif obj[9]<=0.0:
											return 'False'
										else: return 'False'
									elif obj[6]>7:
										return 'False'
									else: return 'False'
								else: return 'False'
							elif obj[10]<=0:
								# {"feature": "Occupation", "instances": 27, "metric_value": 0.1204, "depth": 8}
								if obj[6]<=11:
									# {"feature": "Age", "instances": 24, "metric_value": 0.0758, "depth": 9}
									if obj[4]<=2:
										return 'False'
									elif obj[4]>2:
										# {"feature": "Restaurant20to50", "instances": 11, "metric_value": 0.1591, "depth": 10}
										if obj[9]<=1.0:
											# {"feature": "Distance", "instances": 8, "metric_value": 0.2143, "depth": 11}
											if obj[11]>1:
												# {"feature": "Gender", "instances": 7, "metric_value": 0.2449, "depth": 12}
												if obj[3]<=1:
													return 'False'
												else: return 'False'
											elif obj[11]<=1:
												return 'False'
											else: return 'False'
										elif obj[9]>1.0:
											return 'False'
										else: return 'False'
									else: return 'False'
								elif obj[6]>11:
									# {"feature": "Age", "instances": 3, "metric_value": 0.3333, "depth": 9}
									if obj[4]>1:
										# {"feature": "Restaurant20to50", "instances": 2, "metric_value": 0.0, "depth": 10}
										if obj[9]>1.0:
											return 'True'
										elif obj[9]<=1.0:
											return 'False'
										else: return 'False'
									elif obj[4]<=1:
										return 'False'
									else: return 'False'
								else: return 'False'
							else: return 'False'
						else: return 'False'
					else: return 'False'
				elif obj[5]<=0:
					# {"feature": "Occupation", "instances": 488, "metric_value": 0.4614, "depth": 5}
					if obj[6]>1.348010951701891:
						# {"feature": "Coffeehouse", "instances": 406, "metric_value": 0.4828, "depth": 6}
						if obj[8]<=3.0:
							# {"feature": "Restaurant20to50", "instances": 359, "metric_value": 0.4908, "depth": 7}
							if obj[9]<=2.0:
								# {"feature": "Time", "instances": 338, "metric_value": 0.4892, "depth": 8}
								if obj[1]<=2:
									# {"feature": "Distance", "instances": 224, "metric_value": 0.4909, "depth": 9}
									if obj[11]<=2:
										# {"feature": "Age", "instances": 167, "metric_value": 0.4859, "depth": 10}
										if obj[4]<=5:
											# {"feature": "Direction_same", "instances": 145, "metric_value": 0.4917, "depth": 11}
											if obj[10]<=0:
												# {"feature": "Gender", "instances": 84, "metric_value": 0.4907, "depth": 12}
												if obj[3]>0:
													return 'True'
												elif obj[3]<=0:
													return 'False'
												else: return 'False'
											elif obj[10]>0:
												# {"feature": "Gender", "instances": 61, "metric_value": 0.4807, "depth": 12}
												if obj[3]<=0:
													return 'False'
												elif obj[3]>0:
													return 'False'
												else: return 'False'
											else: return 'False'
										elif obj[4]>5:
											# {"feature": "Direction_same", "instances": 22, "metric_value": 0.3939, "depth": 11}
											if obj[10]<=0:
												# {"feature": "Gender", "instances": 16, "metric_value": 0.373, "depth": 12}
												if obj[3]<=0:
													return 'True'
												elif obj[3]>0:
													return 'True'
												else: return 'True'
											elif obj[10]>0:
												# {"feature": "Gender", "instances": 6, "metric_value": 0.4444, "depth": 12}
												if obj[3]>0:
													return 'True'
												elif obj[3]<=0:
													return 'True'
												else: return 'True'
											else: return 'True'
										else: return 'True'
									elif obj[11]>2:
										# {"feature": "Age", "instances": 57, "metric_value": 0.4393, "depth": 10}
										if obj[4]<=6:
											# {"feature": "Gender", "instances": 52, "metric_value": 0.4764, "depth": 11}
											if obj[3]<=0:
												# {"feature": "Direction_same", "instances": 28, "metric_value": 0.4592, "depth": 12}
												if obj[10]<=0:
													return 'False'
												else: return 'False'
											elif obj[3]>0:
												# {"feature": "Direction_same", "instances": 24, "metric_value": 0.4965, "depth": 12}
												if obj[10]<=0:
													return 'False'
												else: return 'False'
											else: return 'False'
										elif obj[4]>6:
											return 'False'
										else: return 'False'
									else: return 'False'
								elif obj[1]>2:
									# {"feature": "Age", "instances": 114, "metric_value": 0.4574, "depth": 9}
									if obj[4]<=3:
										# {"feature": "Gender", "instances": 57, "metric_value": 0.4015, "depth": 10}
										if obj[3]>0:
											# {"feature": "Distance", "instances": 35, "metric_value": 0.4648, "depth": 11}
											if obj[11]<=1:
												# {"feature": "Direction_same", "instances": 20, "metric_value": 0.48, "depth": 12}
												if obj[10]<=0:
													return 'False'
												else: return 'False'
											elif obj[11]>1:
												# {"feature": "Direction_same", "instances": 15, "metric_value": 0.4444, "depth": 12}
												if obj[10]<=0:
													return 'False'
												else: return 'False'
											else: return 'False'
										elif obj[3]<=0:
											# {"feature": "Distance", "instances": 22, "metric_value": 0.2864, "depth": 11}
											if obj[11]>1:
												# {"feature": "Direction_same", "instances": 12, "metric_value": 0.375, "depth": 12}
												if obj[10]<=0:
													return 'False'
												else: return 'False'
											elif obj[11]<=1:
												# {"feature": "Direction_same", "instances": 10, "metric_value": 0.18, "depth": 12}
												if obj[10]<=0:
													return 'False'
												else: return 'False'
											else: return 'False'
										else: return 'False'
									elif obj[4]>3:
										# {"feature": "Direction_same", "instances": 57, "metric_value": 0.4922, "depth": 10}
										if obj[10]<=0:
											# {"feature": "Gender", "instances": 52, "metric_value": 0.4867, "depth": 11}
											if obj[3]<=0:
												# {"feature": "Distance", "instances": 26, "metric_value": 0.48, "depth": 12}
												if obj[11]<=2:
													return 'True'
												elif obj[11]>2:
													return 'False'
												else: return 'False'
											elif obj[3]>0:
												# {"feature": "Distance", "instances": 26, "metric_value": 0.4431, "depth": 12}
												if obj[11]<=2:
													return 'False'
												elif obj[11]>2:
													return 'True'
												else: return 'True'
											else: return 'False'
										elif obj[10]>0:
											# {"feature": "Gender", "instances": 5, "metric_value": 0.4667, "depth": 11}
											if obj[3]>0:
												# {"feature": "Distance", "instances": 3, "metric_value": 0.4444, "depth": 12}
												if obj[11]<=2:
													return 'True'
												else: return 'True'
											elif obj[3]<=0:
												# {"feature": "Distance", "instances": 2, "metric_value": 0.5, "depth": 12}
												if obj[11]<=2:
													return 'False'
												else: return 'False'
											else: return 'False'
										else: return 'True'
									else: return 'False'
								else: return 'False'
							elif obj[9]>2.0:
								# {"feature": "Age", "instances": 21, "metric_value": 0.3083, "depth": 8}
								if obj[4]>0:
									# {"feature": "Distance", "instances": 16, "metric_value": 0.2727, "depth": 9}
									if obj[11]>1:
										# {"feature": "Direction_same", "instances": 11, "metric_value": 0.3737, "depth": 10}
										if obj[10]<=0:
											# {"feature": "Time", "instances": 9, "metric_value": 0.3016, "depth": 11}
											if obj[1]>0:
												# {"feature": "Gender", "instances": 7, "metric_value": 0.2449, "depth": 12}
												if obj[3]<=1:
													return 'True'
												else: return 'True'
											elif obj[1]<=0:
												# {"feature": "Gender", "instances": 2, "metric_value": 0.5, "depth": 12}
												if obj[3]<=1:
													return 'True'
												else: return 'True'
											else: return 'True'
										elif obj[10]>0:
											# {"feature": "Time", "instances": 2, "metric_value": 0.0, "depth": 11}
											if obj[1]>0:
												return 'False'
											elif obj[1]<=0:
												return 'True'
											else: return 'True'
										else: return 'False'
									elif obj[11]<=1:
										return 'True'
									else: return 'True'
								elif obj[4]<=0:
									# {"feature": "Time", "instances": 5, "metric_value": 0.0, "depth": 9}
									if obj[1]<=2:
										return 'False'
									elif obj[1]>2:
										return 'True'
									else: return 'True'
								else: return 'False'
							else: return 'True'
						elif obj[8]>3.0:
							# {"feature": "Distance", "instances": 47, "metric_value": 0.343, "depth": 7}
							if obj[11]>1:
								# {"feature": "Time", "instances": 28, "metric_value": 0.2286, "depth": 8}
								if obj[1]>0:
									# {"feature": "Direction_same", "instances": 20, "metric_value": 0.3, "depth": 9}
									if obj[10]<=0:
										# {"feature": "Age", "instances": 16, "metric_value": 0.3667, "depth": 10}
										if obj[4]<=5:
											# {"feature": "Restaurant20to50", "instances": 15, "metric_value": 0.381, "depth": 11}
											if obj[9]<=2.0:
												# {"feature": "Gender", "instances": 14, "metric_value": 0.4071, "depth": 12}
												if obj[3]>0:
													return 'False'
												elif obj[3]<=0:
													return 'False'
												else: return 'False'
											elif obj[9]>2.0:
												return 'False'
											else: return 'False'
										elif obj[4]>5:
											return 'False'
										else: return 'False'
									elif obj[10]>0:
										return 'False'
									else: return 'False'
								elif obj[1]<=0:
									return 'False'
								else: return 'False'
							elif obj[11]<=1:
								# {"feature": "Restaurant20to50", "instances": 19, "metric_value": 0.427, "depth": 8}
								if obj[9]<=1.0:
									# {"feature": "Time", "instances": 11, "metric_value": 0.3636, "depth": 9}
									if obj[1]>0:
										# {"feature": "Direction_same", "instances": 9, "metric_value": 0.3333, "depth": 10}
										if obj[10]<=0:
											# {"feature": "Age", "instances": 8, "metric_value": 0.3333, "depth": 11}
											if obj[4]<=5:
												# {"feature": "Gender", "instances": 6, "metric_value": 0.1667, "depth": 12}
												if obj[3]<=0:
													return 'False'
												elif obj[3]>0:
													return 'False'
												else: return 'False'
											elif obj[4]>5:
												# {"feature": "Gender", "instances": 2, "metric_value": 0.0, "depth": 12}
												if obj[3]>0:
													return 'False'
												elif obj[3]<=0:
													return 'True'
												else: return 'True'
											else: return 'False'
										elif obj[10]>0:
											return 'True'
										else: return 'True'
									elif obj[1]<=0:
										return 'False'
									else: return 'False'
								elif obj[9]>1.0:
									# {"feature": "Time", "instances": 8, "metric_value": 0.3571, "depth": 9}
									if obj[1]<=2:
										# {"feature": "Age", "instances": 7, "metric_value": 0.4048, "depth": 10}
										if obj[4]>3:
											# {"feature": "Direction_same", "instances": 4, "metric_value": 0.0, "depth": 11}
											if obj[10]<=0:
												return 'True'
											elif obj[10]>0:
												return 'False'
											else: return 'False'
										elif obj[4]<=3:
											# {"feature": "Direction_same", "instances": 3, "metric_value": 0.0, "depth": 11}
											if obj[10]>0:
												return 'True'
											elif obj[10]<=0:
												return 'False'
											else: return 'False'
										else: return 'True'
									elif obj[1]>2:
										return 'False'
									else: return 'False'
								else: return 'True'
							else: return 'False'
						else: return 'False'
					elif obj[6]<=1.348010951701891:
						# {"feature": "Coffeehouse", "instances": 82, "metric_value": 0.2475, "depth": 6}
						if obj[8]<=2.0:
							# {"feature": "Restaurant20to50", "instances": 74, "metric_value": 0.194, "depth": 7}
							if obj[9]<=1.0:
								# {"feature": "Age", "instances": 67, "metric_value": 0.1562, "depth": 8}
								if obj[4]>1:
									# {"feature": "Time", "instances": 47, "metric_value": 0.2197, "depth": 9}
									if obj[1]<=3:
										# {"feature": "Direction_same", "instances": 43, "metric_value": 0.2377, "depth": 10}
										if obj[10]<=0:
											# {"feature": "Gender", "instances": 31, "metric_value": 0.2615, "depth": 11}
											if obj[3]>0:
												# {"feature": "Distance", "instances": 24, "metric_value": 0.2, "depth": 12}
												if obj[11]<=2:
													return 'False'
												elif obj[11]>2:
													return 'False'
												else: return 'False'
											elif obj[3]<=0:
												# {"feature": "Distance", "instances": 7, "metric_value": 0.4048, "depth": 12}
												if obj[11]>1:
													return 'False'
												elif obj[11]<=1:
													return 'False'
												else: return 'False'
											else: return 'False'
										elif obj[10]>0:
											# {"feature": "Distance", "instances": 12, "metric_value": 0.1333, "depth": 11}
											if obj[11]<=1:
												return 'False'
											elif obj[11]>1:
												# {"feature": "Gender", "instances": 5, "metric_value": 0.3, "depth": 12}
												if obj[3]>0:
													return 'False'
												elif obj[3]<=0:
													return 'False'
												else: return 'False'
											else: return 'False'
										else: return 'False'
									elif obj[1]>3:
										return 'False'
									else: return 'False'
								elif obj[4]<=1:
									return 'False'
								else: return 'False'
							elif obj[9]>1.0:
								# {"feature": "Gender", "instances": 7, "metric_value": 0.0, "depth": 8}
								if obj[3]>0:
									return 'True'
								elif obj[3]<=0:
									return 'False'
								else: return 'False'
							else: return 'True'
						elif obj[8]>2.0:
							# {"feature": "Time", "instances": 8, "metric_value": 0.1667, "depth": 7}
							if obj[1]<=1:
								return 'True'
							elif obj[1]>1:
								# {"feature": "Gender", "instances": 3, "metric_value": 0.0, "depth": 8}
								if obj[3]>0:
									return 'False'
								elif obj[3]<=0:
									return 'True'
								else: return 'True'
							else: return 'False'
						else: return 'True'
					else: return 'False'
				else: return 'False'
			elif obj[0]>2:
				# {"feature": "Age", "instances": 219, "metric_value": 0.4854, "depth": 4}
				if obj[4]>2:
					# {"feature": "Restaurant20to50", "instances": 123, "metric_value": 0.4675, "depth": 5}
					if obj[9]<=1.0:
						# {"feature": "Occupation", "instances": 86, "metric_value": 0.4791, "depth": 6}
						if obj[6]>0:
							# {"feature": "Education", "instances": 83, "metric_value": 0.4877, "depth": 7}
							if obj[5]<=2:
								# {"feature": "Time", "instances": 64, "metric_value": 0.4763, "depth": 8}
								if obj[1]>0:
									# {"feature": "Distance", "instances": 62, "metric_value": 0.486, "depth": 9}
									if obj[11]>1:
										# {"feature": "Coffeehouse", "instances": 49, "metric_value": 0.4694, "depth": 10}
										if obj[8]>0.0:
											# {"feature": "Gender", "instances": 27, "metric_value": 0.4242, "depth": 11}
											if obj[3]>0:
												# {"feature": "Direction_same", "instances": 16, "metric_value": 0.375, "depth": 12}
												if obj[10]<=0:
													return 'False'
												else: return 'False'
											elif obj[3]<=0:
												# {"feature": "Direction_same", "instances": 11, "metric_value": 0.4959, "depth": 12}
												if obj[10]<=0:
													return 'False'
												else: return 'False'
											else: return 'False'
										elif obj[8]<=0.0:
											# {"feature": "Gender", "instances": 22, "metric_value": 0.381, "depth": 11}
											if obj[3]<=0:
												# {"feature": "Direction_same", "instances": 15, "metric_value": 0.4444, "depth": 12}
												if obj[10]<=0:
													return 'False'
												else: return 'False'
											elif obj[3]>0:
												# {"feature": "Direction_same", "instances": 7, "metric_value": 0.2449, "depth": 12}
												if obj[10]<=0:
													return 'True'
												else: return 'True'
											else: return 'True'
										else: return 'False'
									elif obj[11]<=1:
										# {"feature": "Coffeehouse", "instances": 13, "metric_value": 0.3916, "depth": 10}
										if obj[8]<=2.0:
											# {"feature": "Gender", "instances": 11, "metric_value": 0.4416, "depth": 11}
											if obj[3]<=0:
												# {"feature": "Direction_same", "instances": 7, "metric_value": 0.4082, "depth": 12}
												if obj[10]<=0:
													return 'True'
												else: return 'True'
											elif obj[3]>0:
												# {"feature": "Direction_same", "instances": 4, "metric_value": 0.5, "depth": 12}
												if obj[10]<=0:
													return 'True'
												else: return 'True'
											else: return 'True'
										elif obj[8]>2.0:
											return 'False'
										else: return 'False'
									else: return 'True'
								elif obj[1]<=0:
									return 'False'
								else: return 'False'
							elif obj[5]>2:
								# {"feature": "Time", "instances": 19, "metric_value": 0.4087, "depth": 8}
								if obj[1]<=3:
									# {"feature": "Coffeehouse", "instances": 17, "metric_value": 0.3494, "depth": 9}
									if obj[8]<=2.0:
										# {"feature": "Gender", "instances": 11, "metric_value": 0.2803, "depth": 10}
										if obj[3]>0:
											# {"feature": "Direction_same", "instances": 8, "metric_value": 0.2188, "depth": 11}
											if obj[10]<=0:
												# {"feature": "Distance", "instances": 8, "metric_value": 0.2188, "depth": 12}
												if obj[11]<=2:
													return 'True'
												else: return 'True'
											else: return 'True'
										elif obj[3]<=0:
											# {"feature": "Direction_same", "instances": 3, "metric_value": 0.4444, "depth": 11}
											if obj[10]<=0:
												# {"feature": "Distance", "instances": 3, "metric_value": 0.4444, "depth": 12}
												if obj[11]<=2:
													return 'True'
												else: return 'True'
											else: return 'True'
										else: return 'True'
									elif obj[8]>2.0:
										# {"feature": "Gender", "instances": 6, "metric_value": 0.4, "depth": 10}
										if obj[3]>0:
											# {"feature": "Direction_same", "instances": 5, "metric_value": 0.48, "depth": 11}
											if obj[10]<=0:
												# {"feature": "Distance", "instances": 5, "metric_value": 0.48, "depth": 12}
												if obj[11]<=2:
													return 'False'
												else: return 'False'
											else: return 'False'
										elif obj[3]<=0:
											return 'False'
										else: return 'False'
									else: return 'False'
								elif obj[1]>3:
									return 'False'
								else: return 'False'
							else: return 'True'
						elif obj[6]<=0:
							return 'True'
						else: return 'True'
					elif obj[9]>1.0:
						# {"feature": "Education", "instances": 37, "metric_value": 0.3326, "depth": 6}
						if obj[5]>0:
							# {"feature": "Coffeehouse", "instances": 26, "metric_value": 0.4431, "depth": 7}
							if obj[8]>-1.0:
								# {"feature": "Time", "instances": 25, "metric_value": 0.4383, "depth": 8}
								if obj[1]<=3:
									# {"feature": "Occupation", "instances": 23, "metric_value": 0.456, "depth": 9}
									if obj[6]<=9:
										# {"feature": "Gender", "instances": 18, "metric_value": 0.4938, "depth": 10}
										if obj[3]>0:
											# {"feature": "Direction_same", "instances": 9, "metric_value": 0.4938, "depth": 11}
											if obj[10]<=0:
												# {"feature": "Distance", "instances": 9, "metric_value": 0.4938, "depth": 12}
												if obj[11]<=2:
													return 'True'
												else: return 'True'
											else: return 'True'
										elif obj[3]<=0:
											# {"feature": "Direction_same", "instances": 9, "metric_value": 0.4938, "depth": 11}
											if obj[10]<=0:
												# {"feature": "Distance", "instances": 9, "metric_value": 0.4938, "depth": 12}
												if obj[11]<=2:
													return 'True'
												else: return 'True'
											else: return 'True'
										else: return 'True'
									elif obj[6]>9:
										# {"feature": "Gender", "instances": 5, "metric_value": 0.2667, "depth": 10}
										if obj[3]<=0:
											# {"feature": "Direction_same", "instances": 3, "metric_value": 0.4444, "depth": 11}
											if obj[10]<=0:
												# {"feature": "Distance", "instances": 3, "metric_value": 0.4444, "depth": 12}
												if obj[11]<=2:
													return 'True'
												else: return 'True'
											else: return 'True'
										elif obj[3]>0:
											return 'True'
										else: return 'True'
									else: return 'True'
								elif obj[1]>3:
									return 'True'
								else: return 'True'
							elif obj[8]<=-1.0:
								return 'False'
							else: return 'False'
						elif obj[5]<=0:
							return 'True'
						else: return 'True'
					else: return 'True'
				elif obj[4]<=2:
					# {"feature": "Education", "instances": 96, "metric_value": 0.4495, "depth": 5}
					if obj[5]<=2:
						# {"feature": "Restaurant20to50", "instances": 76, "metric_value": 0.4171, "depth": 6}
						if obj[9]>-1.0:
							# {"feature": "Time", "instances": 74, "metric_value": 0.4109, "depth": 7}
							if obj[1]>2:
								# {"feature": "Coffeehouse", "instances": 52, "metric_value": 0.3537, "depth": 8}
								if obj[8]<=3.0:
									# {"feature": "Occupation", "instances": 49, "metric_value": 0.3231, "depth": 9}
									if obj[6]<=21:
										# {"feature": "Gender", "instances": 48, "metric_value": 0.3241, "depth": 10}
										if obj[3]>0:
											# {"feature": "Distance", "instances": 30, "metric_value": 0.2716, "depth": 11}
											if obj[11]>1:
												# {"feature": "Direction_same", "instances": 27, "metric_value": 0.3018, "depth": 12}
												if obj[10]<=0:
													return 'False'
												else: return 'False'
											elif obj[11]<=1:
												return 'False'
											else: return 'False'
										elif obj[3]<=0:
											# {"feature": "Distance", "instances": 18, "metric_value": 0.4, "depth": 11}
											if obj[11]>1:
												# {"feature": "Direction_same", "instances": 15, "metric_value": 0.3911, "depth": 12}
												if obj[10]<=0:
													return 'False'
												else: return 'False'
											elif obj[11]<=1:
												# {"feature": "Direction_same", "instances": 3, "metric_value": 0.4444, "depth": 12}
												if obj[10]<=0:
													return 'False'
												else: return 'False'
											else: return 'False'
										else: return 'False'
									elif obj[6]>21:
										return 'True'
									else: return 'True'
								elif obj[8]>3.0:
									# {"feature": "Gender", "instances": 3, "metric_value": 0.0, "depth": 9}
									if obj[3]<=0:
										return 'True'
									elif obj[3]>0:
										return 'False'
									else: return 'False'
								else: return 'True'
							elif obj[1]<=2:
								# {"feature": "Coffeehouse", "instances": 22, "metric_value": 0.4306, "depth": 8}
								if obj[8]<=2.0:
									# {"feature": "Occupation", "instances": 19, "metric_value": 0.4451, "depth": 9}
									if obj[6]<=12:
										# {"feature": "Gender", "instances": 14, "metric_value": 0.4898, "depth": 10}
										if obj[3]<=0:
											# {"feature": "Direction_same", "instances": 7, "metric_value": 0.4898, "depth": 11}
											if obj[10]<=0:
												# {"feature": "Distance", "instances": 7, "metric_value": 0.4898, "depth": 12}
												if obj[11]<=2:
													return 'False'
												else: return 'False'
											else: return 'False'
										elif obj[3]>0:
											# {"feature": "Direction_same", "instances": 7, "metric_value": 0.4898, "depth": 11}
											if obj[10]<=0:
												# {"feature": "Distance", "instances": 7, "metric_value": 0.4898, "depth": 12}
												if obj[11]<=2:
													return 'False'
												else: return 'False'
											else: return 'False'
										else: return 'False'
									elif obj[6]>12:
										# {"feature": "Gender", "instances": 5, "metric_value": 0.2667, "depth": 10}
										if obj[3]<=0:
											# {"feature": "Direction_same", "instances": 3, "metric_value": 0.4444, "depth": 11}
											if obj[10]<=0:
												# {"feature": "Distance", "instances": 3, "metric_value": 0.4444, "depth": 12}
												if obj[11]<=2:
													return 'True'
												else: return 'True'
											else: return 'True'
										elif obj[3]>0:
											return 'True'
										else: return 'True'
									else: return 'True'
								elif obj[8]>2.0:
									return 'False'
								else: return 'False'
							else: return 'False'
						elif obj[9]<=-1.0:
							return 'True'
						else: return 'True'
					elif obj[5]>2:
						# {"feature": "Coffeehouse", "instances": 20, "metric_value": 0.4, "depth": 6}
						if obj[8]<=3.0:
							# {"feature": "Restaurant20to50", "instances": 18, "metric_value": 0.3922, "depth": 7}
							if obj[9]>-1.0:
								# {"feature": "Occupation", "instances": 17, "metric_value": 0.3644, "depth": 8}
								if obj[6]<=6:
									# {"feature": "Time", "instances": 9, "metric_value": 0.4815, "depth": 9}
									if obj[1]>2:
										# {"feature": "Gender", "instances": 6, "metric_value": 0.4, "depth": 10}
										if obj[3]<=0:
											# {"feature": "Distance", "instances": 5, "metric_value": 0.4667, "depth": 11}
											if obj[11]>1:
												# {"feature": "Direction_same", "instances": 3, "metric_value": 0.4444, "depth": 12}
												if obj[10]<=0:
													return 'True'
												else: return 'True'
											elif obj[11]<=1:
												# {"feature": "Direction_same", "instances": 2, "metric_value": 0.5, "depth": 12}
												if obj[10]<=0:
													return 'True'
												else: return 'True'
											else: return 'True'
										elif obj[3]>0:
											return 'False'
										else: return 'False'
									elif obj[1]<=2:
										# {"feature": "Gender", "instances": 3, "metric_value": 0.3333, "depth": 10}
										if obj[3]<=0:
											# {"feature": "Direction_same", "instances": 2, "metric_value": 0.5, "depth": 11}
											if obj[10]<=0:
												# {"feature": "Distance", "instances": 2, "metric_value": 0.5, "depth": 12}
												if obj[11]<=2:
													return 'True'
												else: return 'True'
											else: return 'True'
										elif obj[3]>0:
											return 'True'
										else: return 'True'
									else: return 'True'
								elif obj[6]>6:
									# {"feature": "Time", "instances": 8, "metric_value": 0.125, "depth": 9}
									if obj[1]>2:
										return 'True'
									elif obj[1]<=2:
										# {"feature": "Gender", "instances": 2, "metric_value": 0.0, "depth": 10}
										if obj[3]>0:
											return 'True'
										elif obj[3]<=0:
											return 'False'
										else: return 'False'
									else: return 'True'
								else: return 'True'
							elif obj[9]<=-1.0:
								return 'False'
							else: return 'False'
						elif obj[8]>3.0:
							return 'False'
						else: return 'False'
					else: return 'True'
				else: return 'False'
			else: return 'False'
		elif obj[7]>1.0:
			# {"feature": "Restaurant20to50", "instances": 662, "metric_value": 0.4594, "depth": 3}
			if obj[9]<=1.0:
				# {"feature": "Passanger", "instances": 355, "metric_value": 0.4904, "depth": 4}
				if obj[0]<=2:
					# {"feature": "Time", "instances": 290, "metric_value": 0.4838, "depth": 5}
					if obj[1]<=2:
						# {"feature": "Occupation", "instances": 202, "metric_value": 0.4801, "depth": 6}
						if obj[6]<=13.60630442015693:
							# {"feature": "Gender", "instances": 170, "metric_value": 0.4739, "depth": 7}
							if obj[3]<=0:
								# {"feature": "Coffeehouse", "instances": 102, "metric_value": 0.4471, "depth": 8}
								if obj[8]>1.0:
									# {"feature": "Distance", "instances": 61, "metric_value": 0.4486, "depth": 9}
									if obj[11]<=2:
										# {"feature": "Direction_same", "instances": 45, "metric_value": 0.4864, "depth": 10}
										if obj[10]<=0:
											# {"feature": "Education", "instances": 27, "metric_value": 0.4167, "depth": 11}
											if obj[5]<=2:
												# {"feature": "Age", "instances": 24, "metric_value": 0.4348, "depth": 12}
												if obj[4]>0:
													return 'False'
												elif obj[4]<=0:
													return 'True'
												else: return 'True'
											elif obj[5]>2:
												return 'True'
											else: return 'True'
										elif obj[10]>0:
											# {"feature": "Age", "instances": 18, "metric_value": 0.4314, "depth": 11}
											if obj[4]>0:
												# {"feature": "Education", "instances": 17, "metric_value": 0.4044, "depth": 12}
												if obj[5]<=3:
													return 'True'
												elif obj[5]>3:
													return 'False'
												else: return 'False'
											elif obj[4]<=0:
												return 'False'
											else: return 'False'
										else: return 'True'
									elif obj[11]>2:
										# {"feature": "Age", "instances": 16, "metric_value": 0.2768, "depth": 10}
										if obj[4]<=4:
											# {"feature": "Education", "instances": 14, "metric_value": 0.2286, "depth": 11}
											if obj[5]>0:
												# {"feature": "Direction_same", "instances": 10, "metric_value": 0.32, "depth": 12}
												if obj[10]<=0:
													return 'True'
												else: return 'True'
											elif obj[5]<=0:
												return 'True'
											else: return 'True'
										elif obj[4]>4:
											# {"feature": "Education", "instances": 2, "metric_value": 0.5, "depth": 11}
											if obj[5]<=0:
												# {"feature": "Direction_same", "instances": 2, "metric_value": 0.5, "depth": 12}
												if obj[10]<=0:
													return 'True'
												else: return 'True'
											else: return 'True'
										else: return 'True'
									else: return 'True'
								elif obj[8]<=1.0:
									# {"feature": "Distance", "instances": 41, "metric_value": 0.3579, "depth": 9}
									if obj[11]<=2:
										# {"feature": "Age", "instances": 28, "metric_value": 0.2296, "depth": 10}
										if obj[4]>3:
											# {"feature": "Education", "instances": 14, "metric_value": 0.4571, "depth": 11}
											if obj[5]>0:
												# {"feature": "Direction_same", "instances": 9, "metric_value": 0.4444, "depth": 12}
												if obj[10]<=0:
													return 'True'
												elif obj[10]>0:
													return 'True'
												else: return 'True'
											elif obj[5]<=0:
												# {"feature": "Direction_same", "instances": 5, "metric_value": 0.4667, "depth": 12}
												if obj[10]<=0:
													return 'True'
												elif obj[10]>0:
													return 'False'
												else: return 'False'
											else: return 'True'
										elif obj[4]<=3:
											return 'True'
										else: return 'True'
									elif obj[11]>2:
										# {"feature": "Age", "instances": 13, "metric_value": 0.1346, "depth": 10}
										if obj[4]>1:
											# {"feature": "Education", "instances": 8, "metric_value": 0.2083, "depth": 11}
											if obj[5]<=0:
												# {"feature": "Direction_same", "instances": 6, "metric_value": 0.2778, "depth": 12}
												if obj[10]<=0:
													return 'True'
												else: return 'True'
											elif obj[5]>0:
												return 'True'
											else: return 'True'
										elif obj[4]<=1:
											return 'False'
										else: return 'False'
									else: return 'True'
								else: return 'True'
							elif obj[3]>0:
								# {"feature": "Education", "instances": 68, "metric_value": 0.4834, "depth": 8}
								if obj[5]>1:
									# {"feature": "Age", "instances": 37, "metric_value": 0.4142, "depth": 9}
									if obj[4]>1:
										# {"feature": "Coffeehouse", "instances": 28, "metric_value": 0.4076, "depth": 10}
										if obj[8]>0.0:
											# {"feature": "Distance", "instances": 25, "metric_value": 0.3726, "depth": 11}
											if obj[11]<=2:
												# {"feature": "Direction_same", "instances": 19, "metric_value": 0.3301, "depth": 12}
												if obj[10]<=0:
													return 'False'
												elif obj[10]>0:
													return 'False'
												else: return 'False'
											elif obj[11]>2:
												# {"feature": "Direction_same", "instances": 6, "metric_value": 0.5, "depth": 12}
												if obj[10]<=0:
													return 'False'
												else: return 'False'
											else: return 'False'
										elif obj[8]<=0.0:
											# {"feature": "Distance", "instances": 3, "metric_value": 0.0, "depth": 11}
											if obj[11]<=2:
												return 'True'
											elif obj[11]>2:
												return 'False'
											else: return 'False'
										else: return 'True'
									elif obj[4]<=1:
										# {"feature": "Coffeehouse", "instances": 9, "metric_value": 0.2667, "depth": 10}
										if obj[8]<=0.0:
											# {"feature": "Direction_same", "instances": 5, "metric_value": 0.4, "depth": 11}
											if obj[10]<=0:
												# {"feature": "Distance", "instances": 4, "metric_value": 0.3333, "depth": 12}
												if obj[11]<=2:
													return 'False'
												elif obj[11]>2:
													return 'True'
												else: return 'True'
											elif obj[10]>0:
												return 'True'
											else: return 'True'
										elif obj[8]>0.0:
											return 'True'
										else: return 'True'
									else: return 'True'
								elif obj[5]<=1:
									# {"feature": "Coffeehouse", "instances": 31, "metric_value": 0.3829, "depth": 9}
									if obj[8]>0.0:
										# {"feature": "Distance", "instances": 23, "metric_value": 0.3794, "depth": 10}
										if obj[11]<=2:
											# {"feature": "Age", "instances": 17, "metric_value": 0.4059, "depth": 11}
											if obj[4]>1:
												# {"feature": "Direction_same", "instances": 12, "metric_value": 0.3429, "depth": 12}
												if obj[10]<=0:
													return 'True'
												elif obj[10]>0:
													return 'True'
												else: return 'True'
											elif obj[4]<=1:
												# {"feature": "Direction_same", "instances": 5, "metric_value": 0.2667, "depth": 12}
												if obj[10]<=0:
													return 'False'
												elif obj[10]>0:
													return 'True'
												else: return 'True'
											else: return 'True'
										elif obj[11]>2:
											# {"feature": "Age", "instances": 6, "metric_value": 0.25, "depth": 11}
											if obj[4]>1:
												# {"feature": "Direction_same", "instances": 4, "metric_value": 0.375, "depth": 12}
												if obj[10]<=0:
													return 'True'
												else: return 'True'
											elif obj[4]<=1:
												return 'True'
											else: return 'True'
										else: return 'True'
									elif obj[8]<=0.0:
										# {"feature": "Age", "instances": 8, "metric_value": 0.3, "depth": 10}
										if obj[4]<=0:
											# {"feature": "Direction_same", "instances": 5, "metric_value": 0.3, "depth": 11}
											if obj[10]<=0:
												# {"feature": "Distance", "instances": 4, "metric_value": 0.3333, "depth": 12}
												if obj[11]<=2:
													return 'False'
												elif obj[11]>2:
													return 'False'
												else: return 'False'
											elif obj[10]>0:
												return 'True'
											else: return 'True'
										elif obj[4]>0:
											return 'False'
										else: return 'False'
									else: return 'False'
								else: return 'True'
							else: return 'True'
						elif obj[6]>13.60630442015693:
							# {"feature": "Age", "instances": 32, "metric_value": 0.4167, "depth": 7}
							if obj[4]<=2:
								# {"feature": "Distance", "instances": 20, "metric_value": 0.2637, "depth": 8}
								if obj[11]>1:
									# {"feature": "Education", "instances": 13, "metric_value": 0.1154, "depth": 9}
									if obj[5]<=2:
										return 'False'
									elif obj[5]>2:
										# {"feature": "Coffeehouse", "instances": 4, "metric_value": 0.3333, "depth": 10}
										if obj[8]>0.0:
											# {"feature": "Gender", "instances": 3, "metric_value": 0.4444, "depth": 11}
											if obj[3]<=0:
												# {"feature": "Direction_same", "instances": 3, "metric_value": 0.4444, "depth": 12}
												if obj[10]<=0:
													return 'False'
												else: return 'False'
											else: return 'False'
										elif obj[8]<=0.0:
											return 'False'
										else: return 'False'
									else: return 'False'
								elif obj[11]<=1:
									# {"feature": "Coffeehouse", "instances": 7, "metric_value": 0.3429, "depth": 9}
									if obj[8]>1.0:
										# {"feature": "Education", "instances": 5, "metric_value": 0.4, "depth": 10}
										if obj[5]>0:
											# {"feature": "Direction_same", "instances": 4, "metric_value": 0.3333, "depth": 11}
											if obj[10]<=0:
												# {"feature": "Gender", "instances": 3, "metric_value": 0.4444, "depth": 12}
												if obj[3]<=0:
													return 'True'
												else: return 'True'
											elif obj[10]>0:
												return 'False'
											else: return 'False'
										elif obj[5]<=0:
											return 'False'
										else: return 'False'
									elif obj[8]<=1.0:
										return 'True'
									else: return 'True'
								else: return 'True'
							elif obj[4]>2:
								# {"feature": "Distance", "instances": 12, "metric_value": 0.2381, "depth": 8}
								if obj[11]<=2:
									# {"feature": "Coffeehouse", "instances": 7, "metric_value": 0.2857, "depth": 9}
									if obj[8]>1.0:
										# {"feature": "Direction_same", "instances": 4, "metric_value": 0.0, "depth": 10}
										if obj[10]>0:
											return 'True'
										elif obj[10]<=0:
											return 'False'
										else: return 'False'
									elif obj[8]<=1.0:
										return 'False'
									else: return 'False'
								elif obj[11]>2:
									return 'True'
								else: return 'True'
							else: return 'True'
						else: return 'False'
					elif obj[1]>2:
						# {"feature": "Gender", "instances": 88, "metric_value": 0.4489, "depth": 6}
						if obj[3]<=0:
							# {"feature": "Age", "instances": 59, "metric_value": 0.4039, "depth": 7}
							if obj[4]>0:
								# {"feature": "Direction_same", "instances": 44, "metric_value": 0.4242, "depth": 8}
								if obj[10]<=0:
									# {"feature": "Occupation", "instances": 42, "metric_value": 0.4228, "depth": 9}
									if obj[6]<=21:
										# {"feature": "Coffeehouse", "instances": 41, "metric_value": 0.4138, "depth": 10}
										if obj[8]<=3.0:
											# {"feature": "Distance", "instances": 38, "metric_value": 0.3907, "depth": 11}
											if obj[11]<=1:
												# {"feature": "Education", "instances": 21, "metric_value": 0.4571, "depth": 12}
												if obj[5]<=2:
													return 'False'
												elif obj[5]>2:
													return 'False'
												else: return 'False'
											elif obj[11]>1:
												# {"feature": "Education", "instances": 17, "metric_value": 0.2773, "depth": 12}
												if obj[5]<=2:
													return 'False'
												elif obj[5]>2:
													return 'False'
												else: return 'False'
											else: return 'False'
										elif obj[8]>3.0:
											# {"feature": "Education", "instances": 3, "metric_value": 0.3333, "depth": 11}
											if obj[5]<=0:
												# {"feature": "Distance", "instances": 2, "metric_value": 0.0, "depth": 12}
												if obj[11]<=1:
													return 'False'
												elif obj[11]>1:
													return 'True'
												else: return 'True'
											elif obj[5]>0:
												return 'True'
											else: return 'True'
										else: return 'True'
									elif obj[6]>21:
										return 'True'
									else: return 'True'
								elif obj[10]>0:
									return 'True'
								else: return 'True'
							elif obj[4]<=0:
								# {"feature": "Coffeehouse", "instances": 15, "metric_value": 0.2111, "depth": 8}
								if obj[8]<=3.0:
									# {"feature": "Direction_same", "instances": 12, "metric_value": 0.0833, "depth": 9}
									if obj[10]<=0:
										return 'False'
									elif obj[10]>0:
										# {"feature": "Education", "instances": 2, "metric_value": 0.0, "depth": 10}
										if obj[5]>2:
											return 'False'
										elif obj[5]<=2:
											return 'True'
										else: return 'True'
									else: return 'False'
								elif obj[8]>3.0:
									# {"feature": "Direction_same", "instances": 3, "metric_value": 0.3333, "depth": 9}
									if obj[10]<=0:
										# {"feature": "Distance", "instances": 2, "metric_value": 0.0, "depth": 10}
										if obj[11]>1:
											return 'True'
										elif obj[11]<=1:
											return 'False'
										else: return 'False'
									elif obj[10]>0:
										return 'False'
									else: return 'False'
								else: return 'False'
							else: return 'False'
						elif obj[3]>0:
							# {"feature": "Age", "instances": 29, "metric_value": 0.4263, "depth": 7}
							if obj[4]>1:
								# {"feature": "Occupation", "instances": 18, "metric_value": 0.4167, "depth": 8}
								if obj[6]<=5:
									# {"feature": "Coffeehouse", "instances": 12, "metric_value": 0.35, "depth": 9}
									if obj[8]<=3.0:
										# {"feature": "Distance", "instances": 10, "metric_value": 0.24, "depth": 10}
										if obj[11]<=1:
											return 'False'
										elif obj[11]>1:
											# {"feature": "Education", "instances": 5, "metric_value": 0.2667, "depth": 11}
											if obj[5]>1:
												# {"feature": "Direction_same", "instances": 3, "metric_value": 0.4444, "depth": 12}
												if obj[10]<=0:
													return 'True'
												else: return 'True'
											elif obj[5]<=1:
												return 'False'
											else: return 'False'
										else: return 'False'
									elif obj[8]>3.0:
										# {"feature": "Distance", "instances": 2, "metric_value": 0.0, "depth": 10}
										if obj[11]<=1:
											return 'True'
										elif obj[11]>1:
											return 'False'
										else: return 'False'
									else: return 'True'
								elif obj[6]>5:
									# {"feature": "Coffeehouse", "instances": 6, "metric_value": 0.4, "depth": 9}
									if obj[8]<=2.0:
										# {"feature": "Education", "instances": 5, "metric_value": 0.4, "depth": 10}
										if obj[5]<=0:
											# {"feature": "Direction_same", "instances": 4, "metric_value": 0.5, "depth": 11}
											if obj[10]<=0:
												# {"feature": "Distance", "instances": 4, "metric_value": 0.5, "depth": 12}
												if obj[11]>1:
													return 'True'
												elif obj[11]<=1:
													return 'False'
												else: return 'False'
											else: return 'True'
										elif obj[5]>0:
											return 'True'
										else: return 'True'
									elif obj[8]>2.0:
										return 'False'
									else: return 'False'
								else: return 'True'
							elif obj[4]<=1:
								# {"feature": "Education", "instances": 11, "metric_value": 0.2909, "depth": 8}
								if obj[5]<=4:
									# {"feature": "Coffeehouse", "instances": 10, "metric_value": 0.1778, "depth": 9}
									if obj[8]>-1.0:
										# {"feature": "Direction_same", "instances": 9, "metric_value": 0.1111, "depth": 10}
										if obj[10]<=0:
											return 'True'
										elif obj[10]>0:
											# {"feature": "Occupation", "instances": 2, "metric_value": 0.0, "depth": 11}
											if obj[6]<=4:
												return 'False'
											elif obj[6]>4:
												return 'True'
											else: return 'True'
										else: return 'False'
									elif obj[8]<=-1.0:
										return 'False'
									else: return 'False'
								elif obj[5]>4:
									return 'False'
								else: return 'False'
							else: return 'True'
						else: return 'False'
					else: return 'False'
				elif obj[0]>2:
					# {"feature": "Time", "instances": 65, "metric_value": 0.4117, "depth": 5}
					if obj[1]>2:
						# {"feature": "Age", "instances": 47, "metric_value": 0.3245, "depth": 6}
						if obj[4]>1:
							# {"feature": "Coffeehouse", "instances": 28, "metric_value": 0.4196, "depth": 7}
							if obj[8]<=2.0:
								# {"feature": "Occupation", "instances": 20, "metric_value": 0.4444, "depth": 8}
								if obj[6]>2:
									# {"feature": "Education", "instances": 18, "metric_value": 0.4333, "depth": 9}
									if obj[5]<=0:
										# {"feature": "Distance", "instances": 10, "metric_value": 0.475, "depth": 10}
										if obj[11]>1:
											# {"feature": "Gender", "instances": 8, "metric_value": 0.4667, "depth": 11}
											if obj[3]<=0:
												# {"feature": "Direction_same", "instances": 5, "metric_value": 0.48, "depth": 12}
												if obj[10]<=0:
													return 'True'
												else: return 'True'
											elif obj[3]>0:
												# {"feature": "Direction_same", "instances": 3, "metric_value": 0.4444, "depth": 12}
												if obj[10]<=0:
													return 'True'
												else: return 'True'
											else: return 'True'
										elif obj[11]<=1:
											# {"feature": "Gender", "instances": 2, "metric_value": 0.5, "depth": 11}
											if obj[3]<=0:
												# {"feature": "Direction_same", "instances": 2, "metric_value": 0.5, "depth": 12}
												if obj[10]<=0:
													return 'True'
												else: return 'True'
											else: return 'True'
										else: return 'True'
									elif obj[5]>0:
										# {"feature": "Gender", "instances": 8, "metric_value": 0.3333, "depth": 10}
										if obj[3]<=0:
											# {"feature": "Distance", "instances": 6, "metric_value": 0.4167, "depth": 11}
											if obj[11]>1:
												# {"feature": "Direction_same", "instances": 4, "metric_value": 0.375, "depth": 12}
												if obj[10]<=0:
													return 'False'
												else: return 'False'
											elif obj[11]<=1:
												# {"feature": "Direction_same", "instances": 2, "metric_value": 0.5, "depth": 12}
												if obj[10]<=0:
													return 'True'
												else: return 'True'
											else: return 'True'
										elif obj[3]>0:
											return 'False'
										else: return 'False'
									else: return 'False'
								elif obj[6]<=2:
									return 'True'
								else: return 'True'
							elif obj[8]>2.0:
								# {"feature": "Gender", "instances": 8, "metric_value": 0.125, "depth": 8}
								if obj[3]<=0:
									return 'True'
								elif obj[3]>0:
									# {"feature": "Education", "instances": 2, "metric_value": 0.0, "depth": 9}
									if obj[5]>0:
										return 'False'
									elif obj[5]<=0:
										return 'True'
									else: return 'True'
								else: return 'False'
							else: return 'True'
						elif obj[4]<=1:
							# {"feature": "Occupation", "instances": 19, "metric_value": 0.0877, "depth": 7}
							if obj[6]>1:
								return 'True'
							elif obj[6]<=1:
								# {"feature": "Coffeehouse", "instances": 6, "metric_value": 0.1667, "depth": 8}
								if obj[8]>0.0:
									return 'True'
								elif obj[8]<=0.0:
									# {"feature": "Education", "instances": 2, "metric_value": 0.0, "depth": 9}
									if obj[5]>0:
										return 'False'
									elif obj[5]<=0:
										return 'True'
									else: return 'True'
								else: return 'False'
							else: return 'True'
						else: return 'True'
					elif obj[1]<=2:
						# {"feature": "Occupation", "instances": 18, "metric_value": 0.2564, "depth": 6}
						if obj[6]<=10:
							# {"feature": "Age", "instances": 13, "metric_value": 0.3077, "depth": 7}
							if obj[4]<=2:
								# {"feature": "Coffeehouse", "instances": 9, "metric_value": 0.3333, "depth": 8}
								if obj[8]>0.0:
									# {"feature": "Education", "instances": 6, "metric_value": 0.25, "depth": 9}
									if obj[5]<=2:
										# {"feature": "Gender", "instances": 4, "metric_value": 0.3333, "depth": 10}
										if obj[3]<=0:
											# {"feature": "Direction_same", "instances": 3, "metric_value": 0.4444, "depth": 11}
											if obj[10]<=0:
												# {"feature": "Distance", "instances": 3, "metric_value": 0.4444, "depth": 12}
												if obj[11]<=2:
													return 'True'
												else: return 'True'
											else: return 'True'
										elif obj[3]>0:
											return 'True'
										else: return 'True'
									elif obj[5]>2:
										return 'False'
									else: return 'False'
								elif obj[8]<=0.0:
									return 'False'
								else: return 'False'
							elif obj[4]>2:
								return 'False'
							else: return 'False'
						elif obj[6]>10:
							return 'True'
						else: return 'True'
					else: return 'False'
				else: return 'True'
			elif obj[9]>1.0:
				# {"feature": "Direction_same", "instances": 307, "metric_value": 0.4012, "depth": 4}
				if obj[10]<=0:
					# {"feature": "Education", "instances": 250, "metric_value": 0.4308, "depth": 5}
					if obj[5]>1:
						# {"feature": "Occupation", "instances": 161, "metric_value": 0.4573, "depth": 6}
						if obj[6]>1:
							# {"feature": "Time", "instances": 133, "metric_value": 0.4834, "depth": 7}
							if obj[1]>0:
								# {"feature": "Gender", "instances": 112, "metric_value": 0.4851, "depth": 8}
								if obj[3]<=0:
									# {"feature": "Age", "instances": 59, "metric_value": 0.4084, "depth": 9}
									if obj[4]<=3:
										# {"feature": "Passanger", "instances": 41, "metric_value": 0.3744, "depth": 10}
										if obj[0]<=2:
											# {"feature": "Distance", "instances": 29, "metric_value": 0.3067, "depth": 11}
											if obj[11]<=2:
												# {"feature": "Coffeehouse", "instances": 21, "metric_value": 0.218, "depth": 12}
												if obj[8]>0.0:
													return 'True'
												elif obj[8]<=0.0:
													return 'True'
												else: return 'True'
											elif obj[11]>2:
												# {"feature": "Coffeehouse", "instances": 8, "metric_value": 0.4583, "depth": 12}
												if obj[8]<=3.0:
													return 'True'
												elif obj[8]>3.0:
													return 'False'
												else: return 'False'
											else: return 'True'
										elif obj[0]>2:
											# {"feature": "Coffeehouse", "instances": 12, "metric_value": 0.2593, "depth": 11}
											if obj[8]<=3.0:
												# {"feature": "Distance", "instances": 9, "metric_value": 0.3457, "depth": 12}
												if obj[11]<=2:
													return 'True'
												else: return 'True'
											elif obj[8]>3.0:
												return 'False'
											else: return 'False'
										else: return 'True'
									elif obj[4]>3:
										# {"feature": "Passanger", "instances": 18, "metric_value": 0.3723, "depth": 10}
										if obj[0]<=1:
											# {"feature": "Distance", "instances": 11, "metric_value": 0.2803, "depth": 11}
											if obj[11]<=2:
												# {"feature": "Coffeehouse", "instances": 8, "metric_value": 0.2, "depth": 12}
												if obj[8]>0.0:
													return 'False'
												elif obj[8]<=0.0:
													return 'False'
												else: return 'False'
											elif obj[11]>2:
												# {"feature": "Coffeehouse", "instances": 3, "metric_value": 0.4444, "depth": 12}
												if obj[8]<=0.0:
													return 'False'
												else: return 'False'
											else: return 'False'
										elif obj[0]>1:
											# {"feature": "Coffeehouse", "instances": 7, "metric_value": 0.4048, "depth": 11}
											if obj[8]<=0.0:
												# {"feature": "Distance", "instances": 4, "metric_value": 0.375, "depth": 12}
												if obj[11]<=2:
													return 'True'
												else: return 'True'
											elif obj[8]>0.0:
												# {"feature": "Distance", "instances": 3, "metric_value": 0.0, "depth": 12}
												if obj[11]>1:
													return 'False'
												elif obj[11]<=1:
													return 'True'
												else: return 'True'
											else: return 'False'
										else: return 'True'
									else: return 'False'
								elif obj[3]>0:
									# {"feature": "Age", "instances": 53, "metric_value": 0.4586, "depth": 9}
									if obj[4]<=5:
										# {"feature": "Coffeehouse", "instances": 47, "metric_value": 0.4501, "depth": 10}
										if obj[8]>0.0:
											# {"feature": "Distance", "instances": 45, "metric_value": 0.4644, "depth": 11}
											if obj[11]<=2:
												# {"feature": "Passanger", "instances": 32, "metric_value": 0.4442, "depth": 12}
												if obj[0]<=2:
													return 'False'
												elif obj[0]>2:
													return 'False'
												else: return 'False'
											elif obj[11]>2:
												# {"feature": "Passanger", "instances": 13, "metric_value": 0.4615, "depth": 12}
												if obj[0]>0:
													return 'True'
												elif obj[0]<=0:
													return 'False'
												else: return 'False'
											else: return 'False'
										elif obj[8]<=0.0:
											return 'True'
										else: return 'True'
									elif obj[4]>5:
										# {"feature": "Distance", "instances": 6, "metric_value": 0.2222, "depth": 10}
										if obj[11]>1:
											return 'True'
										elif obj[11]<=1:
											# {"feature": "Passanger", "instances": 3, "metric_value": 0.3333, "depth": 11}
											if obj[0]>0:
												# {"feature": "Coffeehouse", "instances": 2, "metric_value": 0.0, "depth": 12}
												if obj[8]<=3.0:
													return 'True'
												elif obj[8]>3.0:
													return 'False'
												else: return 'False'
											elif obj[0]<=0:
												return 'True'
											else: return 'True'
										else: return 'True'
									else: return 'True'
								else: return 'False'
							elif obj[1]<=0:
								# {"feature": "Coffeehouse", "instances": 21, "metric_value": 0.3844, "depth": 8}
								if obj[8]<=2.0:
									# {"feature": "Age", "instances": 11, "metric_value": 0.2424, "depth": 9}
									if obj[4]>1:
										# {"feature": "Passanger", "instances": 6, "metric_value": 0.4167, "depth": 10}
										if obj[0]>0:
											# {"feature": "Gender", "instances": 4, "metric_value": 0.375, "depth": 11}
											if obj[3]<=0:
												# {"feature": "Distance", "instances": 4, "metric_value": 0.375, "depth": 12}
												if obj[11]<=2:
													return 'True'
												else: return 'True'
											else: return 'True'
										elif obj[0]<=0:
											# {"feature": "Gender", "instances": 2, "metric_value": 0.5, "depth": 11}
											if obj[3]<=0:
												# {"feature": "Distance", "instances": 2, "metric_value": 0.5, "depth": 12}
												if obj[11]<=2:
													return 'False'
												else: return 'False'
											else: return 'False'
										else: return 'False'
									elif obj[4]<=1:
										return 'True'
									else: return 'True'
								elif obj[8]>2.0:
									# {"feature": "Age", "instances": 10, "metric_value": 0.3, "depth": 9}
									if obj[4]>2:
										# {"feature": "Passanger", "instances": 8, "metric_value": 0.3333, "depth": 10}
										if obj[0]>0:
											# {"feature": "Gender", "instances": 6, "metric_value": 0.2222, "depth": 11}
											if obj[3]>0:
												return 'True'
											elif obj[3]<=0:
												# {"feature": "Distance", "instances": 3, "metric_value": 0.3333, "depth": 12}
												if obj[11]>1:
													return 'False'
												elif obj[11]<=1:
													return 'True'
												else: return 'True'
											else: return 'True'
										elif obj[0]<=0:
											# {"feature": "Gender", "instances": 2, "metric_value": 0.0, "depth": 11}
											if obj[3]>0:
												return 'False'
											elif obj[3]<=0:
												return 'True'
											else: return 'True'
										else: return 'False'
									elif obj[4]<=2:
										return 'False'
									else: return 'False'
								else: return 'True'
							else: return 'True'
						elif obj[6]<=1:
							# {"feature": "Passanger", "instances": 28, "metric_value": 0.2434, "depth": 7}
							if obj[0]>0:
								# {"feature": "Distance", "instances": 27, "metric_value": 0.2339, "depth": 8}
								if obj[11]<=2:
									# {"feature": "Time", "instances": 19, "metric_value": 0.2551, "depth": 9}
									if obj[1]>1:
										# {"feature": "Gender", "instances": 13, "metric_value": 0.1154, "depth": 10}
										if obj[3]>0:
											return 'True'
										elif obj[3]<=0:
											# {"feature": "Age", "instances": 4, "metric_value": 0.375, "depth": 11}
											if obj[4]<=1:
												# {"feature": "Coffeehouse", "instances": 4, "metric_value": 0.375, "depth": 12}
												if obj[8]<=4.0:
													return 'True'
												else: return 'True'
											else: return 'True'
										else: return 'True'
									elif obj[1]<=1:
										# {"feature": "Gender", "instances": 6, "metric_value": 0.25, "depth": 10}
										if obj[3]>0:
											# {"feature": "Age", "instances": 4, "metric_value": 0.375, "depth": 11}
											if obj[4]<=1:
												# {"feature": "Coffeehouse", "instances": 4, "metric_value": 0.375, "depth": 12}
												if obj[8]<=2.0:
													return 'False'
												else: return 'False'
											else: return 'False'
										elif obj[3]<=0:
											return 'True'
										else: return 'True'
									else: return 'True'
								elif obj[11]>2:
									return 'True'
								else: return 'True'
							elif obj[0]<=0:
								return 'False'
							else: return 'False'
						else: return 'True'
					elif obj[5]<=1:
						# {"feature": "Occupation", "instances": 89, "metric_value": 0.3213, "depth": 6}
						if obj[6]<=10:
							# {"feature": "Age", "instances": 53, "metric_value": 0.3821, "depth": 7}
							if obj[4]>1:
								# {"feature": "Passanger", "instances": 27, "metric_value": 0.4807, "depth": 8}
								if obj[0]<=2:
									# {"feature": "Coffeehouse", "instances": 23, "metric_value": 0.4842, "depth": 9}
									if obj[8]>1.0:
										# {"feature": "Distance", "instances": 17, "metric_value": 0.4683, "depth": 10}
										if obj[11]<=2:
											# {"feature": "Gender", "instances": 13, "metric_value": 0.4689, "depth": 11}
											if obj[3]<=0:
												# {"feature": "Time", "instances": 7, "metric_value": 0.4048, "depth": 12}
												if obj[1]>1:
													return 'True'
												elif obj[1]<=1:
													return 'False'
												else: return 'False'
											elif obj[3]>0:
												# {"feature": "Time", "instances": 6, "metric_value": 0.2222, "depth": 12}
												if obj[1]>0:
													return 'False'
												elif obj[1]<=0:
													return 'True'
												else: return 'True'
											else: return 'False'
										elif obj[11]>2:
											# {"feature": "Gender", "instances": 4, "metric_value": 0.3333, "depth": 11}
											if obj[3]>0:
												# {"feature": "Time", "instances": 3, "metric_value": 0.4444, "depth": 12}
												if obj[1]<=1:
													return 'True'
												else: return 'True'
											elif obj[3]<=0:
												return 'True'
											else: return 'True'
										else: return 'True'
									elif obj[8]<=1.0:
										# {"feature": "Distance", "instances": 6, "metric_value": 0.3333, "depth": 10}
										if obj[11]<=2:
											# {"feature": "Time", "instances": 4, "metric_value": 0.3333, "depth": 11}
											if obj[1]<=1:
												# {"feature": "Gender", "instances": 3, "metric_value": 0.4444, "depth": 12}
												if obj[3]<=0:
													return 'True'
												else: return 'True'
											elif obj[1]>1:
												return 'False'
											else: return 'False'
										elif obj[11]>2:
											return 'False'
										else: return 'False'
									else: return 'False'
								elif obj[0]>2:
									# {"feature": "Time", "instances": 4, "metric_value": 0.0, "depth": 9}
									if obj[1]>2:
										return 'True'
									elif obj[1]<=2:
										return 'False'
									else: return 'False'
								else: return 'True'
							elif obj[4]<=1:
								# {"feature": "Passanger", "instances": 26, "metric_value": 0.2168, "depth": 8}
								if obj[0]<=1:
									# {"feature": "Coffeehouse", "instances": 22, "metric_value": 0.1455, "depth": 9}
									if obj[8]<=1.0:
										return 'True'
									elif obj[8]>1.0:
										# {"feature": "Gender", "instances": 10, "metric_value": 0.2857, "depth": 10}
										if obj[3]<=0:
											# {"feature": "Distance", "instances": 7, "metric_value": 0.2381, "depth": 11}
											if obj[11]<=2:
												# {"feature": "Time", "instances": 6, "metric_value": 0.25, "depth": 12}
												if obj[1]>1:
													return 'True'
												elif obj[1]<=1:
													return 'True'
												else: return 'True'
											elif obj[11]>2:
												return 'False'
											else: return 'False'
										elif obj[3]>0:
											return 'True'
										else: return 'True'
									else: return 'True'
								elif obj[0]>1:
									# {"feature": "Time", "instances": 4, "metric_value": 0.3333, "depth": 9}
									if obj[1]>0:
										# {"feature": "Gender", "instances": 3, "metric_value": 0.0, "depth": 10}
										if obj[3]>0:
											return 'False'
										elif obj[3]<=0:
											return 'True'
										else: return 'True'
									elif obj[1]<=0:
										return 'True'
									else: return 'True'
								else: return 'True'
							else: return 'True'
						elif obj[6]>10:
							# {"feature": "Age", "instances": 36, "metric_value": 0.1212, "depth": 7}
							if obj[4]>0:
								return 'True'
							elif obj[4]<=0:
								# {"feature": "Coffeehouse", "instances": 11, "metric_value": 0.2727, "depth": 8}
								if obj[8]<=1.0:
									# {"feature": "Passanger", "instances": 6, "metric_value": 0.25, "depth": 9}
									if obj[0]<=2:
										# {"feature": "Distance", "instances": 4, "metric_value": 0.0, "depth": 10}
										if obj[11]<=2:
											return 'False'
										elif obj[11]>2:
											return 'True'
										else: return 'True'
									elif obj[0]>2:
										return 'True'
									else: return 'True'
								elif obj[8]>1.0:
									return 'True'
								else: return 'True'
							else: return 'True'
						else: return 'True'
					else: return 'True'
				elif obj[10]>0:
					# {"feature": "Time", "instances": 57, "metric_value": 0.2047, "depth": 5}
					if obj[1]<=0:
						# {"feature": "Age", "instances": 40, "metric_value": 0.1086, "depth": 6}
						if obj[4]<=5:
							# {"feature": "Occupation", "instances": 35, "metric_value": 0.0286, "depth": 7}
							if obj[6]<=21:
								return 'True'
							elif obj[6]>21:
								# {"feature": "Gender", "instances": 2, "metric_value": 0.0, "depth": 8}
								if obj[3]>0:
									return 'False'
								elif obj[3]<=0:
									return 'True'
								else: return 'True'
							else: return 'False'
						elif obj[4]>5:
							# {"feature": "Occupation", "instances": 5, "metric_value": 0.2667, "depth": 7}
							if obj[6]<=12:
								# {"feature": "Education", "instances": 3, "metric_value": 0.0, "depth": 8}
								if obj[5]<=1:
									return 'False'
								elif obj[5]>1:
									return 'True'
								else: return 'True'
							elif obj[6]>12:
								return 'True'
							else: return 'True'
						else: return 'True'
					elif obj[1]>0:
						# {"feature": "Distance", "instances": 17, "metric_value": 0.2834, "depth": 6}
						if obj[11]>1:
							# {"feature": "Age", "instances": 11, "metric_value": 0.1364, "depth": 7}
							if obj[4]<=3:
								return 'True'
							elif obj[4]>3:
								# {"feature": "Education", "instances": 4, "metric_value": 0.0, "depth": 8}
								if obj[5]<=0:
									return 'True'
								elif obj[5]>0:
									return 'False'
								else: return 'False'
							else: return 'True'
						elif obj[11]<=1:
							# {"feature": "Education", "instances": 6, "metric_value": 0.25, "depth": 7}
							if obj[5]<=2:
								# {"feature": "Occupation", "instances": 4, "metric_value": 0.25, "depth": 8}
								if obj[6]>5:
									return 'True'
								elif obj[6]<=5:
									# {"feature": "Passanger", "instances": 2, "metric_value": 0.5, "depth": 9}
									if obj[0]<=1:
										# {"feature": "Gender", "instances": 2, "metric_value": 0.5, "depth": 10}
										if obj[3]<=0:
											# {"feature": "Age", "instances": 2, "metric_value": 0.5, "depth": 11}
											if obj[4]<=0:
												# {"feature": "Coffeehouse", "instances": 2, "metric_value": 0.5, "depth": 12}
												if obj[8]<=2.0:
													return 'False'
												else: return 'False'
											else: return 'False'
										else: return 'False'
									else: return 'False'
								else: return 'False'
							elif obj[5]>2:
								return 'False'
							else: return 'False'
						else: return 'True'
					else: return 'True'
				else: return 'True'
			else: return 'True'
		else: return 'True'
	else: return 'False'
