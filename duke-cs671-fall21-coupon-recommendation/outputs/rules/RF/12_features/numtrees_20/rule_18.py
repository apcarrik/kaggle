def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Gender, obj[4]: Age, obj[5]: Education, obj[6]: Occupation, obj[7]: Bar, obj[8]: Coffeehouse, obj[9]: Restaurant20to50, obj[10]: Direction_same, obj[11]: Distance
	# {"feature": "Occupation", "instances": 51, "metric_value": 0.9183, "depth": 1}
	if obj[6]<=10:
		# {"feature": "Bar", "instances": 33, "metric_value": 0.7455, "depth": 2}
		if obj[7]<=3.0:
			# {"feature": "Restaurant20to50", "instances": 32, "metric_value": 0.6962, "depth": 3}
			if obj[9]<=1.0:
				# {"feature": "Education", "instances": 24, "metric_value": 0.8113, "depth": 4}
				if obj[5]<=2:
					# {"feature": "Coupon", "instances": 18, "metric_value": 0.9183, "depth": 5}
					if obj[2]>0:
						# {"feature": "Time", "instances": 16, "metric_value": 0.8113, "depth": 6}
						if obj[1]>0:
							# {"feature": "Coffeehouse", "instances": 9, "metric_value": 0.9911, "depth": 7}
							if obj[8]>1.0:
								# {"feature": "Age", "instances": 5, "metric_value": 0.7219, "depth": 8}
								if obj[4]>0:
									return 'True'
								elif obj[4]<=0:
									return 'False'
								else: return 'False'
							elif obj[8]<=1.0:
								# {"feature": "Direction_same", "instances": 4, "metric_value": 0.8113, "depth": 8}
								if obj[10]<=0:
									return 'False'
								elif obj[10]>0:
									# {"feature": "Passanger", "instances": 2, "metric_value": 1.0, "depth": 9}
									if obj[0]<=1:
										# {"feature": "Gender", "instances": 2, "metric_value": 1.0, "depth": 10}
										if obj[3]<=0:
											# {"feature": "Age", "instances": 2, "metric_value": 1.0, "depth": 11}
											if obj[4]<=4:
												# {"feature": "Distance", "instances": 2, "metric_value": 1.0, "depth": 12}
												if obj[11]<=2:
													return 'False'
												else: return 'False'
											else: return 'False'
										else: return 'False'
									else: return 'False'
								else: return 'False'
							else: return 'False'
						elif obj[1]<=0:
							return 'True'
						else: return 'True'
					elif obj[2]<=0:
						return 'False'
					else: return 'False'
				elif obj[5]>2:
					return 'True'
				else: return 'True'
			elif obj[9]>1.0:
				return 'True'
			else: return 'True'
		elif obj[7]>3.0:
			return 'False'
		else: return 'False'
	elif obj[6]>10:
		# {"feature": "Age", "instances": 18, "metric_value": 0.9911, "depth": 2}
		if obj[4]<=4:
			# {"feature": "Bar", "instances": 15, "metric_value": 0.9183, "depth": 3}
			if obj[7]>0.0:
				# {"feature": "Passanger", "instances": 9, "metric_value": 0.5033, "depth": 4}
				if obj[0]>0:
					return 'False'
				elif obj[0]<=0:
					return 'True'
				else: return 'True'
			elif obj[7]<=0.0:
				# {"feature": "Coffeehouse", "instances": 6, "metric_value": 0.9183, "depth": 4}
				if obj[8]>0.0:
					return 'True'
				elif obj[8]<=0.0:
					return 'False'
				else: return 'False'
			else: return 'True'
		elif obj[4]>4:
			return 'True'
		else: return 'True'
	else: return 'False'
