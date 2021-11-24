def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Education, obj[4]: Occupation, obj[5]: Bar, obj[6]: Coffeehouse, obj[7]: Restaurant20to50, obj[8]: Direction_same, obj[9]: Distance
	# {"feature": "Coupon", "instances": 8147, "metric_value": 0.4722, "depth": 1}
	if obj[2]>1:
		# {"feature": "Coffeehouse", "instances": 5903, "metric_value": 0.4569, "depth": 2}
		if obj[6]<=1.0:
			# {"feature": "Passanger", "instances": 3018, "metric_value": 0.4857, "depth": 3}
			if obj[0]<=1:
				# {"feature": "Distance", "instances": 1928, "metric_value": 0.4872, "depth": 4}
				if obj[9]<=1:
					# {"feature": "Time", "instances": 1066, "metric_value": 0.4791, "depth": 5}
					if obj[1]>0:
						# {"feature": "Direction_same", "instances": 704, "metric_value": 0.457, "depth": 6}
						if obj[8]>0:
							# {"feature": "Occupation", "instances": 360, "metric_value": 0.4901, "depth": 7}
							if obj[4]<=20.37285734786367:
								# {"feature": "Bar", "instances": 337, "metric_value": 0.4933, "depth": 8}
								if obj[5]<=1.0:
									# {"feature": "Education", "instances": 270, "metric_value": 0.4904, "depth": 9}
									if obj[3]<=3:
										# {"feature": "Restaurant20to50", "instances": 238, "metric_value": 0.493, "depth": 10}
										if obj[7]<=2.0:
											return 'True'
										elif obj[7]>2.0:
											return 'True'
										else: return 'True'
									elif obj[3]>3:
										# {"feature": "Restaurant20to50", "instances": 32, "metric_value": 0.4234, "depth": 10}
										if obj[7]>-1.0:
											return 'True'
										elif obj[7]<=-1.0:
											return 'False'
										else: return 'False'
									else: return 'True'
								elif obj[5]>1.0:
									# {"feature": "Restaurant20to50", "instances": 67, "metric_value": 0.4662, "depth": 9}
									if obj[7]<=1.0:
										# {"feature": "Education", "instances": 40, "metric_value": 0.4504, "depth": 10}
										if obj[3]>0:
											return 'False'
										elif obj[3]<=0:
											return 'False'
										else: return 'False'
									elif obj[7]>1.0:
										# {"feature": "Education", "instances": 27, "metric_value": 0.4267, "depth": 10}
										if obj[3]<=3:
											return 'True'
										elif obj[3]>3:
											return 'False'
										else: return 'False'
									else: return 'True'
								else: return 'False'
							elif obj[4]>20.37285734786367:
								# {"feature": "Restaurant20to50", "instances": 23, "metric_value": 0.3478, "depth": 8}
								if obj[7]<=1.0:
									# {"feature": "Education", "instances": 18, "metric_value": 0.4167, "depth": 9}
									if obj[3]<=2:
										# {"feature": "Bar", "instances": 12, "metric_value": 0.4444, "depth": 10}
										if obj[5]<=0.0:
											return 'True'
										elif obj[5]>0.0:
											return 'False'
										else: return 'False'
									elif obj[3]>2:
										# {"feature": "Bar", "instances": 6, "metric_value": 0.2222, "depth": 10}
										if obj[5]<=1.0:
											return 'True'
										elif obj[5]>1.0:
											return 'True'
										else: return 'True'
									else: return 'True'
								elif obj[7]>1.0:
									return 'True'
								else: return 'True'
							else: return 'True'
						elif obj[8]<=0:
							# {"feature": "Bar", "instances": 344, "metric_value": 0.4136, "depth": 7}
							if obj[5]<=2.0:
								# {"feature": "Occupation", "instances": 314, "metric_value": 0.4005, "depth": 8}
								if obj[4]<=16.766183412132953:
									# {"feature": "Restaurant20to50", "instances": 296, "metric_value": 0.393, "depth": 9}
									if obj[7]>0.0:
										# {"feature": "Education", "instances": 228, "metric_value": 0.4055, "depth": 10}
										if obj[3]>0:
											return 'True'
										elif obj[3]<=0:
											return 'True'
										else: return 'True'
									elif obj[7]<=0.0:
										# {"feature": "Education", "instances": 68, "metric_value": 0.3409, "depth": 10}
										if obj[3]>0:
											return 'True'
										elif obj[3]<=0:
											return 'True'
										else: return 'True'
									else: return 'True'
								elif obj[4]>16.766183412132953:
									# {"feature": "Restaurant20to50", "instances": 18, "metric_value": 0.3571, "depth": 9}
									if obj[7]>0.0:
										# {"feature": "Education", "instances": 14, "metric_value": 0.4571, "depth": 10}
										if obj[3]<=0:
											return 'True'
										elif obj[3]>0:
											return 'True'
										else: return 'True'
									elif obj[7]<=0.0:
										return 'False'
									else: return 'False'
								else: return 'True'
							elif obj[5]>2.0:
								# {"feature": "Education", "instances": 30, "metric_value": 0.3911, "depth": 8}
								if obj[3]>0:
									# {"feature": "Occupation", "instances": 19, "metric_value": 0.3618, "depth": 9}
									if obj[4]<=12:
										# {"feature": "Restaurant20to50", "instances": 16, "metric_value": 0.4018, "depth": 10}
										if obj[7]>0.0:
											return 'True'
										elif obj[7]<=0.0:
											return 'True'
										else: return 'True'
									elif obj[4]>12:
										return 'True'
									else: return 'True'
								elif obj[3]<=0:
									# {"feature": "Occupation", "instances": 11, "metric_value": 0.2727, "depth": 9}
									if obj[4]>10:
										# {"feature": "Restaurant20to50", "instances": 6, "metric_value": 0.4444, "depth": 10}
										if obj[7]<=1.0:
											return 'False'
										elif obj[7]>1.0:
											return 'True'
										else: return 'True'
									elif obj[4]<=10:
										return 'False'
									else: return 'False'
								else: return 'False'
							else: return 'True'
						else: return 'True'
					elif obj[1]<=0:
						# {"feature": "Restaurant20to50", "instances": 362, "metric_value": 0.4901, "depth": 6}
						if obj[7]<=2.0:
							# {"feature": "Education", "instances": 355, "metric_value": 0.4936, "depth": 7}
							if obj[3]<=3:
								# {"feature": "Direction_same", "instances": 328, "metric_value": 0.4963, "depth": 8}
								if obj[8]<=0:
									# {"feature": "Bar", "instances": 196, "metric_value": 0.4876, "depth": 9}
									if obj[5]>-1.0:
										# {"feature": "Occupation", "instances": 193, "metric_value": 0.4888, "depth": 10}
										if obj[4]>0:
											return 'False'
										elif obj[4]<=0:
											return 'True'
										else: return 'True'
									elif obj[5]<=-1.0:
										return 'True'
									else: return 'True'
								elif obj[8]>0:
									# {"feature": "Occupation", "instances": 132, "metric_value": 0.4905, "depth": 9}
									if obj[4]<=20.383206281203112:
										# {"feature": "Bar", "instances": 124, "metric_value": 0.4933, "depth": 10}
										if obj[5]>-1.0:
											return 'True'
										elif obj[5]<=-1.0:
											return 'False'
										else: return 'False'
									elif obj[4]>20.383206281203112:
										# {"feature": "Bar", "instances": 8, "metric_value": 0.3333, "depth": 10}
										if obj[5]>0.0:
											return 'True'
										elif obj[5]<=0.0:
											return 'True'
										else: return 'True'
									else: return 'True'
								else: return 'True'
							elif obj[3]>3:
								# {"feature": "Occupation", "instances": 27, "metric_value": 0.3789, "depth": 8}
								if obj[4]<=21:
									# {"feature": "Bar", "instances": 26, "metric_value": 0.375, "depth": 9}
									if obj[5]>0.0:
										# {"feature": "Direction_same", "instances": 18, "metric_value": 0.4417, "depth": 10}
										if obj[8]<=0:
											return 'True'
										elif obj[8]>0:
											return 'True'
										else: return 'True'
									elif obj[5]<=0.0:
										# {"feature": "Direction_same", "instances": 8, "metric_value": 0.1875, "depth": 10}
										if obj[8]<=0:
											return 'True'
										elif obj[8]>0:
											return 'True'
										else: return 'True'
									else: return 'True'
								elif obj[4]>21:
									return 'False'
								else: return 'False'
							else: return 'True'
						elif obj[7]>2.0:
							return 'True'
						else: return 'True'
					else: return 'True'
				elif obj[9]>1:
					# {"feature": "Time", "instances": 862, "metric_value": 0.4813, "depth": 5}
					if obj[1]<=3:
						# {"feature": "Direction_same", "instances": 705, "metric_value": 0.4721, "depth": 6}
						if obj[8]<=0:
							# {"feature": "Education", "instances": 528, "metric_value": 0.4597, "depth": 7}
							if obj[3]<=3:
								# {"feature": "Bar", "instances": 481, "metric_value": 0.4536, "depth": 8}
								if obj[5]<=2.0:
									# {"feature": "Restaurant20to50", "instances": 450, "metric_value": 0.459, "depth": 9}
									if obj[7]<=3.0:
										# {"feature": "Occupation", "instances": 449, "metric_value": 0.4585, "depth": 10}
										if obj[4]<=19.487365400575516:
											return 'False'
										elif obj[4]>19.487365400575516:
											return 'False'
										else: return 'False'
									elif obj[7]>3.0:
										return 'True'
									else: return 'True'
								elif obj[5]>2.0:
									# {"feature": "Occupation", "instances": 31, "metric_value": 0.3387, "depth": 9}
									if obj[4]<=17:
										# {"feature": "Restaurant20to50", "instances": 28, "metric_value": 0.3712, "depth": 10}
										if obj[7]>0.0:
											return 'False'
										elif obj[7]<=0.0:
											return 'False'
										else: return 'False'
									elif obj[4]>17:
										return 'False'
									else: return 'False'
								else: return 'False'
							elif obj[3]>3:
								# {"feature": "Restaurant20to50", "instances": 47, "metric_value": 0.4785, "depth": 8}
								if obj[7]>-1.0:
									# {"feature": "Bar", "instances": 45, "metric_value": 0.484, "depth": 9}
									if obj[5]<=1.0:
										# {"feature": "Occupation", "instances": 36, "metric_value": 0.4825, "depth": 10}
										if obj[4]<=12:
											return 'True'
										elif obj[4]>12:
											return 'True'
										else: return 'True'
									elif obj[5]>1.0:
										# {"feature": "Occupation", "instances": 9, "metric_value": 0.2667, "depth": 10}
										if obj[4]>9:
											return 'True'
										elif obj[4]<=9:
											return 'False'
										else: return 'False'
									else: return 'False'
								elif obj[7]<=-1.0:
									return 'False'
								else: return 'False'
							else: return 'False'
						elif obj[8]>0:
							# {"feature": "Education", "instances": 177, "metric_value": 0.4858, "depth": 7}
							if obj[3]<=2:
								# {"feature": "Occupation", "instances": 144, "metric_value": 0.4859, "depth": 8}
								if obj[4]<=14.164944200311755:
									# {"feature": "Bar", "instances": 123, "metric_value": 0.4902, "depth": 9}
									if obj[5]>-1.0:
										# {"feature": "Restaurant20to50", "instances": 121, "metric_value": 0.4909, "depth": 10}
										if obj[7]<=2.0:
											return 'True'
										elif obj[7]>2.0:
											return 'True'
										else: return 'True'
									elif obj[5]<=-1.0:
										return 'False'
									else: return 'False'
								elif obj[4]>14.164944200311755:
									# {"feature": "Bar", "instances": 21, "metric_value": 0.3429, "depth": 9}
									if obj[5]>0.0:
										# {"feature": "Restaurant20to50", "instances": 15, "metric_value": 0.3636, "depth": 10}
										if obj[7]<=1.0:
											return 'False'
										elif obj[7]>1.0:
											return 'True'
										else: return 'True'
									elif obj[5]<=0.0:
										return 'True'
									else: return 'True'
								else: return 'True'
							elif obj[3]>2:
								# {"feature": "Restaurant20to50", "instances": 33, "metric_value": 0.3663, "depth": 8}
								if obj[7]<=1.0:
									# {"feature": "Occupation", "instances": 26, "metric_value": 0.3067, "depth": 9}
									if obj[4]>3:
										# {"feature": "Bar", "instances": 17, "metric_value": 0.202, "depth": 10}
										if obj[5]>0.0:
											return 'False'
										elif obj[5]<=0.0:
											return 'False'
										else: return 'False'
									elif obj[4]<=3:
										# {"feature": "Bar", "instances": 9, "metric_value": 0.4921, "depth": 10}
										if obj[5]<=0.0:
											return 'False'
										elif obj[5]>0.0:
											return 'True'
										else: return 'True'
									else: return 'False'
								elif obj[7]>1.0:
									# {"feature": "Occupation", "instances": 7, "metric_value": 0.2381, "depth": 9}
									if obj[4]>1:
										# {"feature": "Bar", "instances": 6, "metric_value": 0.25, "depth": 10}
										if obj[5]>0.0:
											return 'True'
										elif obj[5]<=0.0:
											return 'True'
										else: return 'True'
									elif obj[4]<=1:
										return 'False'
									else: return 'False'
								else: return 'True'
							else: return 'False'
						else: return 'True'
					elif obj[1]>3:
						# {"feature": "Occupation", "instances": 157, "metric_value": 0.4776, "depth": 6}
						if obj[4]<=8.490445859872612:
							# {"feature": "Education", "instances": 89, "metric_value": 0.4512, "depth": 7}
							if obj[3]>0:
								# {"feature": "Restaurant20to50", "instances": 50, "metric_value": 0.4622, "depth": 8}
								if obj[7]>0.0:
									# {"feature": "Bar", "instances": 43, "metric_value": 0.4765, "depth": 9}
									if obj[5]>-1.0:
										# {"feature": "Direction_same", "instances": 41, "metric_value": 0.4997, "depth": 10}
										if obj[8]<=0:
											return 'True'
										else: return 'True'
									elif obj[5]<=-1.0:
										return 'True'
									else: return 'True'
								elif obj[7]<=0.0:
									# {"feature": "Bar", "instances": 7, "metric_value": 0.2381, "depth": 9}
									if obj[5]>-1.0:
										# {"feature": "Direction_same", "instances": 6, "metric_value": 0.2778, "depth": 10}
										if obj[8]<=0:
											return 'True'
										else: return 'True'
									elif obj[5]<=-1.0:
										return 'True'
									else: return 'True'
								else: return 'True'
							elif obj[3]<=0:
								# {"feature": "Bar", "instances": 39, "metric_value": 0.3779, "depth": 8}
								if obj[5]>-1.0:
									# {"feature": "Restaurant20to50", "instances": 38, "metric_value": 0.3775, "depth": 9}
									if obj[7]<=1.0:
										# {"feature": "Direction_same", "instances": 24, "metric_value": 0.3299, "depth": 10}
										if obj[8]<=0:
											return 'True'
										else: return 'True'
									elif obj[7]>1.0:
										# {"feature": "Direction_same", "instances": 14, "metric_value": 0.4592, "depth": 10}
										if obj[8]<=0:
											return 'True'
										else: return 'True'
									else: return 'True'
								elif obj[5]<=-1.0:
									return 'False'
								else: return 'False'
							else: return 'True'
						elif obj[4]>8.490445859872612:
							# {"feature": "Bar", "instances": 68, "metric_value": 0.4644, "depth": 7}
							if obj[5]<=1.0:
								# {"feature": "Restaurant20to50", "instances": 50, "metric_value": 0.471, "depth": 8}
								if obj[7]<=1.0:
									# {"feature": "Education", "instances": 40, "metric_value": 0.4534, "depth": 9}
									if obj[3]<=3:
										# {"feature": "Direction_same", "instances": 34, "metric_value": 0.4844, "depth": 10}
										if obj[8]<=0:
											return 'True'
										else: return 'True'
									elif obj[3]>3:
										# {"feature": "Direction_same", "instances": 6, "metric_value": 0.2778, "depth": 10}
										if obj[8]<=0:
											return 'True'
										else: return 'True'
									else: return 'True'
								elif obj[7]>1.0:
									# {"feature": "Education", "instances": 10, "metric_value": 0.2667, "depth": 9}
									if obj[3]<=3:
										# {"feature": "Direction_same", "instances": 6, "metric_value": 0.4444, "depth": 10}
										if obj[8]<=0:
											return 'True'
										else: return 'True'
									elif obj[3]>3:
										return 'False'
									else: return 'False'
								else: return 'False'
							elif obj[5]>1.0:
								# {"feature": "Restaurant20to50", "instances": 18, "metric_value": 0.3889, "depth": 8}
								if obj[7]<=1.0:
									# {"feature": "Education", "instances": 12, "metric_value": 0.4167, "depth": 9}
									if obj[3]<=0:
										# {"feature": "Direction_same", "instances": 8, "metric_value": 0.375, "depth": 10}
										if obj[8]<=0:
											return 'False'
										else: return 'False'
									elif obj[3]>0:
										# {"feature": "Direction_same", "instances": 4, "metric_value": 0.5, "depth": 10}
										if obj[8]<=0:
											return 'False'
										else: return 'False'
									else: return 'False'
								elif obj[7]>1.0:
									# {"feature": "Education", "instances": 6, "metric_value": 0.0, "depth": 9}
									if obj[3]>1:
										return 'False'
									elif obj[3]<=1:
										return 'True'
									else: return 'True'
								else: return 'False'
							else: return 'False'
						else: return 'False'
					else: return 'True'
				else: return 'False'
			elif obj[0]>1:
				# {"feature": "Occupation", "instances": 1090, "metric_value": 0.458, "depth": 4}
				if obj[4]>1.7265574939131305:
					# {"feature": "Distance", "instances": 900, "metric_value": 0.469, "depth": 5}
					if obj[9]>1:
						# {"feature": "Time", "instances": 600, "metric_value": 0.4548, "depth": 6}
						if obj[1]>0:
							# {"feature": "Education", "instances": 477, "metric_value": 0.4657, "depth": 7}
							if obj[3]>1:
								# {"feature": "Bar", "instances": 249, "metric_value": 0.4823, "depth": 8}
								if obj[5]>-1.0:
									# {"feature": "Restaurant20to50", "instances": 248, "metric_value": 0.4829, "depth": 9}
									if obj[7]>-1.0:
										# {"feature": "Direction_same", "instances": 247, "metric_value": 0.4848, "depth": 10}
										if obj[8]<=0:
											return 'True'
										else: return 'True'
									elif obj[7]<=-1.0:
										return 'True'
									else: return 'True'
								elif obj[5]<=-1.0:
									return 'False'
								else: return 'False'
							elif obj[3]<=1:
								# {"feature": "Bar", "instances": 228, "metric_value": 0.4389, "depth": 8}
								if obj[5]<=0.0:
									# {"feature": "Restaurant20to50", "instances": 114, "metric_value": 0.4611, "depth": 9}
									if obj[7]>0.0:
										# {"feature": "Direction_same", "instances": 77, "metric_value": 0.4932, "depth": 10}
										if obj[8]<=0:
											return 'True'
										else: return 'True'
									elif obj[7]<=0.0:
										# {"feature": "Direction_same", "instances": 37, "metric_value": 0.3944, "depth": 10}
										if obj[8]<=0:
											return 'True'
										else: return 'True'
									else: return 'True'
								elif obj[5]>0.0:
									# {"feature": "Restaurant20to50", "instances": 114, "metric_value": 0.3991, "depth": 9}
									if obj[7]>0.0:
										# {"feature": "Direction_same", "instances": 90, "metric_value": 0.3805, "depth": 10}
										if obj[8]<=0:
											return 'True'
										else: return 'True'
									elif obj[7]<=0.0:
										# {"feature": "Direction_same", "instances": 24, "metric_value": 0.4688, "depth": 10}
										if obj[8]<=0:
											return 'True'
										else: return 'True'
									else: return 'True'
								else: return 'True'
							else: return 'True'
						elif obj[1]<=0:
							# {"feature": "Education", "instances": 123, "metric_value": 0.3882, "depth": 7}
							if obj[3]>0:
								# {"feature": "Restaurant20to50", "instances": 78, "metric_value": 0.3364, "depth": 8}
								if obj[7]<=2.0:
									# {"feature": "Bar", "instances": 73, "metric_value": 0.3251, "depth": 9}
									if obj[5]<=3.0:
										# {"feature": "Direction_same", "instances": 70, "metric_value": 0.32, "depth": 10}
										if obj[8]<=0:
											return 'True'
										else: return 'True'
									elif obj[5]>3.0:
										# {"feature": "Direction_same", "instances": 3, "metric_value": 0.4444, "depth": 10}
										if obj[8]<=0:
											return 'True'
										else: return 'True'
									else: return 'True'
								elif obj[7]>2.0:
									# {"feature": "Bar", "instances": 5, "metric_value": 0.4667, "depth": 9}
									if obj[5]>0.0:
										# {"feature": "Direction_same", "instances": 3, "metric_value": 0.4444, "depth": 10}
										if obj[8]<=0:
											return 'True'
										else: return 'True'
									elif obj[5]<=0.0:
										# {"feature": "Direction_same", "instances": 2, "metric_value": 0.5, "depth": 10}
										if obj[8]<=0:
											return 'True'
										else: return 'True'
									else: return 'True'
								else: return 'True'
							elif obj[3]<=0:
								# {"feature": "Bar", "instances": 45, "metric_value": 0.4525, "depth": 8}
								if obj[5]>-1.0:
									# {"feature": "Restaurant20to50", "instances": 44, "metric_value": 0.4525, "depth": 9}
									if obj[7]<=1.0:
										# {"feature": "Direction_same", "instances": 35, "metric_value": 0.48, "depth": 10}
										if obj[8]<=0:
											return 'True'
										else: return 'True'
									elif obj[7]>1.0:
										# {"feature": "Direction_same", "instances": 9, "metric_value": 0.3457, "depth": 10}
										if obj[8]<=0:
											return 'True'
										else: return 'True'
									else: return 'True'
								elif obj[5]<=-1.0:
									return 'False'
								else: return 'False'
							else: return 'True'
						else: return 'True'
					elif obj[9]<=1:
						# {"feature": "Time", "instances": 300, "metric_value": 0.4853, "depth": 6}
						if obj[1]<=2:
							# {"feature": "Education", "instances": 185, "metric_value": 0.4876, "depth": 7}
							if obj[3]>1:
								# {"feature": "Bar", "instances": 99, "metric_value": 0.4708, "depth": 8}
								if obj[5]>-1.0:
									# {"feature": "Restaurant20to50", "instances": 95, "metric_value": 0.4817, "depth": 9}
									if obj[7]<=2.0:
										# {"feature": "Direction_same", "instances": 91, "metric_value": 0.4864, "depth": 10}
										if obj[8]<=0:
											return 'False'
										else: return 'False'
									elif obj[7]>2.0:
										# {"feature": "Direction_same", "instances": 4, "metric_value": 0.375, "depth": 10}
										if obj[8]<=0:
											return 'True'
										else: return 'True'
									else: return 'True'
								elif obj[5]<=-1.0:
									return 'True'
								else: return 'True'
							elif obj[3]<=1:
								# {"feature": "Bar", "instances": 86, "metric_value": 0.4403, "depth": 8}
								if obj[5]>-1.0:
									# {"feature": "Restaurant20to50", "instances": 79, "metric_value": 0.4521, "depth": 9}
									if obj[7]<=1.0:
										# {"feature": "Direction_same", "instances": 63, "metric_value": 0.4717, "depth": 10}
										if obj[8]<=0:
											return 'True'
										else: return 'True'
									elif obj[7]>1.0:
										# {"feature": "Direction_same", "instances": 16, "metric_value": 0.375, "depth": 10}
										if obj[8]<=0:
											return 'True'
										else: return 'True'
									else: return 'True'
								elif obj[5]<=-1.0:
									# {"feature": "Restaurant20to50", "instances": 7, "metric_value": 0.2286, "depth": 9}
									if obj[7]<=-1.0:
										# {"feature": "Direction_same", "instances": 5, "metric_value": 0.32, "depth": 10}
										if obj[8]<=0:
											return 'False'
										else: return 'False'
									elif obj[7]>-1.0:
										return 'False'
									else: return 'False'
								else: return 'False'
							else: return 'True'
						elif obj[1]>2:
							# {"feature": "Bar", "instances": 115, "metric_value": 0.449, "depth": 7}
							if obj[5]<=0.0:
								# {"feature": "Education", "instances": 60, "metric_value": 0.3915, "depth": 8}
								if obj[3]<=3:
									# {"feature": "Restaurant20to50", "instances": 55, "metric_value": 0.4199, "depth": 9}
									if obj[7]<=2.0:
										# {"feature": "Direction_same", "instances": 53, "metric_value": 0.4357, "depth": 10}
										if obj[8]<=0:
											return 'True'
										else: return 'True'
									elif obj[7]>2.0:
										return 'True'
									else: return 'True'
								elif obj[3]>3:
									return 'True'
								else: return 'True'
							elif obj[5]>0.0:
								# {"feature": "Restaurant20to50", "instances": 55, "metric_value": 0.4628, "depth": 8}
								if obj[7]<=1.0:
									# {"feature": "Education", "instances": 36, "metric_value": 0.454, "depth": 9}
									if obj[3]<=3:
										# {"feature": "Direction_same", "instances": 35, "metric_value": 0.4669, "depth": 10}
										if obj[8]<=0:
											return 'True'
										else: return 'True'
									elif obj[3]>3:
										return 'True'
									else: return 'True'
								elif obj[7]>1.0:
									# {"feature": "Education", "instances": 19, "metric_value": 0.4173, "depth": 9}
									if obj[3]>1:
										# {"feature": "Direction_same", "instances": 12, "metric_value": 0.375, "depth": 10}
										if obj[8]<=0:
											return 'False'
										else: return 'False'
									elif obj[3]<=1:
										# {"feature": "Direction_same", "instances": 7, "metric_value": 0.4898, "depth": 10}
										if obj[8]<=0:
											return 'True'
										else: return 'True'
									else: return 'True'
								else: return 'False'
							else: return 'True'
						else: return 'True'
					else: return 'True'
				elif obj[4]<=1.7265574939131305:
					# {"feature": "Bar", "instances": 190, "metric_value": 0.3878, "depth": 5}
					if obj[5]<=1.0:
						# {"feature": "Distance", "instances": 141, "metric_value": 0.414, "depth": 6}
						if obj[9]>1:
							# {"feature": "Time", "instances": 91, "metric_value": 0.3842, "depth": 7}
							if obj[1]<=2:
								# {"feature": "Education", "instances": 49, "metric_value": 0.4035, "depth": 8}
								if obj[3]<=3:
									# {"feature": "Restaurant20to50", "instances": 44, "metric_value": 0.4344, "depth": 9}
									if obj[7]>0.0:
										# {"feature": "Direction_same", "instances": 30, "metric_value": 0.48, "depth": 10}
										if obj[8]<=0:
											return 'True'
										else: return 'True'
									elif obj[7]<=0.0:
										# {"feature": "Direction_same", "instances": 14, "metric_value": 0.3367, "depth": 10}
										if obj[8]<=0:
											return 'True'
										else: return 'True'
									else: return 'True'
								elif obj[3]>3:
									return 'True'
								else: return 'True'
							elif obj[1]>2:
								# {"feature": "Education", "instances": 42, "metric_value": 0.2983, "depth": 8}
								if obj[3]<=2:
									# {"feature": "Restaurant20to50", "instances": 34, "metric_value": 0.249, "depth": 9}
									if obj[7]>0.0:
										# {"feature": "Direction_same", "instances": 24, "metric_value": 0.2778, "depth": 10}
										if obj[8]<=0:
											return 'True'
										else: return 'True'
									elif obj[7]<=0.0:
										# {"feature": "Direction_same", "instances": 10, "metric_value": 0.18, "depth": 10}
										if obj[8]<=0:
											return 'True'
										else: return 'True'
									else: return 'True'
								elif obj[3]>2:
									# {"feature": "Restaurant20to50", "instances": 8, "metric_value": 0.4286, "depth": 9}
									if obj[7]<=1.0:
										# {"feature": "Direction_same", "instances": 7, "metric_value": 0.4898, "depth": 10}
										if obj[8]<=0:
											return 'False'
										else: return 'False'
									elif obj[7]>1.0:
										return 'True'
									else: return 'True'
								else: return 'True'
							else: return 'True'
						elif obj[9]<=1:
							# {"feature": "Time", "instances": 50, "metric_value": 0.403, "depth": 7}
							if obj[1]>0:
								# {"feature": "Education", "instances": 40, "metric_value": 0.3635, "depth": 8}
								if obj[3]>0:
									# {"feature": "Restaurant20to50", "instances": 24, "metric_value": 0.2698, "depth": 9}
									if obj[7]<=1.0:
										# {"feature": "Direction_same", "instances": 21, "metric_value": 0.3084, "depth": 10}
										if obj[8]<=0:
											return 'True'
										else: return 'True'
									elif obj[7]>1.0:
										return 'True'
									else: return 'True'
								elif obj[3]<=0:
									# {"feature": "Restaurant20to50", "instances": 16, "metric_value": 0.3462, "depth": 9}
									if obj[7]<=1.0:
										# {"feature": "Direction_same", "instances": 13, "metric_value": 0.426, "depth": 10}
										if obj[8]<=0:
											return 'True'
										else: return 'True'
									elif obj[7]>1.0:
										return 'False'
									else: return 'False'
								else: return 'True'
							elif obj[1]<=0:
								# {"feature": "Restaurant20to50", "instances": 10, "metric_value": 0.3111, "depth": 8}
								if obj[7]<=1.0:
									# {"feature": "Education", "instances": 9, "metric_value": 0.3175, "depth": 9}
									if obj[3]>0:
										# {"feature": "Direction_same", "instances": 7, "metric_value": 0.4082, "depth": 10}
										if obj[8]<=0:
											return 'False'
										else: return 'False'
									elif obj[3]<=0:
										return 'False'
									else: return 'False'
								elif obj[7]>1.0:
									return 'True'
								else: return 'True'
							else: return 'False'
						else: return 'True'
					elif obj[5]>1.0:
						# {"feature": "Time", "instances": 49, "metric_value": 0.2956, "depth": 6}
						if obj[1]<=3:
							# {"feature": "Distance", "instances": 33, "metric_value": 0.2389, "depth": 7}
							if obj[9]>1:
								# {"feature": "Restaurant20to50", "instances": 17, "metric_value": 0.0941, "depth": 8}
								if obj[7]<=1.0:
									return 'True'
								elif obj[7]>1.0:
									# {"feature": "Education", "instances": 5, "metric_value": 0.2667, "depth": 9}
									if obj[3]<=0:
										# {"feature": "Direction_same", "instances": 3, "metric_value": 0.4444, "depth": 10}
										if obj[8]<=0:
											return 'True'
										else: return 'True'
									elif obj[3]>0:
										return 'True'
									else: return 'True'
								else: return 'True'
							elif obj[9]<=1:
								# {"feature": "Education", "instances": 16, "metric_value": 0.3571, "depth": 8}
								if obj[3]<=2:
									# {"feature": "Restaurant20to50", "instances": 14, "metric_value": 0.3095, "depth": 9}
									if obj[7]>0.0:
										# {"feature": "Direction_same", "instances": 12, "metric_value": 0.2778, "depth": 10}
										if obj[8]<=0:
											return 'True'
										else: return 'True'
									elif obj[7]<=0.0:
										# {"feature": "Direction_same", "instances": 2, "metric_value": 0.5, "depth": 10}
										if obj[8]<=0:
											return 'False'
										else: return 'False'
									else: return 'False'
								elif obj[3]>2:
									# {"feature": "Restaurant20to50", "instances": 2, "metric_value": 0.5, "depth": 9}
									if obj[7]<=1.0:
										# {"feature": "Direction_same", "instances": 2, "metric_value": 0.5, "depth": 10}
										if obj[8]<=0:
											return 'False'
										else: return 'False'
									else: return 'False'
								else: return 'False'
							else: return 'True'
						elif obj[1]>3:
							# {"feature": "Distance", "instances": 16, "metric_value": 0.3, "depth": 7}
							if obj[9]>1:
								# {"feature": "Education", "instances": 10, "metric_value": 0.3167, "depth": 8}
								if obj[3]<=1:
									# {"feature": "Restaurant20to50", "instances": 6, "metric_value": 0.25, "depth": 9}
									if obj[7]>0.0:
										# {"feature": "Direction_same", "instances": 4, "metric_value": 0.375, "depth": 10}
										if obj[8]<=0:
											return 'True'
										else: return 'True'
									elif obj[7]<=0.0:
										return 'True'
									else: return 'True'
								elif obj[3]>1:
									# {"feature": "Restaurant20to50", "instances": 4, "metric_value": 0.375, "depth": 9}
									if obj[7]<=1.0:
										# {"feature": "Direction_same", "instances": 4, "metric_value": 0.375, "depth": 10}
										if obj[8]<=0:
											return 'False'
										else: return 'False'
									else: return 'False'
								else: return 'False'
							elif obj[9]<=1:
								return 'True'
							else: return 'True'
						else: return 'True'
					else: return 'True'
				else: return 'True'
			else: return 'True'
		elif obj[6]>1.0:
			# {"feature": "Distance", "instances": 2885, "metric_value": 0.412, "depth": 3}
			if obj[9]<=2:
				# {"feature": "Passanger", "instances": 2614, "metric_value": 0.4001, "depth": 4}
				if obj[0]<=2:
					# {"feature": "Occupation", "instances": 1699, "metric_value": 0.4228, "depth": 5}
					if obj[4]<=18.185882392956827:
						# {"feature": "Direction_same", "instances": 1580, "metric_value": 0.4321, "depth": 6}
						if obj[8]<=0:
							# {"feature": "Time", "instances": 1024, "metric_value": 0.4381, "depth": 7}
							if obj[1]>1:
								# {"feature": "Bar", "instances": 553, "metric_value": 0.3955, "depth": 8}
								if obj[5]<=1.0:
									# {"feature": "Education", "instances": 337, "metric_value": 0.3654, "depth": 9}
									if obj[3]>0:
										# {"feature": "Restaurant20to50", "instances": 226, "metric_value": 0.3926, "depth": 10}
										if obj[7]<=2.0:
											return 'True'
										elif obj[7]>2.0:
											return 'True'
										else: return 'True'
									elif obj[3]<=0:
										# {"feature": "Restaurant20to50", "instances": 111, "metric_value": 0.2967, "depth": 10}
										if obj[7]>0.0:
											return 'True'
										elif obj[7]<=0.0:
											return 'True'
										else: return 'True'
									else: return 'True'
								elif obj[5]>1.0:
									# {"feature": "Education", "instances": 216, "metric_value": 0.4289, "depth": 9}
									if obj[3]>1:
										# {"feature": "Restaurant20to50", "instances": 156, "metric_value": 0.4005, "depth": 10}
										if obj[7]>0.0:
											return 'True'
										elif obj[7]<=0.0:
											return 'True'
										else: return 'True'
									elif obj[3]<=1:
										# {"feature": "Restaurant20to50", "instances": 60, "metric_value": 0.4854, "depth": 10}
										if obj[7]>0.0:
											return 'True'
										elif obj[7]<=0.0:
											return 'False'
										else: return 'False'
									else: return 'True'
								else: return 'True'
							elif obj[1]<=1:
								# {"feature": "Bar", "instances": 471, "metric_value": 0.4804, "depth": 8}
								if obj[5]>0.0:
									# {"feature": "Education", "instances": 331, "metric_value": 0.489, "depth": 9}
									if obj[3]<=3:
										# {"feature": "Restaurant20to50", "instances": 309, "metric_value": 0.4916, "depth": 10}
										if obj[7]>-1.0:
											return 'True'
										elif obj[7]<=-1.0:
											return 'True'
										else: return 'True'
									elif obj[3]>3:
										# {"feature": "Restaurant20to50", "instances": 22, "metric_value": 0.3955, "depth": 10}
										if obj[7]<=3.0:
											return 'True'
										elif obj[7]>3.0:
											return 'True'
										else: return 'True'
									else: return 'True'
								elif obj[5]<=0.0:
									# {"feature": "Restaurant20to50", "instances": 140, "metric_value": 0.4472, "depth": 9}
									if obj[7]>-1.0:
										# {"feature": "Education", "instances": 138, "metric_value": 0.4534, "depth": 10}
										if obj[3]>0:
											return 'True'
										elif obj[3]<=0:
											return 'True'
										else: return 'True'
									elif obj[7]<=-1.0:
										return 'True'
									else: return 'True'
								else: return 'True'
							else: return 'True'
						elif obj[8]>0:
							# {"feature": "Time", "instances": 556, "metric_value": 0.3922, "depth": 7}
							if obj[1]<=1:
								# {"feature": "Education", "instances": 451, "metric_value": 0.3659, "depth": 8}
								if obj[3]>1:
									# {"feature": "Restaurant20to50", "instances": 273, "metric_value": 0.3959, "depth": 9}
									if obj[7]<=1.0:
										# {"feature": "Bar", "instances": 157, "metric_value": 0.4233, "depth": 10}
										if obj[5]<=3.0:
											return 'True'
										elif obj[5]>3.0:
											return 'True'
										else: return 'True'
									elif obj[7]>1.0:
										# {"feature": "Bar", "instances": 116, "metric_value": 0.3455, "depth": 10}
										if obj[5]>0.0:
											return 'True'
										elif obj[5]<=0.0:
											return 'True'
										else: return 'True'
									else: return 'True'
								elif obj[3]<=1:
									# {"feature": "Bar", "instances": 178, "metric_value": 0.3125, "depth": 9}
									if obj[5]<=2.0:
										# {"feature": "Restaurant20to50", "instances": 155, "metric_value": 0.2929, "depth": 10}
										if obj[7]>0.0:
											return 'True'
										elif obj[7]<=0.0:
											return 'True'
										else: return 'True'
									elif obj[5]>2.0:
										# {"feature": "Restaurant20to50", "instances": 23, "metric_value": 0.4161, "depth": 10}
										if obj[7]<=2.0:
											return 'True'
										elif obj[7]>2.0:
											return 'False'
										else: return 'False'
									else: return 'True'
								else: return 'True'
							elif obj[1]>1:
								# {"feature": "Restaurant20to50", "instances": 105, "metric_value": 0.4749, "depth": 8}
								if obj[7]<=2.0:
									# {"feature": "Education", "instances": 90, "metric_value": 0.4651, "depth": 9}
									if obj[3]<=3:
										# {"feature": "Bar", "instances": 86, "metric_value": 0.4858, "depth": 10}
										if obj[5]<=2.0:
											return 'True'
										elif obj[5]>2.0:
											return 'True'
										else: return 'True'
									elif obj[3]>3:
										return 'True'
									else: return 'True'
								elif obj[7]>2.0:
									# {"feature": "Bar", "instances": 15, "metric_value": 0.3636, "depth": 9}
									if obj[5]>1.0:
										# {"feature": "Education", "instances": 11, "metric_value": 0.3409, "depth": 10}
										if obj[3]<=2:
											return 'True'
										elif obj[3]>2:
											return 'False'
										else: return 'False'
									elif obj[5]<=1.0:
										return 'False'
									else: return 'False'
								else: return 'False'
							else: return 'True'
						else: return 'True'
					elif obj[4]>18.185882392956827:
						# {"feature": "Bar", "instances": 119, "metric_value": 0.2679, "depth": 6}
						if obj[5]<=2.0:
							# {"feature": "Education", "instances": 98, "metric_value": 0.2244, "depth": 7}
							if obj[3]<=2:
								# {"feature": "Time", "instances": 64, "metric_value": 0.1618, "depth": 8}
								if obj[1]>0:
									# {"feature": "Restaurant20to50", "instances": 50, "metric_value": 0.1087, "depth": 9}
									if obj[7]<=1.0:
										# {"feature": "Direction_same", "instances": 32, "metric_value": 0.1594, "depth": 10}
										if obj[8]<=0:
											return 'True'
										elif obj[8]>0:
											return 'True'
										else: return 'True'
									elif obj[7]>1.0:
										return 'True'
									else: return 'True'
								elif obj[1]<=0:
									# {"feature": "Restaurant20to50", "instances": 14, "metric_value": 0.3214, "depth": 9}
									if obj[7]<=1.0:
										# {"feature": "Direction_same", "instances": 12, "metric_value": 0.375, "depth": 10}
										if obj[8]<=0:
											return 'True'
										elif obj[8]>0:
											return 'True'
										else: return 'True'
									elif obj[7]>1.0:
										return 'True'
									else: return 'True'
								else: return 'True'
							elif obj[3]>2:
								# {"feature": "Time", "instances": 34, "metric_value": 0.2864, "depth": 8}
								if obj[1]>0:
									# {"feature": "Restaurant20to50", "instances": 23, "metric_value": 0.3959, "depth": 9}
									if obj[7]<=1.0:
										# {"feature": "Direction_same", "instances": 12, "metric_value": 0.4857, "depth": 10}
										if obj[8]>0:
											return 'True'
										elif obj[8]<=0:
											return 'True'
										else: return 'True'
									elif obj[7]>1.0:
										# {"feature": "Direction_same", "instances": 11, "metric_value": 0.2828, "depth": 10}
										if obj[8]<=0:
											return 'True'
										elif obj[8]>0:
											return 'True'
										else: return 'True'
									else: return 'True'
								elif obj[1]<=0:
									return 'True'
								else: return 'True'
							else: return 'True'
						elif obj[5]>2.0:
							# {"feature": "Restaurant20to50", "instances": 21, "metric_value": 0.2424, "depth": 7}
							if obj[7]>1.0:
								# {"feature": "Education", "instances": 11, "metric_value": 0.3636, "depth": 8}
								if obj[3]<=0:
									# {"feature": "Direction_same", "instances": 8, "metric_value": 0.375, "depth": 9}
									if obj[8]<=0:
										# {"feature": "Time", "instances": 4, "metric_value": 0.25, "depth": 10}
										if obj[1]>1:
											return 'True'
										elif obj[1]<=1:
											return 'True'
										else: return 'True'
									elif obj[8]>0:
										# {"feature": "Time", "instances": 4, "metric_value": 0.3333, "depth": 10}
										if obj[1]>0:
											return 'False'
										elif obj[1]<=0:
											return 'False'
										else: return 'False'
									else: return 'False'
								elif obj[3]>0:
									return 'False'
								else: return 'False'
							elif obj[7]<=1.0:
								return 'True'
							else: return 'True'
						else: return 'True'
					else: return 'True'
				elif obj[0]>2:
					# {"feature": "Bar", "instances": 915, "metric_value": 0.3493, "depth": 5}
					if obj[5]<=3.0:
						# {"feature": "Time", "instances": 854, "metric_value": 0.3376, "depth": 6}
						if obj[1]<=2:
							# {"feature": "Education", "instances": 516, "metric_value": 0.3, "depth": 7}
							if obj[3]<=3:
								# {"feature": "Occupation", "instances": 486, "metric_value": 0.3121, "depth": 8}
								if obj[4]>2.557115496448203:
									# {"feature": "Restaurant20to50", "instances": 402, "metric_value": 0.3302, "depth": 9}
									if obj[7]<=2.0:
										# {"feature": "Direction_same", "instances": 367, "metric_value": 0.3187, "depth": 10}
										if obj[8]<=0:
											return 'True'
										else: return 'True'
									elif obj[7]>2.0:
										# {"feature": "Direction_same", "instances": 35, "metric_value": 0.4506, "depth": 10}
										if obj[8]<=0:
											return 'True'
										else: return 'True'
									else: return 'True'
								elif obj[4]<=2.557115496448203:
									# {"feature": "Restaurant20to50", "instances": 84, "metric_value": 0.2076, "depth": 9}
									if obj[7]<=2.0:
										# {"feature": "Direction_same", "instances": 78, "metric_value": 0.2235, "depth": 10}
										if obj[8]<=0:
											return 'True'
										else: return 'True'
									elif obj[7]>2.0:
										return 'True'
									else: return 'True'
								else: return 'True'
							elif obj[3]>3:
								# {"feature": "Occupation", "instances": 30, "metric_value": 0.0444, "depth": 8}
								if obj[4]>1:
									return 'True'
								elif obj[4]<=1:
									# {"feature": "Restaurant20to50", "instances": 3, "metric_value": 0.3333, "depth": 9}
									if obj[7]>0.0:
										# {"feature": "Direction_same", "instances": 2, "metric_value": 0.5, "depth": 10}
										if obj[8]<=0:
											return 'True'
										else: return 'True'
									elif obj[7]<=0.0:
										return 'True'
									else: return 'True'
								else: return 'True'
							else: return 'True'
						elif obj[1]>2:
							# {"feature": "Education", "instances": 338, "metric_value": 0.381, "depth": 7}
							if obj[3]<=2:
								# {"feature": "Occupation", "instances": 236, "metric_value": 0.3403, "depth": 8}
								if obj[4]<=7.656779661016949:
									# {"feature": "Restaurant20to50", "instances": 147, "metric_value": 0.374, "depth": 9}
									if obj[7]<=1.0:
										# {"feature": "Direction_same", "instances": 93, "metric_value": 0.4028, "depth": 10}
										if obj[8]<=0:
											return 'True'
										else: return 'True'
									elif obj[7]>1.0:
										# {"feature": "Direction_same", "instances": 54, "metric_value": 0.3244, "depth": 10}
										if obj[8]<=0:
											return 'True'
										else: return 'True'
									else: return 'True'
								elif obj[4]>7.656779661016949:
									# {"feature": "Restaurant20to50", "instances": 89, "metric_value": 0.2783, "depth": 9}
									if obj[7]<=3.0:
										# {"feature": "Direction_same", "instances": 86, "metric_value": 0.288, "depth": 10}
										if obj[8]<=0:
											return 'True'
										else: return 'True'
									elif obj[7]>3.0:
										return 'True'
									else: return 'True'
								else: return 'True'
							elif obj[3]>2:
								# {"feature": "Occupation", "instances": 102, "metric_value": 0.4493, "depth": 8}
								if obj[4]<=13:
									# {"feature": "Restaurant20to50", "instances": 84, "metric_value": 0.4824, "depth": 9}
									if obj[7]<=2.0:
										# {"feature": "Direction_same", "instances": 74, "metric_value": 0.4909, "depth": 10}
										if obj[8]<=0:
											return 'True'
										else: return 'True'
									elif obj[7]>2.0:
										# {"feature": "Direction_same", "instances": 10, "metric_value": 0.42, "depth": 10}
										if obj[8]<=0:
											return 'True'
										else: return 'True'
									else: return 'True'
								elif obj[4]>13:
									# {"feature": "Restaurant20to50", "instances": 18, "metric_value": 0.2667, "depth": 9}
									if obj[7]<=2.0:
										# {"feature": "Direction_same", "instances": 15, "metric_value": 0.32, "depth": 10}
										if obj[8]<=0:
											return 'True'
										else: return 'True'
									elif obj[7]>2.0:
										return 'True'
									else: return 'True'
								else: return 'True'
							else: return 'True'
						else: return 'True'
					elif obj[5]>3.0:
						# {"feature": "Time", "instances": 61, "metric_value": 0.4287, "depth": 6}
						if obj[1]>0:
							# {"feature": "Occupation", "instances": 49, "metric_value": 0.4074, "depth": 7}
							if obj[4]<=12:
								# {"feature": "Restaurant20to50", "instances": 36, "metric_value": 0.3676, "depth": 8}
								if obj[7]>0.0:
									# {"feature": "Education", "instances": 34, "metric_value": 0.3488, "depth": 9}
									if obj[3]>0:
										# {"feature": "Direction_same", "instances": 25, "metric_value": 0.4032, "depth": 10}
										if obj[8]<=0:
											return 'True'
										else: return 'True'
									elif obj[3]<=0:
										# {"feature": "Direction_same", "instances": 9, "metric_value": 0.1975, "depth": 10}
										if obj[8]<=0:
											return 'True'
										else: return 'True'
									else: return 'True'
								elif obj[7]<=0.0:
									# {"feature": "Education", "instances": 2, "metric_value": 0.5, "depth": 9}
									if obj[3]<=0:
										# {"feature": "Direction_same", "instances": 2, "metric_value": 0.5, "depth": 10}
										if obj[8]<=0:
											return 'True'
										else: return 'True'
									else: return 'True'
								else: return 'True'
							elif obj[4]>12:
								# {"feature": "Education", "instances": 13, "metric_value": 0.3916, "depth": 8}
								if obj[3]<=0:
									# {"feature": "Restaurant20to50", "instances": 11, "metric_value": 0.4606, "depth": 9}
									if obj[7]<=1.0:
										# {"feature": "Direction_same", "instances": 6, "metric_value": 0.4444, "depth": 10}
										if obj[8]<=0:
											return 'True'
										else: return 'True'
									elif obj[7]>1.0:
										# {"feature": "Direction_same", "instances": 5, "metric_value": 0.48, "depth": 10}
										if obj[8]<=0:
											return 'True'
										else: return 'True'
									else: return 'True'
								elif obj[3]>0:
									return 'False'
								else: return 'False'
							else: return 'True'
						elif obj[1]<=0:
							# {"feature": "Occupation", "instances": 12, "metric_value": 0.3333, "depth": 7}
							if obj[4]<=12:
								# {"feature": "Education", "instances": 8, "metric_value": 0.3333, "depth": 8}
								if obj[3]>0:
									# {"feature": "Restaurant20to50", "instances": 6, "metric_value": 0.4, "depth": 9}
									if obj[7]>1.0:
										# {"feature": "Direction_same", "instances": 5, "metric_value": 0.48, "depth": 10}
										if obj[8]<=0:
											return 'False'
										else: return 'False'
									elif obj[7]<=1.0:
										return 'False'
									else: return 'False'
								elif obj[3]<=0:
									return 'True'
								else: return 'True'
							elif obj[4]>12:
								return 'False'
							else: return 'False'
						else: return 'False'
					else: return 'True'
				else: return 'True'
			elif obj[9]>2:
				# {"feature": "Education", "instances": 271, "metric_value": 0.488, "depth": 4}
				if obj[3]>0:
					# {"feature": "Passanger", "instances": 191, "metric_value": 0.4838, "depth": 5}
					if obj[0]>0:
						# {"feature": "Bar", "instances": 184, "metric_value": 0.4821, "depth": 6}
						if obj[5]<=1.0:
							# {"feature": "Restaurant20to50", "instances": 106, "metric_value": 0.4587, "depth": 7}
							if obj[7]<=2.0:
								# {"feature": "Occupation", "instances": 102, "metric_value": 0.467, "depth": 8}
								if obj[4]<=13:
									# {"feature": "Time", "instances": 90, "metric_value": 0.4643, "depth": 9}
									if obj[1]<=1:
										# {"feature": "Direction_same", "instances": 70, "metric_value": 0.4669, "depth": 10}
										if obj[8]<=0:
											return 'False'
										else: return 'False'
									elif obj[1]>1:
										# {"feature": "Direction_same", "instances": 20, "metric_value": 0.455, "depth": 10}
										if obj[8]<=0:
											return 'False'
										else: return 'False'
									else: return 'False'
								elif obj[4]>13:
									# {"feature": "Time", "instances": 12, "metric_value": 0.4167, "depth": 9}
									if obj[1]>0:
										# {"feature": "Direction_same", "instances": 10, "metric_value": 0.5, "depth": 10}
										if obj[8]<=0:
											return 'False'
										else: return 'False'
									elif obj[1]<=0:
										return 'True'
									else: return 'True'
								else: return 'True'
							elif obj[7]>2.0:
								return 'False'
							else: return 'False'
						elif obj[5]>1.0:
							# {"feature": "Time", "instances": 78, "metric_value": 0.4797, "depth": 7}
							if obj[1]>0:
								# {"feature": "Occupation", "instances": 65, "metric_value": 0.4642, "depth": 8}
								if obj[4]<=16:
									# {"feature": "Restaurant20to50", "instances": 57, "metric_value": 0.4887, "depth": 9}
									if obj[7]>-1.0:
										# {"feature": "Direction_same", "instances": 56, "metric_value": 0.4974, "depth": 10}
										if obj[8]<=0:
											return 'True'
										else: return 'True'
									elif obj[7]<=-1.0:
										return 'False'
									else: return 'False'
								elif obj[4]>16:
									# {"feature": "Restaurant20to50", "instances": 8, "metric_value": 0.1667, "depth": 9}
									if obj[7]<=1.0:
										return 'True'
									elif obj[7]>1.0:
										# {"feature": "Direction_same", "instances": 3, "metric_value": 0.4444, "depth": 10}
										if obj[8]<=0:
											return 'True'
										else: return 'True'
									else: return 'True'
								else: return 'True'
							elif obj[1]<=0:
								# {"feature": "Occupation", "instances": 13, "metric_value": 0.3692, "depth": 8}
								if obj[4]<=11:
									# {"feature": "Restaurant20to50", "instances": 10, "metric_value": 0.4444, "depth": 9}
									if obj[7]>0.0:
										# {"feature": "Direction_same", "instances": 9, "metric_value": 0.4938, "depth": 10}
										if obj[8]<=0:
											return 'False'
										else: return 'False'
									elif obj[7]<=0.0:
										return 'False'
									else: return 'False'
								elif obj[4]>11:
									return 'False'
								else: return 'False'
							else: return 'False'
						else: return 'True'
					elif obj[0]<=0:
						# {"feature": "Occupation", "instances": 7, "metric_value": 0.1429, "depth": 6}
						if obj[4]>1:
							return 'True'
						elif obj[4]<=1:
							# {"feature": "Bar", "instances": 2, "metric_value": 0.0, "depth": 7}
							if obj[5]>0.0:
								return 'False'
							elif obj[5]<=0.0:
								return 'True'
							else: return 'True'
						else: return 'False'
					else: return 'True'
				elif obj[3]<=0:
					# {"feature": "Restaurant20to50", "instances": 80, "metric_value": 0.4549, "depth": 5}
					if obj[7]<=2.0:
						# {"feature": "Occupation", "instances": 72, "metric_value": 0.4538, "depth": 6}
						if obj[4]<=10:
							# {"feature": "Bar", "instances": 59, "metric_value": 0.4917, "depth": 7}
							if obj[5]<=3.0:
								# {"feature": "Time", "instances": 56, "metric_value": 0.4895, "depth": 8}
								if obj[1]<=1:
									# {"feature": "Passanger", "instances": 45, "metric_value": 0.4868, "depth": 9}
									if obj[0]>0:
										# {"feature": "Direction_same", "instances": 42, "metric_value": 0.4898, "depth": 10}
										if obj[8]<=0:
											return 'True'
										else: return 'True'
									elif obj[0]<=0:
										# {"feature": "Direction_same", "instances": 3, "metric_value": 0.4444, "depth": 10}
										if obj[8]<=0:
											return 'True'
										else: return 'True'
									else: return 'True'
								elif obj[1]>1:
									# {"feature": "Passanger", "instances": 11, "metric_value": 0.4959, "depth": 9}
									if obj[0]<=1:
										# {"feature": "Direction_same", "instances": 11, "metric_value": 0.4959, "depth": 10}
										if obj[8]<=0:
											return 'False'
										else: return 'False'
									else: return 'False'
								else: return 'False'
							elif obj[5]>3.0:
								# {"feature": "Passanger", "instances": 3, "metric_value": 0.4444, "depth": 8}
								if obj[0]<=1:
									# {"feature": "Time", "instances": 3, "metric_value": 0.4444, "depth": 9}
									if obj[1]<=1:
										# {"feature": "Direction_same", "instances": 3, "metric_value": 0.4444, "depth": 10}
										if obj[8]<=0:
											return 'False'
										else: return 'False'
									else: return 'False'
								else: return 'False'
							else: return 'False'
						elif obj[4]>10:
							# {"feature": "Bar", "instances": 13, "metric_value": 0.1846, "depth": 7}
							if obj[5]>0.0:
								return 'True'
							elif obj[5]<=0.0:
								# {"feature": "Passanger", "instances": 5, "metric_value": 0.48, "depth": 8}
								if obj[0]<=1:
									# {"feature": "Time", "instances": 5, "metric_value": 0.48, "depth": 9}
									if obj[1]<=1:
										# {"feature": "Direction_same", "instances": 5, "metric_value": 0.48, "depth": 10}
										if obj[8]<=0:
											return 'True'
										else: return 'True'
									else: return 'True'
								else: return 'True'
							else: return 'True'
						else: return 'True'
					elif obj[7]>2.0:
						# {"feature": "Occupation", "instances": 8, "metric_value": 0.0, "depth": 6}
						if obj[4]<=7:
							return 'True'
						elif obj[4]>7:
							return 'False'
						else: return 'False'
					else: return 'True'
				else: return 'True'
			else: return 'True'
		else: return 'True'
	elif obj[2]<=1:
		# {"feature": "Bar", "instances": 2244, "metric_value": 0.4571, "depth": 2}
		if obj[5]<=1.0:
			# {"feature": "Passanger", "instances": 1582, "metric_value": 0.4435, "depth": 3}
			if obj[0]<=2:
				# {"feature": "Education", "instances": 1363, "metric_value": 0.4284, "depth": 4}
				if obj[3]>0:
					# {"feature": "Time", "instances": 875, "metric_value": 0.3931, "depth": 5}
					if obj[1]>0:
						# {"feature": "Coffeehouse", "instances": 584, "metric_value": 0.3532, "depth": 6}
						if obj[6]<=3.0:
							# {"feature": "Restaurant20to50", "instances": 548, "metric_value": 0.3667, "depth": 7}
							if obj[7]<=1.0:
								# {"feature": "Occupation", "instances": 393, "metric_value": 0.3429, "depth": 8}
								if obj[4]<=7.735368956743002:
									# {"feature": "Direction_same", "instances": 231, "metric_value": 0.3713, "depth": 9}
									if obj[8]<=0:
										# {"feature": "Distance", "instances": 199, "metric_value": 0.3658, "depth": 10}
										if obj[9]<=2:
											return 'False'
										elif obj[9]>2:
											return 'False'
										else: return 'False'
									elif obj[8]>0:
										# {"feature": "Distance", "instances": 32, "metric_value": 0.388, "depth": 10}
										if obj[9]>1:
											return 'False'
										elif obj[9]<=1:
											return 'False'
										else: return 'False'
									else: return 'False'
								elif obj[4]>7.735368956743002:
									# {"feature": "Distance", "instances": 162, "metric_value": 0.3007, "depth": 9}
									if obj[9]<=2:
										# {"feature": "Direction_same", "instances": 122, "metric_value": 0.2849, "depth": 10}
										if obj[8]<=0:
											return 'False'
										elif obj[8]>0:
											return 'False'
										else: return 'False'
									elif obj[9]>2:
										# {"feature": "Direction_same", "instances": 40, "metric_value": 0.3487, "depth": 10}
										if obj[8]<=0:
											return 'False'
										else: return 'False'
									else: return 'False'
								else: return 'False'
							elif obj[7]>1.0:
								# {"feature": "Occupation", "instances": 155, "metric_value": 0.4101, "depth": 8}
								if obj[4]>2:
									# {"feature": "Direction_same", "instances": 118, "metric_value": 0.4436, "depth": 9}
									if obj[8]<=0:
										# {"feature": "Distance", "instances": 101, "metric_value": 0.4579, "depth": 10}
										if obj[9]>1:
											return 'False'
										elif obj[9]<=1:
											return 'False'
										else: return 'False'
									elif obj[8]>0:
										# {"feature": "Distance", "instances": 17, "metric_value": 0.2773, "depth": 10}
										if obj[9]>1:
											return 'False'
										elif obj[9]<=1:
											return 'False'
										else: return 'False'
									else: return 'False'
								elif obj[4]<=2:
									# {"feature": "Distance", "instances": 37, "metric_value": 0.2593, "depth": 9}
									if obj[9]>1:
										# {"feature": "Direction_same", "instances": 22, "metric_value": 0.3337, "depth": 10}
										if obj[8]<=0:
											return 'False'
										elif obj[8]>0:
											return 'False'
										else: return 'False'
									elif obj[9]<=1:
										# {"feature": "Direction_same", "instances": 15, "metric_value": 0.1222, "depth": 10}
										if obj[8]<=0:
											return 'False'
										elif obj[8]>0:
											return 'False'
										else: return 'False'
									else: return 'False'
								else: return 'False'
							else: return 'False'
						elif obj[6]>3.0:
							# {"feature": "Occupation", "instances": 36, "metric_value": 0.0955, "depth": 7}
							if obj[4]<=9:
								# {"feature": "Restaurant20to50", "instances": 32, "metric_value": 0.0595, "depth": 8}
								if obj[7]<=1.0:
									# {"feature": "Distance", "instances": 21, "metric_value": 0.0889, "depth": 9}
									if obj[9]<=2:
										# {"feature": "Direction_same", "instances": 15, "metric_value": 0.1231, "depth": 10}
										if obj[8]<=0:
											return 'False'
										elif obj[8]>0:
											return 'False'
										else: return 'False'
									elif obj[9]>2:
										return 'False'
									else: return 'False'
								elif obj[7]>1.0:
									return 'False'
								else: return 'False'
							elif obj[4]>9:
								# {"feature": "Distance", "instances": 4, "metric_value": 0.25, "depth": 8}
								if obj[9]<=1:
									# {"feature": "Restaurant20to50", "instances": 2, "metric_value": 0.5, "depth": 9}
									if obj[7]<=2.0:
										# {"feature": "Direction_same", "instances": 2, "metric_value": 0.5, "depth": 10}
										if obj[8]<=0:
											return 'False'
										else: return 'False'
									else: return 'False'
								elif obj[9]>1:
									return 'False'
								else: return 'False'
							else: return 'False'
						else: return 'False'
					elif obj[1]<=0:
						# {"feature": "Coffeehouse", "instances": 291, "metric_value": 0.4584, "depth": 6}
						if obj[6]<=2.0:
							# {"feature": "Occupation", "instances": 235, "metric_value": 0.4724, "depth": 7}
							if obj[4]<=13.79717461950581:
								# {"feature": "Restaurant20to50", "instances": 198, "metric_value": 0.4822, "depth": 8}
								if obj[7]>0.0:
									# {"feature": "Distance", "instances": 150, "metric_value": 0.4925, "depth": 9}
									if obj[9]<=2:
										# {"feature": "Direction_same", "instances": 131, "metric_value": 0.4965, "depth": 10}
										if obj[8]<=0:
											return 'False'
										elif obj[8]>0:
											return 'False'
										else: return 'False'
									elif obj[9]>2:
										# {"feature": "Direction_same", "instances": 19, "metric_value": 0.4654, "depth": 10}
										if obj[8]<=0:
											return 'False'
										else: return 'False'
									else: return 'False'
								elif obj[7]<=0.0:
									# {"feature": "Distance", "instances": 48, "metric_value": 0.4427, "depth": 9}
									if obj[9]>1:
										# {"feature": "Direction_same", "instances": 32, "metric_value": 0.4167, "depth": 10}
										if obj[8]<=0:
											return 'False'
										elif obj[8]>0:
											return 'False'
										else: return 'False'
									elif obj[9]<=1:
										# {"feature": "Direction_same", "instances": 16, "metric_value": 0.4167, "depth": 10}
										if obj[8]>0:
											return 'False'
										elif obj[8]<=0:
											return 'True'
										else: return 'True'
									else: return 'False'
								else: return 'False'
							elif obj[4]>13.79717461950581:
								# {"feature": "Restaurant20to50", "instances": 37, "metric_value": 0.3605, "depth": 8}
								if obj[7]<=1.0:
									# {"feature": "Distance", "instances": 32, "metric_value": 0.3406, "depth": 9}
									if obj[9]>1:
										# {"feature": "Direction_same", "instances": 20, "metric_value": 0.3158, "depth": 10}
										if obj[8]<=0:
											return 'False'
										elif obj[8]>0:
											return 'False'
										else: return 'False'
									elif obj[9]<=1:
										# {"feature": "Direction_same", "instances": 12, "metric_value": 0.375, "depth": 10}
										if obj[8]<=1:
											return 'False'
										else: return 'False'
									else: return 'False'
								elif obj[7]>1.0:
									# {"feature": "Direction_same", "instances": 5, "metric_value": 0.2667, "depth": 9}
									if obj[8]>0:
										# {"feature": "Distance", "instances": 3, "metric_value": 0.4444, "depth": 10}
										if obj[9]<=1:
											return 'False'
										else: return 'False'
									elif obj[8]<=0:
										return 'True'
									else: return 'True'
								else: return 'True'
							else: return 'False'
						elif obj[6]>2.0:
							# {"feature": "Direction_same", "instances": 56, "metric_value": 0.3174, "depth": 7}
							if obj[8]>0:
								# {"feature": "Restaurant20to50", "instances": 29, "metric_value": 0.4606, "depth": 8}
								if obj[7]>-1.0:
									# {"feature": "Occupation", "instances": 28, "metric_value": 0.4584, "depth": 9}
									if obj[4]>5:
										# {"feature": "Distance", "instances": 17, "metric_value": 0.4706, "depth": 10}
										if obj[9]<=1:
											return 'False'
										elif obj[9]>1:
											return 'False'
										else: return 'False'
									elif obj[4]<=5:
										# {"feature": "Distance", "instances": 11, "metric_value": 0.3939, "depth": 10}
										if obj[9]<=1:
											return 'False'
										elif obj[9]>1:
											return 'False'
										else: return 'False'
									else: return 'False'
								elif obj[7]<=-1.0:
									return 'True'
								else: return 'True'
							elif obj[8]<=0:
								# {"feature": "Occupation", "instances": 27, "metric_value": 0.1204, "depth": 8}
								if obj[4]<=11:
									# {"feature": "Restaurant20to50", "instances": 24, "metric_value": 0.0784, "depth": 9}
									if obj[7]<=1.0:
										# {"feature": "Distance", "instances": 17, "metric_value": 0.1092, "depth": 10}
										if obj[9]<=2:
											return 'False'
										elif obj[9]>2:
											return 'False'
										else: return 'False'
									elif obj[7]>1.0:
										return 'False'
									else: return 'False'
								elif obj[4]>11:
									# {"feature": "Restaurant20to50", "instances": 3, "metric_value": 0.3333, "depth": 9}
									if obj[7]>1.0:
										# {"feature": "Distance", "instances": 2, "metric_value": 0.0, "depth": 10}
										if obj[9]<=2:
											return 'True'
										elif obj[9]>2:
											return 'False'
										else: return 'False'
									elif obj[7]<=1.0:
										return 'False'
									else: return 'False'
								else: return 'False'
							else: return 'False'
						else: return 'False'
					else: return 'False'
				elif obj[3]<=0:
					# {"feature": "Occupation", "instances": 488, "metric_value": 0.4614, "depth": 5}
					if obj[4]>1.348010951701891:
						# {"feature": "Coffeehouse", "instances": 406, "metric_value": 0.4828, "depth": 6}
						if obj[6]<=3.0:
							# {"feature": "Restaurant20to50", "instances": 359, "metric_value": 0.4908, "depth": 7}
							if obj[7]<=2.0:
								# {"feature": "Time", "instances": 338, "metric_value": 0.4892, "depth": 8}
								if obj[1]<=2:
									# {"feature": "Distance", "instances": 224, "metric_value": 0.4909, "depth": 9}
									if obj[9]<=2:
										# {"feature": "Direction_same", "instances": 167, "metric_value": 0.4905, "depth": 10}
										if obj[8]<=0:
											return 'True'
										elif obj[8]>0:
											return 'False'
										else: return 'False'
									elif obj[9]>2:
										# {"feature": "Direction_same", "instances": 57, "metric_value": 0.4654, "depth": 10}
										if obj[8]<=0:
											return 'False'
										else: return 'False'
									else: return 'False'
								elif obj[1]>2:
									# {"feature": "Direction_same", "instances": 114, "metric_value": 0.4653, "depth": 9}
									if obj[8]<=0:
										# {"feature": "Distance", "instances": 109, "metric_value": 0.4641, "depth": 10}
										if obj[9]<=2:
											return 'False'
										elif obj[9]>2:
											return 'False'
										else: return 'False'
									elif obj[8]>0:
										# {"feature": "Distance", "instances": 5, "metric_value": 0.48, "depth": 10}
										if obj[9]<=2:
											return 'True'
										else: return 'True'
									else: return 'True'
								else: return 'False'
							elif obj[7]>2.0:
								# {"feature": "Direction_same", "instances": 21, "metric_value": 0.4222, "depth": 8}
								if obj[8]<=0:
									# {"feature": "Time", "instances": 15, "metric_value": 0.3744, "depth": 9}
									if obj[1]>0:
										# {"feature": "Distance", "instances": 13, "metric_value": 0.3538, "depth": 10}
										if obj[9]<=2:
											return 'True'
										elif obj[9]>2:
											return 'True'
										else: return 'True'
									elif obj[1]<=0:
										# {"feature": "Distance", "instances": 2, "metric_value": 0.0, "depth": 10}
										if obj[9]<=2:
											return 'True'
										elif obj[9]>2:
											return 'False'
										else: return 'False'
									else: return 'True'
								elif obj[8]>0:
									# {"feature": "Time", "instances": 6, "metric_value": 0.25, "depth": 9}
									if obj[1]<=0:
										# {"feature": "Distance", "instances": 4, "metric_value": 0.3333, "depth": 10}
										if obj[9]<=1:
											return 'True'
										elif obj[9]>1:
											return 'True'
										else: return 'True'
									elif obj[1]>0:
										return 'False'
									else: return 'False'
								else: return 'False'
							else: return 'True'
						elif obj[6]>3.0:
							# {"feature": "Distance", "instances": 47, "metric_value": 0.343, "depth": 7}
							if obj[9]>1:
								# {"feature": "Time", "instances": 28, "metric_value": 0.2286, "depth": 8}
								if obj[1]>0:
									# {"feature": "Direction_same", "instances": 20, "metric_value": 0.3, "depth": 9}
									if obj[8]<=0:
										# {"feature": "Restaurant20to50", "instances": 16, "metric_value": 0.3667, "depth": 10}
										if obj[7]<=2.0:
											return 'False'
										elif obj[7]>2.0:
											return 'False'
										else: return 'False'
									elif obj[8]>0:
										return 'False'
									else: return 'False'
								elif obj[1]<=0:
									return 'False'
								else: return 'False'
							elif obj[9]<=1:
								# {"feature": "Restaurant20to50", "instances": 19, "metric_value": 0.427, "depth": 8}
								if obj[7]<=1.0:
									# {"feature": "Time", "instances": 11, "metric_value": 0.3636, "depth": 9}
									if obj[1]>0:
										# {"feature": "Direction_same", "instances": 9, "metric_value": 0.3333, "depth": 10}
										if obj[8]<=0:
											return 'False'
										elif obj[8]>0:
											return 'True'
										else: return 'True'
									elif obj[1]<=0:
										return 'False'
									else: return 'False'
								elif obj[7]>1.0:
									# {"feature": "Time", "instances": 8, "metric_value": 0.3571, "depth": 9}
									if obj[1]<=2:
										# {"feature": "Direction_same", "instances": 7, "metric_value": 0.4048, "depth": 10}
										if obj[8]<=0:
											return 'True'
										elif obj[8]>0:
											return 'True'
										else: return 'True'
									elif obj[1]>2:
										return 'False'
									else: return 'False'
								else: return 'True'
							else: return 'False'
						else: return 'False'
					elif obj[4]<=1.348010951701891:
						# {"feature": "Coffeehouse", "instances": 82, "metric_value": 0.2475, "depth": 6}
						if obj[6]<=2.0:
							# {"feature": "Restaurant20to50", "instances": 74, "metric_value": 0.194, "depth": 7}
							if obj[7]<=1.0:
								# {"feature": "Time", "instances": 67, "metric_value": 0.1615, "depth": 8}
								if obj[1]<=3:
									# {"feature": "Distance", "instances": 61, "metric_value": 0.1758, "depth": 9}
									if obj[9]<=2:
										# {"feature": "Direction_same", "instances": 43, "metric_value": 0.2021, "depth": 10}
										if obj[8]<=0:
											return 'False'
										elif obj[8]>0:
											return 'False'
										else: return 'False'
									elif obj[9]>2:
										# {"feature": "Direction_same", "instances": 18, "metric_value": 0.1049, "depth": 10}
										if obj[8]<=0:
											return 'False'
										else: return 'False'
									else: return 'False'
								elif obj[1]>3:
									return 'False'
								else: return 'False'
							elif obj[7]>1.0:
								# {"feature": "Distance", "instances": 7, "metric_value": 0.2143, "depth": 8}
								if obj[9]>1:
									# {"feature": "Time", "instances": 4, "metric_value": 0.3333, "depth": 9}
									if obj[1]>0:
										# {"feature": "Direction_same", "instances": 3, "metric_value": 0.4444, "depth": 10}
										if obj[8]<=0:
											return 'False'
										else: return 'False'
									elif obj[1]<=0:
										return 'False'
									else: return 'False'
								elif obj[9]<=1:
									return 'True'
								else: return 'True'
							else: return 'True'
						elif obj[6]>2.0:
							# {"feature": "Time", "instances": 8, "metric_value": 0.1667, "depth": 7}
							if obj[1]<=1:
								return 'True'
							elif obj[1]>1:
								# {"feature": "Restaurant20to50", "instances": 3, "metric_value": 0.0, "depth": 8}
								if obj[7]>1.0:
									return 'False'
								elif obj[7]<=1.0:
									return 'True'
								else: return 'True'
							else: return 'False'
						else: return 'True'
					else: return 'False'
				else: return 'False'
			elif obj[0]>2:
				# {"feature": "Restaurant20to50", "instances": 219, "metric_value": 0.4866, "depth": 4}
				if obj[7]<=1.0:
					# {"feature": "Education", "instances": 160, "metric_value": 0.4718, "depth": 5}
					if obj[3]<=2:
						# {"feature": "Occupation", "instances": 126, "metric_value": 0.453, "depth": 6}
						if obj[4]>0:
							# {"feature": "Time", "instances": 123, "metric_value": 0.4573, "depth": 7}
							if obj[1]>0:
								# {"feature": "Coffeehouse", "instances": 120, "metric_value": 0.4631, "depth": 8}
								if obj[6]<=1.0:
									# {"feature": "Distance", "instances": 80, "metric_value": 0.4619, "depth": 9}
									if obj[9]>1:
										# {"feature": "Direction_same", "instances": 68, "metric_value": 0.465, "depth": 10}
										if obj[8]<=0:
											return 'False'
										else: return 'False'
									elif obj[9]<=1:
										# {"feature": "Direction_same", "instances": 12, "metric_value": 0.4444, "depth": 10}
										if obj[8]<=0:
											return 'True'
										else: return 'True'
									else: return 'True'
								elif obj[6]>1.0:
									# {"feature": "Distance", "instances": 40, "metric_value": 0.4165, "depth": 9}
									if obj[9]>1:
										# {"feature": "Direction_same", "instances": 31, "metric_value": 0.437, "depth": 10}
										if obj[8]<=0:
											return 'False'
										else: return 'False'
									elif obj[9]<=1:
										# {"feature": "Direction_same", "instances": 9, "metric_value": 0.3457, "depth": 10}
										if obj[8]<=0:
											return 'False'
										else: return 'False'
									else: return 'False'
								else: return 'False'
							elif obj[1]<=0:
								return 'False'
							else: return 'False'
						elif obj[4]<=0:
							return 'True'
						else: return 'True'
					elif obj[3]>2:
						# {"feature": "Coffeehouse", "instances": 34, "metric_value": 0.4141, "depth": 6}
						if obj[6]<=2.0:
							# {"feature": "Time", "instances": 25, "metric_value": 0.319, "depth": 7}
							if obj[1]<=3:
								# {"feature": "Occupation", "instances": 21, "metric_value": 0.2857, "depth": 8}
								if obj[4]<=11:
									# {"feature": "Direction_same", "instances": 16, "metric_value": 0.375, "depth": 9}
									if obj[8]<=0:
										# {"feature": "Distance", "instances": 16, "metric_value": 0.375, "depth": 10}
										if obj[9]<=2:
											return 'True'
										else: return 'True'
									else: return 'True'
								elif obj[4]>11:
									return 'True'
								else: return 'True'
							elif obj[1]>3:
								# {"feature": "Occupation", "instances": 4, "metric_value": 0.25, "depth": 8}
								if obj[4]<=6:
									return 'False'
								elif obj[4]>6:
									# {"feature": "Direction_same", "instances": 2, "metric_value": 0.5, "depth": 9}
									if obj[8]<=0:
										# {"feature": "Distance", "instances": 2, "metric_value": 0.5, "depth": 10}
										if obj[9]<=1:
											return 'False'
										else: return 'False'
									else: return 'False'
								else: return 'False'
							else: return 'False'
						elif obj[6]>2.0:
							# {"feature": "Time", "instances": 9, "metric_value": 0.3333, "depth": 7}
							if obj[1]<=3:
								# {"feature": "Occupation", "instances": 8, "metric_value": 0.3333, "depth": 8}
								if obj[4]>5:
									# {"feature": "Direction_same", "instances": 6, "metric_value": 0.4444, "depth": 9}
									if obj[8]<=0:
										# {"feature": "Distance", "instances": 6, "metric_value": 0.4444, "depth": 10}
										if obj[9]<=2:
											return 'False'
										else: return 'False'
									else: return 'False'
								elif obj[4]<=5:
									return 'False'
								else: return 'False'
							elif obj[1]>3:
								return 'True'
							else: return 'True'
						else: return 'False'
					else: return 'True'
				elif obj[7]>1.0:
					# {"feature": "Education", "instances": 59, "metric_value": 0.4309, "depth": 5}
					if obj[3]>0:
						# {"feature": "Coffeehouse", "instances": 44, "metric_value": 0.4723, "depth": 6}
						if obj[6]<=2.0:
							# {"feature": "Time", "instances": 39, "metric_value": 0.4712, "depth": 7}
							if obj[1]<=3:
								# {"feature": "Occupation", "instances": 37, "metric_value": 0.4725, "depth": 8}
								if obj[4]<=9:
									# {"feature": "Direction_same", "instances": 29, "metric_value": 0.4994, "depth": 9}
									if obj[8]<=0:
										# {"feature": "Distance", "instances": 29, "metric_value": 0.4994, "depth": 10}
										if obj[9]<=2:
											return 'False'
										else: return 'False'
									else: return 'False'
								elif obj[4]>9:
									# {"feature": "Direction_same", "instances": 8, "metric_value": 0.375, "depth": 9}
									if obj[8]<=0:
										# {"feature": "Distance", "instances": 8, "metric_value": 0.375, "depth": 10}
										if obj[9]<=2:
											return 'True'
										else: return 'True'
									else: return 'True'
								else: return 'True'
							elif obj[1]>3:
								return 'True'
							else: return 'True'
						elif obj[6]>2.0:
							# {"feature": "Time", "instances": 5, "metric_value": 0.2, "depth": 7}
							if obj[1]>2:
								return 'False'
							elif obj[1]<=2:
								# {"feature": "Occupation", "instances": 2, "metric_value": 0.5, "depth": 8}
								if obj[4]<=9:
									# {"feature": "Direction_same", "instances": 2, "metric_value": 0.5, "depth": 9}
									if obj[8]<=0:
										# {"feature": "Distance", "instances": 2, "metric_value": 0.5, "depth": 10}
										if obj[9]<=2:
											return 'True'
										else: return 'True'
									else: return 'True'
								else: return 'True'
							else: return 'True'
						else: return 'False'
					elif obj[3]<=0:
						# {"feature": "Occupation", "instances": 15, "metric_value": 0.1238, "depth": 6}
						if obj[4]>3:
							# {"feature": "Coffeehouse", "instances": 14, "metric_value": 0.0952, "depth": 7}
							if obj[6]>0.0:
								return 'True'
							elif obj[6]<=0.0:
								# {"feature": "Time", "instances": 3, "metric_value": 0.3333, "depth": 8}
								if obj[1]>2:
									# {"feature": "Direction_same", "instances": 2, "metric_value": 0.5, "depth": 9}
									if obj[8]<=0:
										# {"feature": "Distance", "instances": 2, "metric_value": 0.5, "depth": 10}
										if obj[9]<=2:
											return 'False'
										else: return 'False'
									else: return 'False'
								elif obj[1]<=2:
									return 'True'
								else: return 'True'
							else: return 'True'
						elif obj[4]<=3:
							return 'False'
						else: return 'False'
					else: return 'True'
				else: return 'True'
			else: return 'False'
		elif obj[5]>1.0:
			# {"feature": "Restaurant20to50", "instances": 662, "metric_value": 0.4594, "depth": 3}
			if obj[7]<=1.0:
				# {"feature": "Passanger", "instances": 355, "metric_value": 0.4904, "depth": 4}
				if obj[0]<=2:
					# {"feature": "Time", "instances": 290, "metric_value": 0.4838, "depth": 5}
					if obj[1]<=2:
						# {"feature": "Occupation", "instances": 202, "metric_value": 0.4801, "depth": 6}
						if obj[4]<=13.60630442015693:
							# {"feature": "Direction_same", "instances": 170, "metric_value": 0.4796, "depth": 7}
							if obj[8]<=0:
								# {"feature": "Distance", "instances": 116, "metric_value": 0.4833, "depth": 8}
								if obj[9]<=2:
									# {"feature": "Coffeehouse", "instances": 71, "metric_value": 0.4642, "depth": 9}
									if obj[6]<=2.0:
										# {"feature": "Education", "instances": 41, "metric_value": 0.4564, "depth": 10}
										if obj[3]<=2:
											return 'True'
										elif obj[3]>2:
											return 'True'
										else: return 'True'
									elif obj[6]>2.0:
										# {"feature": "Education", "instances": 30, "metric_value": 0.4368, "depth": 10}
										if obj[3]<=3:
											return 'False'
										elif obj[3]>3:
											return 'True'
										else: return 'True'
									else: return 'False'
								elif obj[9]>2:
									# {"feature": "Coffeehouse", "instances": 45, "metric_value": 0.3748, "depth": 9}
									if obj[6]<=2.0:
										# {"feature": "Education", "instances": 30, "metric_value": 0.4785, "depth": 10}
										if obj[3]<=1:
											return 'True'
										elif obj[3]>1:
											return 'False'
										else: return 'False'
									elif obj[6]>2.0:
										# {"feature": "Education", "instances": 15, "metric_value": 0.1212, "depth": 10}
										if obj[3]>0:
											return 'True'
										elif obj[3]<=0:
											return 'True'
										else: return 'True'
									else: return 'True'
								else: return 'True'
							elif obj[8]>0:
								# {"feature": "Coffeehouse", "instances": 54, "metric_value": 0.4384, "depth": 8}
								if obj[6]>0.0:
									# {"feature": "Education", "instances": 39, "metric_value": 0.4575, "depth": 9}
									if obj[3]<=2:
										# {"feature": "Distance", "instances": 35, "metric_value": 0.4667, "depth": 10}
										if obj[9]<=1:
											return 'True'
										elif obj[9]>1:
											return 'True'
										else: return 'True'
									elif obj[3]>2:
										# {"feature": "Distance", "instances": 4, "metric_value": 0.3333, "depth": 10}
										if obj[9]<=1:
											return 'False'
										elif obj[9]>1:
											return 'False'
										else: return 'False'
									else: return 'False'
								elif obj[6]<=0.0:
									# {"feature": "Education", "instances": 15, "metric_value": 0.3071, "depth": 9}
									if obj[3]>0:
										# {"feature": "Distance", "instances": 8, "metric_value": 0.2188, "depth": 10}
										if obj[9]<=1:
											return 'True'
										else: return 'True'
									elif obj[3]<=0:
										# {"feature": "Distance", "instances": 7, "metric_value": 0.381, "depth": 10}
										if obj[9]<=1:
											return 'True'
										elif obj[9]>1:
											return 'True'
										else: return 'True'
									else: return 'True'
								else: return 'True'
							else: return 'True'
						elif obj[4]>13.60630442015693:
							# {"feature": "Distance", "instances": 32, "metric_value": 0.4383, "depth": 7}
							if obj[9]<=2:
								# {"feature": "Direction_same", "instances": 21, "metric_value": 0.3516, "depth": 8}
								if obj[8]<=0:
									# {"feature": "Education", "instances": 13, "metric_value": 0.2198, "depth": 9}
									if obj[3]>0:
										# {"feature": "Coffeehouse", "instances": 7, "metric_value": 0.381, "depth": 10}
										if obj[6]>0.0:
											return 'False'
										elif obj[6]<=0.0:
											return 'False'
										else: return 'False'
									elif obj[3]<=0:
										return 'False'
									else: return 'False'
								elif obj[8]>0:
									# {"feature": "Education", "instances": 8, "metric_value": 0.3333, "depth": 9}
									if obj[3]<=0:
										# {"feature": "Coffeehouse", "instances": 6, "metric_value": 0.4444, "depth": 10}
										if obj[6]>1.0:
											return 'True'
										elif obj[6]<=1.0:
											return 'True'
										else: return 'True'
									elif obj[3]>0:
										return 'False'
									else: return 'False'
								else: return 'False'
							elif obj[9]>2:
								# {"feature": "Coffeehouse", "instances": 11, "metric_value": 0.4364, "depth": 8}
								if obj[6]<=3.0:
									# {"feature": "Education", "instances": 10, "metric_value": 0.45, "depth": 9}
									if obj[3]<=1:
										# {"feature": "Direction_same", "instances": 6, "metric_value": 0.5, "depth": 10}
										if obj[8]<=0:
											return 'False'
										else: return 'False'
									elif obj[3]>1:
										# {"feature": "Direction_same", "instances": 4, "metric_value": 0.375, "depth": 10}
										if obj[8]<=0:
											return 'True'
										else: return 'True'
									else: return 'True'
								elif obj[6]>3.0:
									return 'False'
								else: return 'False'
							else: return 'True'
						else: return 'False'
					elif obj[1]>2:
						# {"feature": "Distance", "instances": 88, "metric_value": 0.4535, "depth": 6}
						if obj[9]<=2:
							# {"feature": "Coffeehouse", "instances": 85, "metric_value": 0.4627, "depth": 7}
							if obj[6]>-1.0:
								# {"feature": "Occupation", "instances": 83, "metric_value": 0.4673, "depth": 8}
								if obj[4]>1:
									# {"feature": "Education", "instances": 74, "metric_value": 0.4754, "depth": 9}
									if obj[3]<=2:
										# {"feature": "Direction_same", "instances": 60, "metric_value": 0.4667, "depth": 10}
										if obj[8]<=0:
											return 'False'
										elif obj[8]>0:
											return 'True'
										else: return 'True'
									elif obj[3]>2:
										# {"feature": "Direction_same", "instances": 14, "metric_value": 0.381, "depth": 10}
										if obj[8]<=0:
											return 'False'
										elif obj[8]>0:
											return 'False'
										else: return 'False'
									else: return 'False'
								elif obj[4]<=1:
									# {"feature": "Education", "instances": 9, "metric_value": 0.3333, "depth": 9}
									if obj[3]<=0:
										# {"feature": "Direction_same", "instances": 8, "metric_value": 0.375, "depth": 10}
										if obj[8]<=0:
											return 'False'
										else: return 'False'
									elif obj[3]>0:
										return 'False'
									else: return 'False'
								else: return 'False'
							elif obj[6]<=-1.0:
								return 'False'
							else: return 'False'
						elif obj[9]>2:
							return 'False'
						else: return 'False'
					else: return 'False'
				elif obj[0]>2:
					# {"feature": "Time", "instances": 65, "metric_value": 0.4117, "depth": 5}
					if obj[1]>2:
						# {"feature": "Coffeehouse", "instances": 47, "metric_value": 0.3469, "depth": 6}
						if obj[6]<=2.0:
							# {"feature": "Occupation", "instances": 32, "metric_value": 0.4193, "depth": 7}
							if obj[4]>2:
								# {"feature": "Education", "instances": 24, "metric_value": 0.4242, "depth": 8}
								if obj[3]<=2:
									# {"feature": "Distance", "instances": 22, "metric_value": 0.4299, "depth": 9}
									if obj[9]>1:
										# {"feature": "Direction_same", "instances": 17, "metric_value": 0.4152, "depth": 10}
										if obj[8]<=0:
											return 'True'
										else: return 'True'
									elif obj[9]<=1:
										# {"feature": "Direction_same", "instances": 5, "metric_value": 0.48, "depth": 10}
										if obj[8]<=0:
											return 'False'
										else: return 'False'
									else: return 'False'
								elif obj[3]>2:
									return 'False'
								else: return 'False'
							elif obj[4]<=2:
								# {"feature": "Education", "instances": 8, "metric_value": 0.2083, "depth": 8}
								if obj[3]>0:
									# {"feature": "Distance", "instances": 6, "metric_value": 0.2667, "depth": 9}
									if obj[9]>1:
										# {"feature": "Direction_same", "instances": 5, "metric_value": 0.32, "depth": 10}
										if obj[8]<=0:
											return 'True'
										else: return 'True'
									elif obj[9]<=1:
										return 'True'
									else: return 'True'
								elif obj[3]<=0:
									return 'True'
								else: return 'True'
							else: return 'True'
						elif obj[6]>2.0:
							# {"feature": "Occupation", "instances": 15, "metric_value": 0.0667, "depth": 7}
							if obj[4]>2:
								return 'True'
							elif obj[4]<=2:
								# {"feature": "Education", "instances": 2, "metric_value": 0.0, "depth": 8}
								if obj[3]>0:
									return 'False'
								elif obj[3]<=0:
									return 'True'
								else: return 'True'
							else: return 'False'
						else: return 'True'
					elif obj[1]<=2:
						# {"feature": "Occupation", "instances": 18, "metric_value": 0.2564, "depth": 6}
						if obj[4]<=10:
							# {"feature": "Coffeehouse", "instances": 13, "metric_value": 0.3077, "depth": 7}
							if obj[6]>1.0:
								# {"feature": "Education", "instances": 9, "metric_value": 0.381, "depth": 8}
								if obj[3]<=2:
									# {"feature": "Direction_same", "instances": 7, "metric_value": 0.4898, "depth": 9}
									if obj[8]<=0:
										# {"feature": "Distance", "instances": 7, "metric_value": 0.4898, "depth": 10}
										if obj[9]<=2:
											return 'False'
										else: return 'False'
									else: return 'False'
								elif obj[3]>2:
									return 'False'
								else: return 'False'
							elif obj[6]<=1.0:
								return 'False'
							else: return 'False'
						elif obj[4]>10:
							return 'True'
						else: return 'True'
					else: return 'False'
				else: return 'True'
			elif obj[7]>1.0:
				# {"feature": "Direction_same", "instances": 307, "metric_value": 0.4012, "depth": 4}
				if obj[8]<=0:
					# {"feature": "Education", "instances": 250, "metric_value": 0.4308, "depth": 5}
					if obj[3]>1:
						# {"feature": "Occupation", "instances": 161, "metric_value": 0.4573, "depth": 6}
						if obj[4]>1:
							# {"feature": "Time", "instances": 133, "metric_value": 0.4834, "depth": 7}
							if obj[1]>0:
								# {"feature": "Coffeehouse", "instances": 112, "metric_value": 0.4867, "depth": 8}
								if obj[6]>1.0:
									# {"feature": "Passanger", "instances": 71, "metric_value": 0.4784, "depth": 9}
									if obj[0]<=2:
										# {"feature": "Distance", "instances": 55, "metric_value": 0.4702, "depth": 10}
										if obj[9]>1:
											return 'True'
										elif obj[9]<=1:
											return 'True'
										else: return 'True'
									elif obj[0]>2:
										# {"feature": "Distance", "instances": 16, "metric_value": 0.5, "depth": 10}
										if obj[9]>1:
											return 'False'
										elif obj[9]<=1:
											return 'False'
										else: return 'False'
									else: return 'False'
								elif obj[6]<=1.0:
									# {"feature": "Passanger", "instances": 41, "metric_value": 0.4457, "depth": 9}
									if obj[0]<=2:
										# {"feature": "Distance", "instances": 33, "metric_value": 0.4354, "depth": 10}
										if obj[9]<=2:
											return 'False'
										elif obj[9]>2:
											return 'True'
										else: return 'True'
									elif obj[0]>2:
										# {"feature": "Distance", "instances": 8, "metric_value": 0.3571, "depth": 10}
										if obj[9]>1:
											return 'True'
										elif obj[9]<=1:
											return 'True'
										else: return 'True'
									else: return 'True'
								else: return 'False'
							elif obj[1]<=0:
								# {"feature": "Coffeehouse", "instances": 21, "metric_value": 0.3844, "depth": 8}
								if obj[6]<=2.0:
									# {"feature": "Distance", "instances": 11, "metric_value": 0.2909, "depth": 9}
									if obj[9]<=2:
										# {"feature": "Passanger", "instances": 10, "metric_value": 0.3167, "depth": 10}
										if obj[0]>0:
											return 'True'
										elif obj[0]<=0:
											return 'True'
										else: return 'True'
									elif obj[9]>2:
										return 'True'
									else: return 'True'
								elif obj[6]>2.0:
									# {"feature": "Passanger", "instances": 10, "metric_value": 0.4, "depth": 9}
									if obj[0]<=1:
										# {"feature": "Distance", "instances": 8, "metric_value": 0.4286, "depth": 10}
										if obj[9]<=2:
											return 'False'
										elif obj[9]>2:
											return 'True'
										else: return 'True'
									elif obj[0]>1:
										return 'True'
									else: return 'True'
								else: return 'True'
							else: return 'True'
						elif obj[4]<=1:
							# {"feature": "Passanger", "instances": 28, "metric_value": 0.2434, "depth": 7}
							if obj[0]>0:
								# {"feature": "Distance", "instances": 27, "metric_value": 0.2339, "depth": 8}
								if obj[9]<=2:
									# {"feature": "Time", "instances": 19, "metric_value": 0.2551, "depth": 9}
									if obj[1]>1:
										# {"feature": "Coffeehouse", "instances": 13, "metric_value": 0.1154, "depth": 10}
										if obj[6]<=3.0:
											return 'True'
										elif obj[6]>3.0:
											return 'True'
										else: return 'True'
									elif obj[1]<=1:
										# {"feature": "Coffeehouse", "instances": 6, "metric_value": 0.25, "depth": 10}
										if obj[6]<=2.0:
											return 'False'
										elif obj[6]>2.0:
											return 'True'
										else: return 'True'
									else: return 'True'
								elif obj[9]>2:
									return 'True'
								else: return 'True'
							elif obj[0]<=0:
								return 'False'
							else: return 'False'
						else: return 'True'
					elif obj[3]<=1:
						# {"feature": "Occupation", "instances": 89, "metric_value": 0.3213, "depth": 6}
						if obj[4]<=10:
							# {"feature": "Coffeehouse", "instances": 53, "metric_value": 0.4044, "depth": 7}
							if obj[6]>0.0:
								# {"feature": "Passanger", "instances": 46, "metric_value": 0.459, "depth": 8}
								if obj[0]<=2:
									# {"feature": "Time", "instances": 41, "metric_value": 0.4658, "depth": 9}
									if obj[1]>0:
										# {"feature": "Distance", "instances": 30, "metric_value": 0.4855, "depth": 10}
										if obj[9]<=2:
											return 'True'
										elif obj[9]>2:
											return 'True'
										else: return 'True'
									elif obj[1]<=0:
										# {"feature": "Distance", "instances": 11, "metric_value": 0.3818, "depth": 10}
										if obj[9]>1:
											return 'True'
										elif obj[9]<=1:
											return 'True'
										else: return 'True'
									else: return 'True'
								elif obj[0]>2:
									# {"feature": "Time", "instances": 5, "metric_value": 0.0, "depth": 9}
									if obj[1]>2:
										return 'True'
									elif obj[1]<=2:
										return 'False'
									else: return 'False'
								else: return 'True'
							elif obj[6]<=0.0:
								return 'True'
							else: return 'True'
						elif obj[4]>10:
							# {"feature": "Passanger", "instances": 36, "metric_value": 0.125, "depth": 7}
							if obj[0]<=1:
								return 'True'
							elif obj[0]>1:
								# {"feature": "Coffeehouse", "instances": 12, "metric_value": 0.2, "depth": 8}
								if obj[6]>1.0:
									return 'True'
								elif obj[6]<=1.0:
									# {"feature": "Distance", "instances": 5, "metric_value": 0.2667, "depth": 9}
									if obj[9]>1:
										# {"feature": "Time", "instances": 3, "metric_value": 0.4444, "depth": 10}
										if obj[1]<=3:
											return 'True'
										else: return 'True'
									elif obj[9]<=1:
										return 'False'
									else: return 'False'
								else: return 'False'
							else: return 'True'
						else: return 'True'
					else: return 'True'
				elif obj[8]>0:
					# {"feature": "Time", "instances": 57, "metric_value": 0.2047, "depth": 5}
					if obj[1]<=0:
						# {"feature": "Occupation", "instances": 40, "metric_value": 0.1279, "depth": 6}
						if obj[4]<=21:
							# {"feature": "Education", "instances": 37, "metric_value": 0.0937, "depth": 7}
							if obj[3]>1:
								return 'True'
							elif obj[3]<=1:
								# {"feature": "Coffeehouse", "instances": 15, "metric_value": 0.2133, "depth": 8}
								if obj[6]>1.0:
									# {"feature": "Passanger", "instances": 10, "metric_value": 0.32, "depth": 9}
									if obj[0]<=1:
										# {"feature": "Distance", "instances": 10, "metric_value": 0.32, "depth": 10}
										if obj[9]<=1:
											return 'True'
										else: return 'True'
									else: return 'True'
								elif obj[6]<=1.0:
									return 'True'
								else: return 'True'
							else: return 'True'
						elif obj[4]>21:
							# {"feature": "Education", "instances": 3, "metric_value": 0.0, "depth": 7}
							if obj[3]<=0:
								return 'True'
							elif obj[3]>0:
								return 'False'
							else: return 'False'
						else: return 'True'
					elif obj[1]>0:
						# {"feature": "Distance", "instances": 17, "metric_value": 0.2834, "depth": 6}
						if obj[9]>1:
							# {"feature": "Occupation", "instances": 11, "metric_value": 0.1364, "depth": 7}
							if obj[4]>7:
								return 'True'
							elif obj[4]<=7:
								# {"feature": "Education", "instances": 4, "metric_value": 0.3333, "depth": 8}
								if obj[3]>0:
									# {"feature": "Coffeehouse", "instances": 3, "metric_value": 0.3333, "depth": 9}
									if obj[6]>2.0:
										# {"feature": "Passanger", "instances": 2, "metric_value": 0.5, "depth": 10}
										if obj[0]<=1:
											return 'True'
										else: return 'True'
									elif obj[6]<=2.0:
										return 'True'
									else: return 'True'
								elif obj[3]<=0:
									return 'True'
								else: return 'True'
							else: return 'True'
						elif obj[9]<=1:
							# {"feature": "Education", "instances": 6, "metric_value": 0.25, "depth": 7}
							if obj[3]<=2:
								# {"feature": "Occupation", "instances": 4, "metric_value": 0.25, "depth": 8}
								if obj[4]>5:
									return 'True'
								elif obj[4]<=5:
									# {"feature": "Passanger", "instances": 2, "metric_value": 0.5, "depth": 9}
									if obj[0]<=1:
										# {"feature": "Coffeehouse", "instances": 2, "metric_value": 0.5, "depth": 10}
										if obj[6]<=2.0:
											return 'False'
										else: return 'False'
									else: return 'False'
								else: return 'False'
							elif obj[3]>2:
								return 'False'
							else: return 'False'
						else: return 'True'
					else: return 'True'
				else: return 'True'
			else: return 'True'
		else: return 'True'
	else: return 'False'
