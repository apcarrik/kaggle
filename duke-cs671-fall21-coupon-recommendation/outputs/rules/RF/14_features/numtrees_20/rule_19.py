def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Gender, obj[4]: Age, obj[5]: Children, obj[6]: Education, obj[7]: Occupation, obj[8]: Income, obj[9]: Bar, obj[10]: Coffeehouse, obj[11]: Restaurant20to50, obj[12]: Direction_same, obj[13]: Distance
	# {"feature": "Distance", "instances": 51, "metric_value": 0.9975, "depth": 1}
	if obj[13]>1:
		# {"feature": "Income", "instances": 27, "metric_value": 0.8767, "depth": 2}
		if obj[8]>1:
			# {"feature": "Restaurant20to50", "instances": 21, "metric_value": 0.9587, "depth": 3}
			if obj[11]>0.0:
				# {"feature": "Time", "instances": 17, "metric_value": 0.9975, "depth": 4}
				if obj[1]>0:
					# {"feature": "Education", "instances": 10, "metric_value": 0.8813, "depth": 5}
					if obj[6]<=2:
						# {"feature": "Coffeehouse", "instances": 9, "metric_value": 0.7642, "depth": 6}
						if obj[10]<=2.0:
							return 'True'
						elif obj[10]>2.0:
							# {"feature": "Passanger", "instances": 4, "metric_value": 1.0, "depth": 7}
							if obj[0]<=1:
								return 'False'
							elif obj[0]>1:
								return 'True'
							else: return 'True'
						else: return 'False'
					elif obj[6]>2:
						return 'False'
					else: return 'False'
				elif obj[1]<=0:
					# {"feature": "Passanger", "instances": 7, "metric_value": 0.5917, "depth": 5}
					if obj[0]<=2:
						return 'False'
					elif obj[0]>2:
						return 'True'
					else: return 'True'
				else: return 'False'
			elif obj[11]<=0.0:
				return 'False'
			else: return 'False'
		elif obj[8]<=1:
			return 'False'
		else: return 'False'
	elif obj[13]<=1:
		# {"feature": "Age", "instances": 24, "metric_value": 0.7383, "depth": 2}
		if obj[4]<=3:
			# {"feature": "Occupation", "instances": 17, "metric_value": 0.874, "depth": 3}
			if obj[7]<=12:
				# {"feature": "Income", "instances": 13, "metric_value": 0.9612, "depth": 4}
				if obj[8]<=6:
					# {"feature": "Time", "instances": 11, "metric_value": 0.994, "depth": 5}
					if obj[1]>0:
						# {"feature": "Coupon", "instances": 9, "metric_value": 0.9183, "depth": 6}
						if obj[2]>0:
							# {"feature": "Coffeehouse", "instances": 8, "metric_value": 0.8113, "depth": 7}
							if obj[10]<=1.0:
								# {"feature": "Bar", "instances": 6, "metric_value": 0.9183, "depth": 8}
								if obj[9]>0.0:
									# {"feature": "Restaurant20to50", "instances": 5, "metric_value": 0.971, "depth": 9}
									if obj[11]<=2.0:
										# {"feature": "Passanger", "instances": 4, "metric_value": 1.0, "depth": 10}
										if obj[0]<=1:
											# {"feature": "Gender", "instances": 2, "metric_value": 1.0, "depth": 11}
											if obj[3]<=1:
												# {"feature": "Children", "instances": 2, "metric_value": 1.0, "depth": 12}
												if obj[5]<=0:
													# {"feature": "Education", "instances": 2, "metric_value": 1.0, "depth": 13}
													if obj[6]<=4:
														# {"feature": "Direction_same", "instances": 2, "metric_value": 1.0, "depth": 14}
														if obj[12]<=1:
															return 'False'
														else: return 'False'
													else: return 'False'
												else: return 'False'
											else: return 'False'
										elif obj[0]>1:
											# {"feature": "Gender", "instances": 2, "metric_value": 1.0, "depth": 11}
											if obj[3]<=1:
												# {"feature": "Children", "instances": 2, "metric_value": 1.0, "depth": 12}
												if obj[5]<=1:
													# {"feature": "Education", "instances": 2, "metric_value": 1.0, "depth": 13}
													if obj[6]<=0:
														# {"feature": "Direction_same", "instances": 2, "metric_value": 1.0, "depth": 14}
														if obj[12]<=0:
															return 'False'
														else: return 'False'
													else: return 'False'
												else: return 'False'
											else: return 'False'
										else: return 'False'
									elif obj[11]>2.0:
										return 'True'
									else: return 'True'
								elif obj[9]<=0.0:
									return 'True'
								else: return 'True'
							elif obj[10]>1.0:
								return 'True'
							else: return 'True'
						elif obj[2]<=0:
							return 'False'
						else: return 'False'
					elif obj[1]<=0:
						return 'False'
					else: return 'False'
				elif obj[8]>6:
					return 'True'
				else: return 'True'
			elif obj[7]>12:
				return 'True'
			else: return 'True'
		elif obj[4]>3:
			return 'True'
		else: return 'True'
	else: return 'True'
