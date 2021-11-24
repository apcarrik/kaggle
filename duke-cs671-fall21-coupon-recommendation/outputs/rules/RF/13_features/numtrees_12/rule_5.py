def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Gender, obj[4]: Age, obj[5]: Children, obj[6]: Education, obj[7]: Occupation, obj[8]: Bar, obj[9]: Coffeehouse, obj[10]: Restaurant20to50, obj[11]: Direction_same, obj[12]: Distance
	# {"feature": "Coffeehouse", "instances": 85, "metric_value": 0.9975, "depth": 1}
	if obj[9]<=3.0:
		# {"feature": "Coupon", "instances": 78, "metric_value": 0.9881, "depth": 2}
		if obj[2]>0:
			# {"feature": "Occupation", "instances": 64, "metric_value": 0.9544, "depth": 3}
			if obj[7]<=17:
				# {"feature": "Bar", "instances": 60, "metric_value": 0.9183, "depth": 4}
				if obj[8]<=2.0:
					# {"feature": "Restaurant20to50", "instances": 57, "metric_value": 0.9348, "depth": 5}
					if obj[10]>-1.0:
						# {"feature": "Children", "instances": 56, "metric_value": 0.9241, "depth": 6}
						if obj[5]<=0:
							# {"feature": "Distance", "instances": 34, "metric_value": 0.8338, "depth": 7}
							if obj[12]<=2:
								# {"feature": "Passanger", "instances": 31, "metric_value": 0.8691, "depth": 8}
								if obj[0]<=1:
									# {"feature": "Age", "instances": 19, "metric_value": 0.9495, "depth": 9}
									if obj[4]>0:
										# {"feature": "Time", "instances": 18, "metric_value": 0.9641, "depth": 10}
										if obj[1]<=2:
											# {"feature": "Direction_same", "instances": 13, "metric_value": 0.8905, "depth": 11}
											if obj[11]<=0:
												# {"feature": "Gender", "instances": 7, "metric_value": 0.5917, "depth": 12}
												if obj[3]>0:
													# {"feature": "Education", "instances": 4, "metric_value": 0.8113, "depth": 13}
													if obj[6]>0:
														return 'True'
													elif obj[6]<=0:
														return 'True'
													else: return 'True'
												elif obj[3]<=0:
													return 'True'
												else: return 'True'
											elif obj[11]>0:
												# {"feature": "Gender", "instances": 6, "metric_value": 1.0, "depth": 12}
												if obj[3]<=0:
													# {"feature": "Education", "instances": 4, "metric_value": 0.8113, "depth": 13}
													if obj[6]<=0:
														return 'False'
													elif obj[6]>0:
														return 'True'
													else: return 'True'
												elif obj[3]>0:
													return 'True'
												else: return 'True'
											else: return 'False'
										elif obj[1]>2:
											# {"feature": "Education", "instances": 5, "metric_value": 0.971, "depth": 11}
											if obj[6]<=0:
												# {"feature": "Direction_same", "instances": 3, "metric_value": 0.9183, "depth": 12}
												if obj[11]<=0:
													# {"feature": "Gender", "instances": 2, "metric_value": 1.0, "depth": 13}
													if obj[3]<=0:
														return 'False'
													else: return 'False'
												elif obj[11]>0:
													return 'True'
												else: return 'True'
											elif obj[6]>0:
												return 'False'
											else: return 'False'
										else: return 'False'
									elif obj[4]<=0:
										return 'True'
									else: return 'True'
								elif obj[0]>1:
									# {"feature": "Time", "instances": 12, "metric_value": 0.65, "depth": 9}
									if obj[1]<=2:
										# {"feature": "Age", "instances": 7, "metric_value": 0.8631, "depth": 10}
										if obj[4]<=4:
											# {"feature": "Gender", "instances": 5, "metric_value": 0.971, "depth": 11}
											if obj[3]<=0:
												# {"feature": "Education", "instances": 3, "metric_value": 0.9183, "depth": 12}
												if obj[6]>0:
													# {"feature": "Direction_same", "instances": 2, "metric_value": 1.0, "depth": 13}
													if obj[11]<=0:
														return 'False'
													else: return 'False'
												elif obj[6]<=0:
													return 'True'
												else: return 'True'
											elif obj[3]>0:
												# {"feature": "Education", "instances": 2, "metric_value": 1.0, "depth": 12}
												if obj[6]<=0:
													return 'False'
												elif obj[6]>0:
													return 'True'
												else: return 'True'
											else: return 'False'
										elif obj[4]>4:
											return 'True'
										else: return 'True'
									elif obj[1]>2:
										return 'True'
									else: return 'True'
								else: return 'True'
							elif obj[12]>2:
								return 'True'
							else: return 'True'
						elif obj[5]>0:
							# {"feature": "Education", "instances": 22, "metric_value": 0.994, "depth": 7}
							if obj[6]<=2:
								# {"feature": "Age", "instances": 20, "metric_value": 0.971, "depth": 8}
								if obj[4]<=3:
									# {"feature": "Passanger", "instances": 16, "metric_value": 1.0, "depth": 9}
									if obj[0]>1:
										# {"feature": "Time", "instances": 13, "metric_value": 0.9957, "depth": 10}
										if obj[1]>0:
											# {"feature": "Distance", "instances": 10, "metric_value": 0.971, "depth": 11}
											if obj[12]>1:
												# {"feature": "Gender", "instances": 8, "metric_value": 0.9544, "depth": 12}
												if obj[3]<=0:
													# {"feature": "Direction_same", "instances": 5, "metric_value": 0.971, "depth": 13}
													if obj[11]<=0:
														return 'False'
													else: return 'False'
												elif obj[3]>0:
													# {"feature": "Direction_same", "instances": 3, "metric_value": 0.9183, "depth": 13}
													if obj[11]<=0:
														return 'False'
													else: return 'False'
												else: return 'False'
											elif obj[12]<=1:
												# {"feature": "Gender", "instances": 2, "metric_value": 1.0, "depth": 12}
												if obj[3]<=1:
													# {"feature": "Direction_same", "instances": 2, "metric_value": 1.0, "depth": 13}
													if obj[11]<=0:
														return 'False'
													else: return 'False'
												else: return 'False'
											else: return 'False'
										elif obj[1]<=0:
											# {"feature": "Distance", "instances": 3, "metric_value": 0.9183, "depth": 11}
											if obj[12]<=1:
												# {"feature": "Gender", "instances": 2, "metric_value": 1.0, "depth": 12}
												if obj[3]<=1:
													# {"feature": "Direction_same", "instances": 2, "metric_value": 1.0, "depth": 13}
													if obj[11]<=0:
														return 'True'
													else: return 'True'
												else: return 'True'
											elif obj[12]>1:
												return 'True'
											else: return 'True'
										else: return 'True'
									elif obj[0]<=1:
										# {"feature": "Time", "instances": 3, "metric_value": 0.9183, "depth": 10}
										if obj[1]>1:
											return 'True'
										elif obj[1]<=1:
											return 'False'
										else: return 'False'
									else: return 'True'
								elif obj[4]>3:
									return 'True'
								else: return 'True'
							elif obj[6]>2:
								return 'False'
							else: return 'False'
						else: return 'True'
					elif obj[10]<=-1.0:
						return 'False'
					else: return 'False'
				elif obj[8]>2.0:
					return 'True'
				else: return 'True'
			elif obj[7]>17:
				return 'False'
			else: return 'False'
		elif obj[2]<=0:
			# {"feature": "Age", "instances": 14, "metric_value": 0.8631, "depth": 3}
			if obj[4]>1:
				return 'False'
			elif obj[4]<=1:
				# {"feature": "Gender", "instances": 6, "metric_value": 0.9183, "depth": 4}
				if obj[3]<=0:
					return 'True'
				elif obj[3]>0:
					return 'False'
				else: return 'False'
			else: return 'True'
		else: return 'False'
	elif obj[9]>3.0:
		# {"feature": "Coupon", "instances": 7, "metric_value": 0.5917, "depth": 2}
		if obj[2]>0:
			return 'False'
		elif obj[2]<=0:
			# {"feature": "Gender", "instances": 2, "metric_value": 1.0, "depth": 3}
			if obj[3]<=0:
				return 'True'
			elif obj[3]>0:
				return 'False'
			else: return 'False'
		else: return 'True'
	else: return 'False'
