def findDecision(obj): #obj[0]: Passanger, obj[1]: Weather, obj[2]: Time, obj[3]: Coupon, obj[4]: Coupon_validity, obj[5]: Gender, obj[6]: Age, obj[7]: Maritalstatus, obj[8]: Children, obj[9]: Education, obj[10]: Occupation, obj[11]: Income, obj[12]: Bar, obj[13]: Coffeehouse, obj[14]: Restaurant20to50, obj[15]: Direction_same, obj[16]: Distance
	# {"feature": "Occupation", "instances": 85, "metric_value": 0.9879, "depth": 1}
	if obj[10]<=19:
		# {"feature": "Education", "instances": 80, "metric_value": 0.971, "depth": 2}
		if obj[9]<=2:
			# {"feature": "Restaurant20to50", "instances": 60, "metric_value": 0.9183, "depth": 3}
			if obj[14]<=2.0:
				# {"feature": "Maritalstatus", "instances": 56, "metric_value": 0.9403, "depth": 4}
				if obj[7]>0:
					# {"feature": "Age", "instances": 37, "metric_value": 0.9868, "depth": 5}
					if obj[6]<=4:
						# {"feature": "Time", "instances": 33, "metric_value": 0.9993, "depth": 6}
						if obj[2]<=3:
							# {"feature": "Bar", "instances": 25, "metric_value": 0.9896, "depth": 7}
							if obj[12]>0.0:
								# {"feature": "Coupon", "instances": 14, "metric_value": 0.8631, "depth": 8}
								if obj[3]>0:
									# {"feature": "Income", "instances": 13, "metric_value": 0.7793, "depth": 9}
									if obj[11]<=3:
										# {"feature": "Distance", "instances": 10, "metric_value": 0.8813, "depth": 10}
										if obj[16]<=2:
											# {"feature": "Coffeehouse", "instances": 8, "metric_value": 0.9544, "depth": 11}
											if obj[13]>1.0:
												# {"feature": "Coupon_validity", "instances": 5, "metric_value": 0.7219, "depth": 12}
												if obj[4]>0:
													return 'False'
												elif obj[4]<=0:
													# {"feature": "Passanger", "instances": 2, "metric_value": 1.0, "depth": 13}
													if obj[0]<=1:
														# {"feature": "Weather", "instances": 2, "metric_value": 1.0, "depth": 14}
														if obj[1]<=0:
															# {"feature": "Gender", "instances": 2, "metric_value": 1.0, "depth": 15}
															if obj[5]<=0:
																# {"feature": "Children", "instances": 2, "metric_value": 1.0, "depth": 16}
																if obj[8]<=0:
																	# {"feature": "Direction_same", "instances": 2, "metric_value": 1.0, "depth": 17}
																	if obj[15]<=0:
																		return 'True'
																	else: return 'True'
																else: return 'True'
															else: return 'True'
														else: return 'True'
													else: return 'True'
												else: return 'True'
											elif obj[13]<=1.0:
												# {"feature": "Gender", "instances": 3, "metric_value": 0.9183, "depth": 12}
												if obj[5]<=0:
													return 'True'
												elif obj[5]>0:
													return 'False'
												else: return 'False'
											else: return 'True'
										elif obj[16]>2:
											return 'False'
										else: return 'False'
									elif obj[11]>3:
										return 'False'
									else: return 'False'
								elif obj[3]<=0:
									return 'True'
								else: return 'True'
							elif obj[12]<=0.0:
								# {"feature": "Income", "instances": 11, "metric_value": 0.9457, "depth": 8}
								if obj[11]<=6:
									# {"feature": "Distance", "instances": 6, "metric_value": 0.9183, "depth": 9}
									if obj[16]<=1:
										return 'False'
									elif obj[16]>1:
										# {"feature": "Coupon", "instances": 3, "metric_value": 0.9183, "depth": 10}
										if obj[3]>0:
											return 'True'
										elif obj[3]<=0:
											return 'False'
										else: return 'False'
									else: return 'True'
								elif obj[11]>6:
									return 'True'
								else: return 'True'
							else: return 'True'
						elif obj[2]>3:
							# {"feature": "Coffeehouse", "instances": 8, "metric_value": 0.8113, "depth": 7}
							if obj[13]>0.0:
								return 'True'
							elif obj[13]<=0.0:
								# {"feature": "Passanger", "instances": 3, "metric_value": 0.9183, "depth": 8}
								if obj[0]<=1:
									return 'False'
								elif obj[0]>1:
									return 'True'
								else: return 'True'
							else: return 'False'
						else: return 'True'
					elif obj[6]>4:
						return 'True'
					else: return 'True'
				elif obj[7]<=0:
					# {"feature": "Gender", "instances": 19, "metric_value": 0.7425, "depth": 5}
					if obj[5]>0:
						# {"feature": "Coffeehouse", "instances": 11, "metric_value": 0.9457, "depth": 6}
						if obj[13]<=1.0:
							# {"feature": "Distance", "instances": 6, "metric_value": 0.9183, "depth": 7}
							if obj[16]<=2:
								# {"feature": "Passanger", "instances": 5, "metric_value": 0.7219, "depth": 8}
								if obj[0]<=1:
									return 'False'
								elif obj[0]>1:
									# {"feature": "Time", "instances": 2, "metric_value": 1.0, "depth": 9}
									if obj[2]>2:
										return 'False'
									elif obj[2]<=2:
										return 'True'
									else: return 'True'
								else: return 'False'
							elif obj[16]>2:
								return 'True'
							else: return 'True'
						elif obj[13]>1.0:
							return 'True'
						else: return 'True'
					elif obj[5]<=0:
						return 'True'
					else: return 'True'
				else: return 'True'
			elif obj[14]>2.0:
				return 'True'
			else: return 'True'
		elif obj[9]>2:
			# {"feature": "Coffeehouse", "instances": 20, "metric_value": 0.971, "depth": 3}
			if obj[13]>1.0:
				# {"feature": "Gender", "instances": 15, "metric_value": 0.9968, "depth": 4}
				if obj[5]>0:
					# {"feature": "Income", "instances": 11, "metric_value": 0.9457, "depth": 5}
					if obj[11]<=5:
						# {"feature": "Direction_same", "instances": 9, "metric_value": 0.7642, "depth": 6}
						if obj[15]<=0:
							# {"feature": "Distance", "instances": 8, "metric_value": 0.5436, "depth": 7}
							if obj[16]>1:
								return 'False'
							elif obj[16]<=1:
								return 'True'
							else: return 'True'
						elif obj[15]>0:
							return 'True'
						else: return 'True'
					elif obj[11]>5:
						return 'True'
					else: return 'True'
				elif obj[5]<=0:
					return 'True'
				else: return 'True'
			elif obj[13]<=1.0:
				return 'False'
			else: return 'False'
		else: return 'False'
	elif obj[10]>19:
		return 'False'
	else: return 'False'
