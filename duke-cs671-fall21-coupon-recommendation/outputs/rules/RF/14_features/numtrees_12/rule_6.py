def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Gender, obj[4]: Age, obj[5]: Children, obj[6]: Education, obj[7]: Occupation, obj[8]: Income, obj[9]: Bar, obj[10]: Coffeehouse, obj[11]: Restaurant20to50, obj[12]: Direction_same, obj[13]: Distance
	# {"feature": "Time", "instances": 85, "metric_value": 0.9999, "depth": 1}
	if obj[1]<=3:
		# {"feature": "Bar", "instances": 73, "metric_value": 0.989, "depth": 2}
		if obj[9]<=2.0:
			# {"feature": "Age", "instances": 63, "metric_value": 0.9587, "depth": 3}
			if obj[4]<=6:
				# {"feature": "Education", "instances": 61, "metric_value": 0.9432, "depth": 4}
				if obj[6]<=2:
					# {"feature": "Passanger", "instances": 52, "metric_value": 0.9732, "depth": 5}
					if obj[0]<=1:
						# {"feature": "Occupation", "instances": 36, "metric_value": 0.888, "depth": 6}
						if obj[7]>2:
							# {"feature": "Income", "instances": 29, "metric_value": 0.9576, "depth": 7}
							if obj[8]>0:
								# {"feature": "Coffeehouse", "instances": 27, "metric_value": 0.9183, "depth": 8}
								if obj[10]>0.0:
									# {"feature": "Children", "instances": 19, "metric_value": 0.9819, "depth": 9}
									if obj[5]<=0:
										# {"feature": "Restaurant20to50", "instances": 13, "metric_value": 0.8905, "depth": 10}
										if obj[11]>0.0:
											# {"feature": "Coupon", "instances": 12, "metric_value": 0.8113, "depth": 11}
											if obj[2]<=2:
												# {"feature": "Gender", "instances": 6, "metric_value": 0.9183, "depth": 12}
												if obj[3]<=0:
													# {"feature": "Direction_same", "instances": 4, "metric_value": 0.8113, "depth": 13}
													if obj[12]<=0:
														# {"feature": "Distance", "instances": 4, "metric_value": 0.8113, "depth": 14}
														if obj[13]<=3:
															return 'False'
														else: return 'False'
													else: return 'False'
												elif obj[3]>0:
													# {"feature": "Direction_same", "instances": 2, "metric_value": 1.0, "depth": 13}
													if obj[12]<=1:
														# {"feature": "Distance", "instances": 2, "metric_value": 1.0, "depth": 14}
														if obj[13]<=1:
															return 'False'
														else: return 'False'
													else: return 'False'
												else: return 'False'
											elif obj[2]>2:
												# {"feature": "Gender", "instances": 6, "metric_value": 0.65, "depth": 12}
												if obj[3]>0:
													# {"feature": "Direction_same", "instances": 4, "metric_value": 0.8113, "depth": 13}
													if obj[12]>0:
														return 'False'
													elif obj[12]<=0:
														# {"feature": "Distance", "instances": 2, "metric_value": 1.0, "depth": 14}
														if obj[13]>1:
															return 'False'
														elif obj[13]<=1:
															return 'True'
														else: return 'True'
													else: return 'False'
												elif obj[3]<=0:
													return 'False'
												else: return 'False'
											else: return 'False'
										elif obj[11]<=0.0:
											return 'True'
										else: return 'True'
									elif obj[5]>0:
										# {"feature": "Gender", "instances": 6, "metric_value": 0.9183, "depth": 10}
										if obj[3]<=0:
											# {"feature": "Coupon", "instances": 3, "metric_value": 0.9183, "depth": 11}
											if obj[2]<=3:
												return 'False'
											elif obj[2]>3:
												return 'True'
											else: return 'True'
										elif obj[3]>0:
											return 'True'
										else: return 'True'
									else: return 'True'
								elif obj[10]<=0.0:
									# {"feature": "Coupon", "instances": 8, "metric_value": 0.5436, "depth": 9}
									if obj[2]>3:
										return 'False'
									elif obj[2]<=3:
										# {"feature": "Restaurant20to50", "instances": 4, "metric_value": 0.8113, "depth": 10}
										if obj[11]<=1.0:
											return 'False'
										elif obj[11]>1.0:
											# {"feature": "Gender", "instances": 2, "metric_value": 1.0, "depth": 11}
											if obj[3]<=0:
												# {"feature": "Children", "instances": 2, "metric_value": 1.0, "depth": 12}
												if obj[5]<=0:
													# {"feature": "Direction_same", "instances": 2, "metric_value": 1.0, "depth": 13}
													if obj[12]<=0:
														# {"feature": "Distance", "instances": 2, "metric_value": 1.0, "depth": 14}
														if obj[13]<=2:
															return 'True'
														else: return 'True'
													else: return 'True'
												else: return 'True'
											else: return 'True'
										else: return 'True'
									else: return 'False'
								else: return 'False'
							elif obj[8]<=0:
								return 'True'
							else: return 'True'
						elif obj[7]<=2:
							return 'False'
						else: return 'False'
					elif obj[0]>1:
						# {"feature": "Restaurant20to50", "instances": 16, "metric_value": 0.9544, "depth": 6}
						if obj[11]>0.0:
							# {"feature": "Coupon", "instances": 13, "metric_value": 0.9957, "depth": 7}
							if obj[2]<=3:
								# {"feature": "Income", "instances": 10, "metric_value": 0.8813, "depth": 8}
								if obj[8]<=7:
									# {"feature": "Occupation", "instances": 9, "metric_value": 0.7642, "depth": 9}
									if obj[7]>2:
										return 'True'
									elif obj[7]<=2:
										# {"feature": "Coffeehouse", "instances": 3, "metric_value": 0.9183, "depth": 10}
										if obj[10]<=1.0:
											return 'False'
										elif obj[10]>1.0:
											return 'True'
										else: return 'True'
									else: return 'False'
								elif obj[8]>7:
									return 'False'
								else: return 'False'
							elif obj[2]>3:
								return 'False'
							else: return 'False'
						elif obj[11]<=0.0:
							return 'True'
						else: return 'True'
					else: return 'True'
				elif obj[6]>2:
					# {"feature": "Income", "instances": 9, "metric_value": 0.5033, "depth": 5}
					if obj[8]<=6:
						return 'False'
					elif obj[8]>6:
						return 'True'
					else: return 'True'
				else: return 'False'
			elif obj[4]>6:
				return 'True'
			else: return 'True'
		elif obj[9]>2.0:
			# {"feature": "Occupation", "instances": 10, "metric_value": 0.7219, "depth": 3}
			if obj[7]<=7:
				return 'True'
			elif obj[7]>7:
				return 'False'
			else: return 'False'
		else: return 'True'
	elif obj[1]>3:
		# {"feature": "Age", "instances": 12, "metric_value": 0.4138, "depth": 2}
		if obj[4]<=4:
			return 'True'
		elif obj[4]>4:
			return 'False'
		else: return 'False'
	else: return 'True'
