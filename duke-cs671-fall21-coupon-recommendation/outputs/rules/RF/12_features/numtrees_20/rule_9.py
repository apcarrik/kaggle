def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Gender, obj[4]: Age, obj[5]: Education, obj[6]: Occupation, obj[7]: Bar, obj[8]: Coffeehouse, obj[9]: Restaurant20to50, obj[10]: Direction_same, obj[11]: Distance
	# {"feature": "Passanger", "instances": 51, "metric_value": 0.9931, "depth": 1}
	if obj[0]<=2:
		# {"feature": "Restaurant20to50", "instances": 35, "metric_value": 0.9852, "depth": 2}
		if obj[9]<=3.0:
			# {"feature": "Coffeehouse", "instances": 33, "metric_value": 0.9673, "depth": 3}
			if obj[8]<=2.0:
				# {"feature": "Time", "instances": 26, "metric_value": 0.8905, "depth": 4}
				if obj[1]<=1:
					# {"feature": "Occupation", "instances": 18, "metric_value": 0.9911, "depth": 5}
					if obj[6]<=12:
						# {"feature": "Bar", "instances": 16, "metric_value": 0.9544, "depth": 6}
						if obj[7]<=0.0:
							# {"feature": "Age", "instances": 12, "metric_value": 1.0, "depth": 7}
							if obj[4]<=4:
								# {"feature": "Distance", "instances": 10, "metric_value": 0.971, "depth": 8}
								if obj[11]>1:
									# {"feature": "Coupon", "instances": 8, "metric_value": 1.0, "depth": 9}
									if obj[2]>0:
										# {"feature": "Education", "instances": 6, "metric_value": 0.9183, "depth": 10}
										if obj[5]<=3:
											# {"feature": "Gender", "instances": 5, "metric_value": 0.7219, "depth": 11}
											if obj[3]>0:
												# {"feature": "Direction_same", "instances": 3, "metric_value": 0.9183, "depth": 12}
												if obj[10]<=0:
													return 'True'
												else: return 'True'
											elif obj[3]<=0:
												return 'True'
											else: return 'True'
										elif obj[5]>3:
											return 'False'
										else: return 'False'
									elif obj[2]<=0:
										return 'False'
									else: return 'False'
								elif obj[11]<=1:
									return 'True'
								else: return 'True'
							elif obj[4]>4:
								return 'False'
							else: return 'False'
						elif obj[7]>0.0:
							return 'False'
						else: return 'False'
					elif obj[6]>12:
						return 'True'
					else: return 'True'
				elif obj[1]>1:
					return 'False'
				else: return 'False'
			elif obj[8]>2.0:
				# {"feature": "Bar", "instances": 7, "metric_value": 0.8631, "depth": 4}
				if obj[7]>0.0:
					return 'True'
				elif obj[7]<=0.0:
					return 'False'
				else: return 'False'
			else: return 'True'
		elif obj[9]>3.0:
			return 'True'
		else: return 'True'
	elif obj[0]>2:
		# {"feature": "Coffeehouse", "instances": 16, "metric_value": 0.6962, "depth": 2}
		if obj[8]<=3.0:
			# {"feature": "Occupation", "instances": 13, "metric_value": 0.3912, "depth": 3}
			if obj[6]<=10:
				return 'True'
			elif obj[6]>10:
				return 'False'
			else: return 'False'
		elif obj[8]>3.0:
			# {"feature": "Age", "instances": 3, "metric_value": 0.9183, "depth": 3}
			if obj[4]<=3:
				return 'False'
			elif obj[4]>3:
				return 'True'
			else: return 'True'
		else: return 'False'
	else: return 'True'
