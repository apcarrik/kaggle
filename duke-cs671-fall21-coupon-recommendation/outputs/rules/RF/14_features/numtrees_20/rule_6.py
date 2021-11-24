def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Gender, obj[4]: Age, obj[5]: Children, obj[6]: Education, obj[7]: Occupation, obj[8]: Income, obj[9]: Bar, obj[10]: Coffeehouse, obj[11]: Restaurant20to50, obj[12]: Direction_same, obj[13]: Distance
	# {"feature": "Coupon", "instances": 51, "metric_value": 0.9864, "depth": 1}
	if obj[2]<=3:
		# {"feature": "Coffeehouse", "instances": 32, "metric_value": 0.9887, "depth": 2}
		if obj[10]>0.0:
			# {"feature": "Time", "instances": 22, "metric_value": 0.8454, "depth": 3}
			if obj[1]<=2:
				# {"feature": "Distance", "instances": 14, "metric_value": 0.9852, "depth": 4}
				if obj[13]<=1:
					# {"feature": "Restaurant20to50", "instances": 7, "metric_value": 0.5917, "depth": 5}
					if obj[11]>0.0:
						return 'True'
					elif obj[11]<=0.0:
						return 'False'
					else: return 'False'
				elif obj[13]>1:
					# {"feature": "Age", "instances": 7, "metric_value": 0.8631, "depth": 5}
					if obj[4]>0:
						# {"feature": "Bar", "instances": 5, "metric_value": 0.971, "depth": 6}
						if obj[9]>0.0:
							# {"feature": "Passanger", "instances": 4, "metric_value": 0.8113, "depth": 7}
							if obj[0]<=1:
								# {"feature": "Education", "instances": 3, "metric_value": 0.9183, "depth": 8}
								if obj[6]>0:
									# {"feature": "Gender", "instances": 2, "metric_value": 1.0, "depth": 9}
									if obj[3]<=0:
										# {"feature": "Children", "instances": 2, "metric_value": 1.0, "depth": 10}
										if obj[5]<=0:
											# {"feature": "Occupation", "instances": 2, "metric_value": 1.0, "depth": 11}
											if obj[7]<=7:
												# {"feature": "Income", "instances": 2, "metric_value": 1.0, "depth": 12}
												if obj[8]<=0:
													# {"feature": "Restaurant20to50", "instances": 2, "metric_value": 1.0, "depth": 13}
													if obj[11]<=2.0:
														# {"feature": "Direction_same", "instances": 2, "metric_value": 1.0, "depth": 14}
														if obj[12]<=0:
															return 'True'
														else: return 'True'
													else: return 'True'
												else: return 'True'
											else: return 'True'
										else: return 'True'
									else: return 'True'
								elif obj[6]<=0:
									return 'False'
								else: return 'False'
							elif obj[0]>1:
								return 'False'
							else: return 'False'
						elif obj[9]<=0.0:
							return 'True'
						else: return 'True'
					elif obj[4]<=0:
						return 'False'
					else: return 'False'
				else: return 'False'
			elif obj[1]>2:
				return 'True'
			else: return 'True'
		elif obj[10]<=0.0:
			# {"feature": "Gender", "instances": 10, "metric_value": 0.7219, "depth": 3}
			if obj[3]<=0:
				return 'False'
			elif obj[3]>0:
				# {"feature": "Passanger", "instances": 4, "metric_value": 1.0, "depth": 4}
				if obj[0]<=1:
					# {"feature": "Time", "instances": 3, "metric_value": 0.9183, "depth": 5}
					if obj[1]>0:
						return 'False'
					elif obj[1]<=0:
						return 'True'
					else: return 'True'
				elif obj[0]>1:
					return 'True'
				else: return 'True'
			else: return 'True'
		else: return 'False'
	elif obj[2]>3:
		# {"feature": "Income", "instances": 19, "metric_value": 0.7425, "depth": 2}
		if obj[8]<=6:
			# {"feature": "Age", "instances": 17, "metric_value": 0.5226, "depth": 3}
			if obj[4]>0:
				# {"feature": "Passanger", "instances": 16, "metric_value": 0.3373, "depth": 4}
				if obj[0]<=2:
					return 'False'
				elif obj[0]>2:
					# {"feature": "Time", "instances": 4, "metric_value": 0.8113, "depth": 5}
					if obj[1]<=2:
						return 'False'
					elif obj[1]>2:
						return 'True'
					else: return 'True'
				else: return 'False'
			elif obj[4]<=0:
				return 'True'
			else: return 'True'
		elif obj[8]>6:
			return 'True'
		else: return 'True'
	else: return 'False'
