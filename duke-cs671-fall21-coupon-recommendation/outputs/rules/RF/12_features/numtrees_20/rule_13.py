def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Gender, obj[4]: Age, obj[5]: Education, obj[6]: Occupation, obj[7]: Bar, obj[8]: Coffeehouse, obj[9]: Restaurant20to50, obj[10]: Direction_same, obj[11]: Distance
	# {"feature": "Direction_same", "instances": 51, "metric_value": 0.9367, "depth": 1}
	if obj[10]<=0:
		# {"feature": "Coffeehouse", "instances": 45, "metric_value": 0.8673, "depth": 2}
		if obj[8]<=3.0:
			# {"feature": "Restaurant20to50", "instances": 39, "metric_value": 0.9183, "depth": 3}
			if obj[9]<=2.0:
				# {"feature": "Coupon", "instances": 37, "metric_value": 0.878, "depth": 4}
				if obj[2]>1:
					# {"feature": "Occupation", "instances": 28, "metric_value": 0.7496, "depth": 5}
					if obj[6]>0:
						# {"feature": "Bar", "instances": 27, "metric_value": 0.6913, "depth": 6}
						if obj[7]<=2.0:
							# {"feature": "Education", "instances": 26, "metric_value": 0.6194, "depth": 7}
							if obj[5]>1:
								# {"feature": "Time", "instances": 14, "metric_value": 0.8631, "depth": 8}
								if obj[1]>0:
									# {"feature": "Age", "instances": 8, "metric_value": 0.5436, "depth": 9}
									if obj[4]<=4:
										return 'True'
									elif obj[4]>4:
										# {"feature": "Passanger", "instances": 2, "metric_value": 1.0, "depth": 10}
										if obj[0]>2:
											return 'True'
										elif obj[0]<=2:
											return 'False'
										else: return 'False'
									else: return 'True'
								elif obj[1]<=0:
									# {"feature": "Age", "instances": 6, "metric_value": 1.0, "depth": 9}
									if obj[4]<=2:
										# {"feature": "Passanger", "instances": 4, "metric_value": 0.8113, "depth": 10}
										if obj[0]<=1:
											# {"feature": "Gender", "instances": 2, "metric_value": 1.0, "depth": 11}
											if obj[3]<=0:
												# {"feature": "Distance", "instances": 2, "metric_value": 1.0, "depth": 12}
												if obj[11]<=2:
													return 'True'
												else: return 'True'
											else: return 'True'
										elif obj[0]>1:
											return 'False'
										else: return 'False'
									elif obj[4]>2:
										return 'True'
									else: return 'True'
								else: return 'True'
							elif obj[5]<=1:
								return 'True'
							else: return 'True'
						elif obj[7]>2.0:
							return 'False'
						else: return 'False'
					elif obj[6]<=0:
						return 'False'
					else: return 'False'
				elif obj[2]<=1:
					# {"feature": "Bar", "instances": 9, "metric_value": 0.9911, "depth": 5}
					if obj[7]>0.0:
						# {"feature": "Time", "instances": 6, "metric_value": 0.9183, "depth": 6}
						if obj[1]>0:
							return 'True'
						elif obj[1]<=0:
							return 'False'
						else: return 'False'
					elif obj[7]<=0.0:
						return 'False'
					else: return 'False'
				else: return 'False'
			elif obj[9]>2.0:
				return 'False'
			else: return 'False'
		elif obj[8]>3.0:
			return 'True'
		else: return 'True'
	elif obj[10]>0:
		# {"feature": "Age", "instances": 6, "metric_value": 0.65, "depth": 2}
		if obj[4]<=3:
			return 'False'
		elif obj[4]>3:
			# {"feature": "Occupation", "instances": 2, "metric_value": 1.0, "depth": 3}
			if obj[6]>8:
				return 'False'
			elif obj[6]<=8:
				return 'True'
			else: return 'True'
		else: return 'False'
	else: return 'False'
