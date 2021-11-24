def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Gender, obj[4]: Age, obj[5]: Children, obj[6]: Education, obj[7]: Occupation, obj[8]: Income, obj[9]: Bar, obj[10]: Coffeehouse, obj[11]: Restaurant20to50, obj[12]: Direction_same, obj[13]: Distance
	# {"feature": "Education", "instances": 34, "metric_value": 0.99, "depth": 1}
	if obj[6]<=3:
		# {"feature": "Coupon", "instances": 31, "metric_value": 0.9629, "depth": 2}
		if obj[2]>1:
			# {"feature": "Occupation", "instances": 24, "metric_value": 1.0, "depth": 3}
			if obj[7]>1:
				# {"feature": "Age", "instances": 21, "metric_value": 0.9852, "depth": 4}
				if obj[4]>1:
					# {"feature": "Coffeehouse", "instances": 16, "metric_value": 0.9887, "depth": 5}
					if obj[10]>0.0:
						# {"feature": "Passanger", "instances": 12, "metric_value": 0.8113, "depth": 6}
						if obj[0]>0:
							# {"feature": "Income", "instances": 11, "metric_value": 0.684, "depth": 7}
							if obj[8]>3:
								# {"feature": "Time", "instances": 8, "metric_value": 0.8113, "depth": 8}
								if obj[1]<=3:
									# {"feature": "Gender", "instances": 6, "metric_value": 0.65, "depth": 9}
									if obj[3]<=0:
										return 'True'
									elif obj[3]>0:
										# {"feature": "Bar", "instances": 3, "metric_value": 0.9183, "depth": 10}
										if obj[9]<=0.0:
											return 'True'
										elif obj[9]>0.0:
											return 'False'
										else: return 'False'
									else: return 'True'
								elif obj[1]>3:
									# {"feature": "Gender", "instances": 2, "metric_value": 1.0, "depth": 9}
									if obj[3]<=0:
										# {"feature": "Children", "instances": 2, "metric_value": 1.0, "depth": 10}
										if obj[5]<=1:
											# {"feature": "Bar", "instances": 2, "metric_value": 1.0, "depth": 11}
											if obj[9]<=0.0:
												# {"feature": "Restaurant20to50", "instances": 2, "metric_value": 1.0, "depth": 12}
												if obj[11]<=1.0:
													# {"feature": "Direction_same", "instances": 2, "metric_value": 1.0, "depth": 13}
													if obj[12]<=0:
														# {"feature": "Distance", "instances": 2, "metric_value": 1.0, "depth": 14}
														if obj[13]<=2:
															return 'False'
														else: return 'False'
													else: return 'False'
												else: return 'False'
											else: return 'False'
										else: return 'False'
									else: return 'False'
								else: return 'False'
							elif obj[8]<=3:
								return 'True'
							else: return 'True'
						elif obj[0]<=0:
							return 'False'
						else: return 'False'
					elif obj[10]<=0.0:
						return 'False'
					else: return 'False'
				elif obj[4]<=1:
					return 'False'
				else: return 'False'
			elif obj[7]<=1:
				return 'True'
			else: return 'True'
		elif obj[2]<=1:
			return 'False'
		else: return 'False'
	elif obj[6]>3:
		return 'True'
	else: return 'True'
