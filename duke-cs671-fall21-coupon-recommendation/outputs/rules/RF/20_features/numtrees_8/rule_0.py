def findDecision(obj): #obj[0]: Driving_to, obj[1]: Passanger, obj[2]: Weather, obj[3]: Temperature, obj[4]: Time, obj[5]: Coupon, obj[6]: Coupon_validity, obj[7]: Gender, obj[8]: Age, obj[9]: Maritalstatus, obj[10]: Children, obj[11]: Education, obj[12]: Occupation, obj[13]: Income, obj[14]: Bar, obj[15]: Coffeehouse, obj[16]: Restaurantlessthan20, obj[17]: Restaurant20to50, obj[18]: Direction_same, obj[19]: Distance
	# {"feature": "Distance", "instances": 127, "metric_value": 0.9566, "depth": 1}
	if obj[19]<=2:
		# {"feature": "Education", "instances": 111, "metric_value": 0.9183, "depth": 2}
		if obj[11]>1:
			# {"feature": "Bar", "instances": 65, "metric_value": 0.9861, "depth": 3}
			if obj[14]<=1.0:
				# {"feature": "Coupon", "instances": 42, "metric_value": 0.9183, "depth": 4}
				if obj[5]>0:
					# {"feature": "Age", "instances": 40, "metric_value": 0.8813, "depth": 5}
					if obj[8]>0:
						# {"feature": "Income", "instances": 33, "metric_value": 0.9457, "depth": 6}
						if obj[13]<=4:
							# {"feature": "Coffeehouse", "instances": 18, "metric_value": 0.7642, "depth": 7}
							if obj[15]<=2.0:
								# {"feature": "Weather", "instances": 15, "metric_value": 0.5665, "depth": 8}
								if obj[2]<=0:
									# {"feature": "Occupation", "instances": 14, "metric_value": 0.3712, "depth": 9}
									if obj[12]>2:
										return 'True'
									elif obj[12]<=2:
										# {"feature": "Restaurantlessthan20", "instances": 3, "metric_value": 0.9183, "depth": 10}
										if obj[16]>1.0:
											return 'True'
										elif obj[16]<=1.0:
											return 'False'
										else: return 'False'
									else: return 'True'
								elif obj[2]>0:
									return 'False'
								else: return 'False'
							elif obj[15]>2.0:
								# {"feature": "Time", "instances": 3, "metric_value": 0.9183, "depth": 8}
								if obj[4]>0:
									return 'False'
								elif obj[4]<=0:
									return 'True'
								else: return 'True'
							else: return 'False'
						elif obj[13]>4:
							# {"feature": "Children", "instances": 15, "metric_value": 0.9968, "depth": 7}
							if obj[10]>0:
								# {"feature": "Occupation", "instances": 8, "metric_value": 0.8113, "depth": 8}
								if obj[12]>4:
									return 'True'
								elif obj[12]<=4:
									# {"feature": "Driving_to", "instances": 3, "metric_value": 0.9183, "depth": 9}
									if obj[0]<=0:
										# {"feature": "Passanger", "instances": 2, "metric_value": 1.0, "depth": 10}
										if obj[1]<=2:
											# {"feature": "Weather", "instances": 2, "metric_value": 1.0, "depth": 11}
											if obj[2]<=0:
												# {"feature": "Temperature", "instances": 2, "metric_value": 1.0, "depth": 12}
												if obj[3]<=80:
													# {"feature": "Time", "instances": 2, "metric_value": 1.0, "depth": 13}
													if obj[4]<=4:
														# {"feature": "Coupon_validity", "instances": 2, "metric_value": 1.0, "depth": 14}
														if obj[6]<=1:
															# {"feature": "Gender", "instances": 2, "metric_value": 1.0, "depth": 15}
															if obj[7]<=0:
																# {"feature": "Maritalstatus", "instances": 2, "metric_value": 1.0, "depth": 16}
																if obj[9]<=0:
																	# {"feature": "Coffeehouse", "instances": 2, "metric_value": 1.0, "depth": 17}
																	if obj[15]<=2.0:
																		# {"feature": "Restaurantlessthan20", "instances": 2, "metric_value": 1.0, "depth": 18}
																		if obj[16]<=2.0:
																			# {"feature": "Restaurant20to50", "instances": 2, "metric_value": 1.0, "depth": 19}
																			if obj[17]<=1.0:
																				# {"feature": "Direction_same", "instances": 2, "metric_value": 1.0, "depth": 20}
																				if obj[18]<=0:
																					return 'False'
																				else: return 'False'
																			else: return 'False'
																		else: return 'False'
																	else: return 'False'
																else: return 'False'
															else: return 'False'
														else: return 'False'
													else: return 'False'
												else: return 'False'
											else: return 'False'
										else: return 'False'
									elif obj[0]>0:
										return 'False'
									else: return 'False'
								else: return 'False'
							elif obj[10]<=0:
								# {"feature": "Weather", "instances": 7, "metric_value": 0.5917, "depth": 8}
								if obj[2]<=0:
									return 'False'
								elif obj[2]>0:
									# {"feature": "Driving_to", "instances": 2, "metric_value": 1.0, "depth": 9}
									if obj[0]>0:
										return 'False'
									elif obj[0]<=0:
										return 'True'
									else: return 'True'
								else: return 'False'
							else: return 'False'
						else: return 'False'
					elif obj[8]<=0:
						return 'True'
					else: return 'True'
				elif obj[5]<=0:
					return 'False'
				else: return 'False'
			elif obj[14]>1.0:
				# {"feature": "Occupation", "instances": 23, "metric_value": 0.9656, "depth": 4}
				if obj[12]>5:
					# {"feature": "Children", "instances": 20, "metric_value": 0.8813, "depth": 5}
					if obj[10]>0:
						# {"feature": "Coupon_validity", "instances": 11, "metric_value": 0.994, "depth": 6}
						if obj[6]>0:
							# {"feature": "Coffeehouse", "instances": 7, "metric_value": 0.8631, "depth": 7}
							if obj[15]<=1.0:
								return 'False'
							elif obj[15]>1.0:
								# {"feature": "Time", "instances": 3, "metric_value": 0.9183, "depth": 8}
								if obj[4]>0:
									return 'True'
								elif obj[4]<=0:
									return 'False'
								else: return 'False'
							else: return 'True'
						elif obj[6]<=0:
							return 'True'
						else: return 'True'
					elif obj[10]<=0:
						return 'False'
					else: return 'False'
				elif obj[12]<=5:
					return 'True'
				else: return 'True'
			else: return 'False'
		elif obj[11]<=1:
			# {"feature": "Restaurant20to50", "instances": 46, "metric_value": 0.7131, "depth": 3}
			if obj[17]>0.0:
				# {"feature": "Income", "instances": 37, "metric_value": 0.4942, "depth": 4}
				if obj[13]<=7:
					# {"feature": "Maritalstatus", "instances": 34, "metric_value": 0.3228, "depth": 5}
					if obj[9]>0:
						return 'True'
					elif obj[9]<=0:
						# {"feature": "Temperature", "instances": 14, "metric_value": 0.5917, "depth": 6}
						if obj[3]<=55:
							return 'True'
						elif obj[3]>55:
							# {"feature": "Time", "instances": 7, "metric_value": 0.8631, "depth": 7}
							if obj[4]>1:
								# {"feature": "Coupon_validity", "instances": 4, "metric_value": 1.0, "depth": 8}
								if obj[6]>0:
									return 'False'
								elif obj[6]<=0:
									return 'True'
								else: return 'True'
							elif obj[4]<=1:
								return 'True'
							else: return 'True'
						else: return 'True'
					else: return 'True'
				elif obj[13]>7:
					# {"feature": "Age", "instances": 3, "metric_value": 0.9183, "depth": 5}
					if obj[8]<=2:
						return 'False'
					elif obj[8]>2:
						return 'True'
					else: return 'True'
				else: return 'False'
			elif obj[17]<=0.0:
				# {"feature": "Occupation", "instances": 9, "metric_value": 0.9911, "depth": 4}
				if obj[12]>1:
					# {"feature": "Age", "instances": 6, "metric_value": 0.65, "depth": 5}
					if obj[8]<=4:
						return 'False'
					elif obj[8]>4:
						return 'True'
					else: return 'True'
				elif obj[12]<=1:
					return 'True'
				else: return 'True'
			else: return 'False'
		else: return 'True'
	elif obj[19]>2:
		# {"feature": "Coupon", "instances": 16, "metric_value": 0.896, "depth": 2}
		if obj[5]>1:
			# {"feature": "Coupon_validity", "instances": 10, "metric_value": 1.0, "depth": 3}
			if obj[6]>0:
				# {"feature": "Age", "instances": 7, "metric_value": 0.8631, "depth": 4}
				if obj[8]>1:
					return 'False'
				elif obj[8]<=1:
					# {"feature": "Driving_to", "instances": 3, "metric_value": 0.9183, "depth": 5}
					if obj[0]<=1:
						return 'True'
					elif obj[0]>1:
						return 'False'
					else: return 'False'
				else: return 'True'
			elif obj[6]<=0:
				return 'True'
			else: return 'True'
		elif obj[5]<=1:
			return 'False'
		else: return 'False'
	else: return 'False'
