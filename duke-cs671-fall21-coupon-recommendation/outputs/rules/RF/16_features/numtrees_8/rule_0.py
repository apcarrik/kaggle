def findDecision(obj): #obj[0]: Passanger, obj[1]: Weather, obj[2]: Time, obj[3]: Coupon, obj[4]: Coupon_validity, obj[5]: Gender, obj[6]: Age, obj[7]: Children, obj[8]: Education, obj[9]: Occupation, obj[10]: Income, obj[11]: Bar, obj[12]: Coffeehouse, obj[13]: Restaurant20to50, obj[14]: Direction_same, obj[15]: Distance
	# {"feature": "Coupon", "instances": 127, "metric_value": 0.9978, "depth": 1}
	if obj[3]>0:
		# {"feature": "Coupon_validity", "instances": 112, "metric_value": 0.9887, "depth": 2}
		if obj[4]<=0:
			# {"feature": "Occupation", "instances": 60, "metric_value": 0.9341, "depth": 3}
			if obj[9]>1:
				# {"feature": "Time", "instances": 51, "metric_value": 0.9774, "depth": 4}
				if obj[2]<=1:
					# {"feature": "Passanger", "instances": 27, "metric_value": 0.9751, "depth": 5}
					if obj[0]>0:
						# {"feature": "Restaurant20to50", "instances": 25, "metric_value": 0.9427, "depth": 6}
						if obj[13]>0.0:
							# {"feature": "Distance", "instances": 21, "metric_value": 0.8631, "depth": 7}
							if obj[15]<=1:
								# {"feature": "Coffeehouse", "instances": 12, "metric_value": 0.4138, "depth": 8}
								if obj[12]<=3.0:
									return 'False'
								elif obj[12]>3.0:
									# {"feature": "Gender", "instances": 3, "metric_value": 0.9183, "depth": 9}
									if obj[5]>0:
										# {"feature": "Age", "instances": 2, "metric_value": 1.0, "depth": 10}
										if obj[6]>2:
											return 'True'
										elif obj[6]<=2:
											return 'False'
										else: return 'False'
									elif obj[5]<=0:
										return 'False'
									else: return 'False'
								else: return 'False'
							elif obj[15]>1:
								# {"feature": "Bar", "instances": 9, "metric_value": 0.9911, "depth": 8}
								if obj[11]<=0.0:
									# {"feature": "Age", "instances": 5, "metric_value": 0.7219, "depth": 9}
									if obj[6]>0:
										return 'True'
									elif obj[6]<=0:
										# {"feature": "Children", "instances": 2, "metric_value": 1.0, "depth": 10}
										if obj[7]<=0:
											return 'True'
										elif obj[7]>0:
											return 'False'
										else: return 'False'
									else: return 'True'
								elif obj[11]>0.0:
									# {"feature": "Age", "instances": 4, "metric_value": 0.8113, "depth": 9}
									if obj[6]>4:
										# {"feature": "Education", "instances": 2, "metric_value": 1.0, "depth": 10}
										if obj[8]>2:
											return 'False'
										elif obj[8]<=2:
											return 'True'
										else: return 'True'
									elif obj[6]<=4:
										return 'False'
									else: return 'False'
								else: return 'False'
							else: return 'True'
						elif obj[13]<=0.0:
							# {"feature": "Weather", "instances": 4, "metric_value": 0.8113, "depth": 7}
							if obj[1]<=0:
								return 'True'
							elif obj[1]>0:
								return 'False'
							else: return 'False'
						else: return 'True'
					elif obj[0]<=0:
						return 'True'
					else: return 'True'
				elif obj[2]>1:
					# {"feature": "Coffeehouse", "instances": 24, "metric_value": 0.7383, "depth": 5}
					if obj[12]>0.0:
						# {"feature": "Income", "instances": 18, "metric_value": 0.3095, "depth": 6}
						if obj[10]<=7:
							return 'True'
						elif obj[10]>7:
							# {"feature": "Passanger", "instances": 2, "metric_value": 1.0, "depth": 7}
							if obj[0]<=1:
								return 'False'
							elif obj[0]>1:
								return 'True'
							else: return 'True'
						else: return 'False'
					elif obj[12]<=0.0:
						# {"feature": "Passanger", "instances": 6, "metric_value": 0.9183, "depth": 6}
						if obj[0]<=2:
							return 'False'
						elif obj[0]>2:
							return 'True'
						else: return 'True'
					else: return 'False'
				else: return 'True'
			elif obj[9]<=1:
				return 'True'
			else: return 'True'
		elif obj[4]>0:
			# {"feature": "Occupation", "instances": 52, "metric_value": 0.9957, "depth": 3}
			if obj[9]<=20:
				# {"feature": "Restaurant20to50", "instances": 49, "metric_value": 0.9852, "depth": 4}
				if obj[13]<=3.0:
					# {"feature": "Income", "instances": 46, "metric_value": 0.9945, "depth": 5}
					if obj[10]<=7:
						# {"feature": "Children", "instances": 44, "metric_value": 0.9865, "depth": 6}
						if obj[7]<=0:
							# {"feature": "Passanger", "instances": 22, "metric_value": 0.8454, "depth": 7}
							if obj[0]>0:
								# {"feature": "Age", "instances": 20, "metric_value": 0.7219, "depth": 8}
								if obj[6]<=5:
									# {"feature": "Gender", "instances": 18, "metric_value": 0.5033, "depth": 9}
									if obj[5]<=0:
										return 'False'
									elif obj[5]>0:
										# {"feature": "Time", "instances": 6, "metric_value": 0.9183, "depth": 10}
										if obj[2]>1:
											return 'False'
										elif obj[2]<=1:
											# {"feature": "Education", "instances": 3, "metric_value": 0.9183, "depth": 11}
											if obj[8]>0:
												return 'True'
											elif obj[8]<=0:
												return 'False'
											else: return 'False'
										else: return 'True'
									else: return 'False'
								elif obj[6]>5:
									return 'True'
								else: return 'True'
							elif obj[0]<=0:
								return 'True'
							else: return 'True'
						elif obj[7]>0:
							# {"feature": "Passanger", "instances": 22, "metric_value": 0.976, "depth": 7}
							if obj[0]>0:
								# {"feature": "Time", "instances": 20, "metric_value": 0.9341, "depth": 8}
								if obj[2]<=3:
									# {"feature": "Bar", "instances": 15, "metric_value": 0.9968, "depth": 9}
									if obj[11]<=1.0:
										# {"feature": "Education", "instances": 13, "metric_value": 0.9957, "depth": 10}
										if obj[8]<=3:
											# {"feature": "Age", "instances": 12, "metric_value": 0.9799, "depth": 11}
											if obj[6]>3:
												# {"feature": "Coffeehouse", "instances": 7, "metric_value": 0.9852, "depth": 12}
												if obj[12]<=2.0:
													# {"feature": "Distance", "instances": 6, "metric_value": 0.9183, "depth": 13}
													if obj[15]>1:
														# {"feature": "Weather", "instances": 5, "metric_value": 0.971, "depth": 14}
														if obj[1]>0:
															# {"feature": "Gender", "instances": 4, "metric_value": 0.8113, "depth": 15}
															if obj[5]<=0:
																# {"feature": "Direction_same", "instances": 2, "metric_value": 1.0, "depth": 16}
																if obj[14]<=0:
																	return 'True'
																else: return 'True'
															elif obj[5]>0:
																return 'True'
															else: return 'True'
														elif obj[1]<=0:
															return 'False'
														else: return 'False'
													elif obj[15]<=1:
														return 'True'
													else: return 'True'
												elif obj[12]>2.0:
													return 'False'
												else: return 'False'
											elif obj[6]<=3:
												# {"feature": "Coffeehouse", "instances": 5, "metric_value": 0.7219, "depth": 12}
												if obj[12]>0.0:
													return 'False'
												elif obj[12]<=0.0:
													# {"feature": "Gender", "instances": 2, "metric_value": 1.0, "depth": 13}
													if obj[5]>0:
														return 'True'
													elif obj[5]<=0:
														return 'False'
													else: return 'False'
												else: return 'True'
											else: return 'False'
										elif obj[8]>3:
											return 'True'
										else: return 'True'
									elif obj[11]>1.0:
										return 'True'
									else: return 'True'
								elif obj[2]>3:
									return 'True'
								else: return 'True'
							elif obj[0]<=0:
								return 'False'
							else: return 'False'
						else: return 'True'
					elif obj[10]>7:
						return 'True'
					else: return 'True'
				elif obj[13]>3.0:
					return 'False'
				else: return 'False'
			elif obj[9]>20:
				return 'True'
			else: return 'True'
		else: return 'False'
	elif obj[3]<=0:
		# {"feature": "Age", "instances": 15, "metric_value": 0.8366, "depth": 2}
		if obj[6]>1:
			return 'False'
		elif obj[6]<=1:
			# {"feature": "Education", "instances": 7, "metric_value": 0.9852, "depth": 3}
			if obj[8]<=1:
				return 'True'
			elif obj[8]>1:
				return 'False'
			else: return 'False'
		else: return 'True'
	else: return 'False'
