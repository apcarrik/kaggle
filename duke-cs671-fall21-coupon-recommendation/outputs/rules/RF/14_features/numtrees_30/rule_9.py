def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Gender, obj[4]: Age, obj[5]: Children, obj[6]: Education, obj[7]: Occupation, obj[8]: Income, obj[9]: Bar, obj[10]: Coffeehouse, obj[11]: Restaurant20to50, obj[12]: Direction_same, obj[13]: Distance
	# {"feature": "Income", "instances": 34, "metric_value": 0.9774, "depth": 1}
	if obj[8]<=5:
		# {"feature": "Education", "instances": 22, "metric_value": 0.994, "depth": 2}
		if obj[6]<=3:
			# {"feature": "Occupation", "instances": 19, "metric_value": 0.9495, "depth": 3}
			if obj[7]>2:
				# {"feature": "Age", "instances": 17, "metric_value": 0.9774, "depth": 4}
				if obj[4]<=5:
					# {"feature": "Restaurant20to50", "instances": 15, "metric_value": 0.9183, "depth": 5}
					if obj[11]>0.0:
						# {"feature": "Coffeehouse", "instances": 12, "metric_value": 0.9799, "depth": 6}
						if obj[10]>0.0:
							# {"feature": "Coupon", "instances": 10, "metric_value": 0.8813, "depth": 7}
							if obj[2]>2:
								# {"feature": "Bar", "instances": 6, "metric_value": 0.65, "depth": 8}
								if obj[9]<=2.0:
									return 'False'
								elif obj[9]>2.0:
									# {"feature": "Passanger", "instances": 2, "metric_value": 1.0, "depth": 9}
									if obj[0]<=1:
										return 'False'
									elif obj[0]>1:
										return 'True'
									else: return 'True'
								else: return 'False'
							elif obj[2]<=2:
								# {"feature": "Time", "instances": 4, "metric_value": 1.0, "depth": 8}
								if obj[1]<=3:
									# {"feature": "Passanger", "instances": 3, "metric_value": 0.9183, "depth": 9}
									if obj[0]>0:
										# {"feature": "Gender", "instances": 2, "metric_value": 1.0, "depth": 10}
										if obj[3]<=1:
											# {"feature": "Children", "instances": 2, "metric_value": 1.0, "depth": 11}
											if obj[5]<=1:
												# {"feature": "Bar", "instances": 2, "metric_value": 1.0, "depth": 12}
												if obj[9]<=0.0:
													# {"feature": "Direction_same", "instances": 2, "metric_value": 1.0, "depth": 13}
													if obj[12]<=0:
														# {"feature": "Distance", "instances": 2, "metric_value": 1.0, "depth": 14}
														if obj[13]<=3:
															return 'True'
														else: return 'True'
													else: return 'True'
												else: return 'True'
											else: return 'True'
										else: return 'True'
									elif obj[0]<=0:
										return 'False'
									else: return 'False'
								elif obj[1]>3:
									return 'True'
								else: return 'True'
							else: return 'True'
						elif obj[10]<=0.0:
							return 'True'
						else: return 'True'
					elif obj[11]<=0.0:
						return 'False'
					else: return 'False'
				elif obj[4]>5:
					return 'True'
				else: return 'True'
			elif obj[7]<=2:
				return 'False'
			else: return 'False'
		elif obj[6]>3:
			return 'True'
		else: return 'True'
	elif obj[8]>5:
		# {"feature": "Occupation", "instances": 12, "metric_value": 0.65, "depth": 2}
		if obj[7]<=8:
			return 'True'
		elif obj[7]>8:
			# {"feature": "Age", "instances": 4, "metric_value": 1.0, "depth": 3}
			if obj[4]>3:
				return 'True'
			elif obj[4]<=3:
				return 'False'
			else: return 'False'
		else: return 'True'
	else: return 'True'
