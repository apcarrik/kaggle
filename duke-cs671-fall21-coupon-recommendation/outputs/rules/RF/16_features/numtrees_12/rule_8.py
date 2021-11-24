def findDecision(obj): #obj[0]: Passanger, obj[1]: Weather, obj[2]: Time, obj[3]: Coupon, obj[4]: Coupon_validity, obj[5]: Gender, obj[6]: Age, obj[7]: Children, obj[8]: Education, obj[9]: Occupation, obj[10]: Income, obj[11]: Bar, obj[12]: Coffeehouse, obj[13]: Restaurant20to50, obj[14]: Direction_same, obj[15]: Distance
	# {"feature": "Education", "instances": 85, "metric_value": 0.9774, "depth": 1}
	if obj[8]<=3:
		# {"feature": "Occupation", "instances": 80, "metric_value": 0.9887, "depth": 2}
		if obj[9]<=19:
			# {"feature": "Coupon", "instances": 77, "metric_value": 0.9793, "depth": 3}
			if obj[3]<=3:
				# {"feature": "Income", "instances": 46, "metric_value": 0.9109, "depth": 4}
				if obj[10]>0:
					# {"feature": "Restaurant20to50", "instances": 42, "metric_value": 0.9403, "depth": 5}
					if obj[13]>0.0:
						# {"feature": "Distance", "instances": 38, "metric_value": 0.8997, "depth": 6}
						if obj[15]<=2:
							# {"feature": "Bar", "instances": 32, "metric_value": 0.9544, "depth": 7}
							if obj[11]>-1.0:
								# {"feature": "Coffeehouse", "instances": 31, "metric_value": 0.9383, "depth": 8}
								if obj[12]<=3.0:
									# {"feature": "Age", "instances": 30, "metric_value": 0.9183, "depth": 9}
									if obj[6]<=4:
										# {"feature": "Coupon_validity", "instances": 25, "metric_value": 0.8555, "depth": 10}
										if obj[4]<=0:
											# {"feature": "Time", "instances": 14, "metric_value": 0.7496, "depth": 11}
											if obj[2]<=1:
												# {"feature": "Direction_same", "instances": 9, "metric_value": 0.9183, "depth": 12}
												if obj[14]<=0:
													# {"feature": "Passanger", "instances": 6, "metric_value": 1.0, "depth": 13}
													if obj[0]<=1:
														# {"feature": "Gender", "instances": 5, "metric_value": 0.971, "depth": 14}
														if obj[5]<=0:
															# {"feature": "Children", "instances": 3, "metric_value": 0.9183, "depth": 15}
															if obj[7]>0:
																# {"feature": "Weather", "instances": 2, "metric_value": 1.0, "depth": 16}
																if obj[1]<=0:
																	return 'False'
																else: return 'False'
															elif obj[7]<=0:
																return 'True'
															else: return 'True'
														elif obj[5]>0:
															# {"feature": "Children", "instances": 2, "metric_value": 1.0, "depth": 15}
															if obj[7]>0:
																return 'True'
															elif obj[7]<=0:
																return 'False'
															else: return 'False'
														else: return 'True'
													elif obj[0]>1:
														return 'False'
													else: return 'False'
												elif obj[14]>0:
													return 'True'
												else: return 'True'
											elif obj[2]>1:
												return 'True'
											else: return 'True'
										elif obj[4]>0:
											# {"feature": "Time", "instances": 11, "metric_value": 0.9457, "depth": 11}
											if obj[2]>0:
												# {"feature": "Direction_same", "instances": 9, "metric_value": 0.9911, "depth": 12}
												if obj[14]<=0:
													# {"feature": "Gender", "instances": 8, "metric_value": 0.9544, "depth": 13}
													if obj[5]>0:
														# {"feature": "Passanger", "instances": 4, "metric_value": 1.0, "depth": 14}
														if obj[0]>0:
															# {"feature": "Children", "instances": 3, "metric_value": 0.9183, "depth": 15}
															if obj[7]>0:
																# {"feature": "Weather", "instances": 2, "metric_value": 1.0, "depth": 16}
																if obj[1]<=0:
																	return 'False'
																else: return 'False'
															elif obj[7]<=0:
																return 'True'
															else: return 'True'
														elif obj[0]<=0:
															return 'False'
														else: return 'False'
													elif obj[5]<=0:
														# {"feature": "Passanger", "instances": 4, "metric_value": 0.8113, "depth": 14}
														if obj[0]<=2:
															return 'True'
														elif obj[0]>2:
															return 'False'
														else: return 'False'
													else: return 'True'
												elif obj[14]>0:
													return 'False'
												else: return 'False'
											elif obj[2]<=0:
												return 'True'
											else: return 'True'
										else: return 'True'
									elif obj[6]>4:
										# {"feature": "Gender", "instances": 5, "metric_value": 0.971, "depth": 10}
										if obj[5]>0:
											# {"feature": "Coupon_validity", "instances": 3, "metric_value": 0.9183, "depth": 11}
											if obj[4]<=0:
												return 'True'
											elif obj[4]>0:
												return 'False'
											else: return 'False'
										elif obj[5]<=0:
											return 'False'
										else: return 'False'
									else: return 'False'
								elif obj[12]>3.0:
									return 'False'
								else: return 'False'
							elif obj[11]<=-1.0:
								return 'False'
							else: return 'False'
						elif obj[15]>2:
							return 'True'
						else: return 'True'
					elif obj[13]<=0.0:
						# {"feature": "Passanger", "instances": 4, "metric_value": 0.8113, "depth": 6}
						if obj[0]<=1:
							return 'False'
						elif obj[0]>1:
							return 'True'
						else: return 'True'
					else: return 'False'
				elif obj[10]<=0:
					return 'True'
				else: return 'True'
			elif obj[3]>3:
				# {"feature": "Weather", "instances": 31, "metric_value": 0.9932, "depth": 4}
				if obj[1]<=0:
					# {"feature": "Coffeehouse", "instances": 28, "metric_value": 1.0, "depth": 5}
					if obj[12]>0.0:
						# {"feature": "Distance", "instances": 16, "metric_value": 0.896, "depth": 6}
						if obj[15]>1:
							# {"feature": "Time", "instances": 11, "metric_value": 0.994, "depth": 7}
							if obj[2]<=2:
								# {"feature": "Age", "instances": 8, "metric_value": 0.9544, "depth": 8}
								if obj[6]<=3:
									return 'False'
								elif obj[6]>3:
									# {"feature": "Income", "instances": 4, "metric_value": 0.8113, "depth": 9}
									if obj[10]<=2:
										return 'True'
									elif obj[10]>2:
										return 'False'
									else: return 'False'
								else: return 'True'
							elif obj[2]>2:
								return 'True'
							else: return 'True'
						elif obj[15]<=1:
							return 'True'
						else: return 'True'
					elif obj[12]<=0.0:
						# {"feature": "Time", "instances": 12, "metric_value": 0.8113, "depth": 6}
						if obj[2]>1:
							# {"feature": "Children", "instances": 7, "metric_value": 0.9852, "depth": 7}
							if obj[7]>0:
								# {"feature": "Bar", "instances": 4, "metric_value": 0.8113, "depth": 8}
								if obj[11]<=0.0:
									return 'True'
								elif obj[11]>0.0:
									return 'False'
								else: return 'False'
							elif obj[7]<=0:
								return 'False'
							else: return 'False'
						elif obj[2]<=1:
							return 'False'
						else: return 'False'
					else: return 'False'
				elif obj[1]>0:
					return 'False'
				else: return 'False'
			else: return 'False'
		elif obj[9]>19:
			return 'False'
		else: return 'False'
	elif obj[8]>3:
		return 'True'
	else: return 'True'
