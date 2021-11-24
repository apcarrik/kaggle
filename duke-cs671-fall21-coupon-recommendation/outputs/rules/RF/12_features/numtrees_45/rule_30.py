def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Gender, obj[4]: Age, obj[5]: Education, obj[6]: Occupation, obj[7]: Bar, obj[8]: Coffeehouse, obj[9]: Restaurant20to50, obj[10]: Direction_same, obj[11]: Distance
	# {"feature": "Passanger", "instances": 23, "metric_value": 0.9877, "depth": 1}
	if obj[0]<=2:
		# {"feature": "Coupon", "instances": 19, "metric_value": 0.998, "depth": 2}
		if obj[2]>0:
			# {"feature": "Occupation", "instances": 17, "metric_value": 0.9975, "depth": 3}
			if obj[6]>2:
				# {"feature": "Bar", "instances": 14, "metric_value": 0.9852, "depth": 4}
				if obj[7]<=2.0:
					# {"feature": "Restaurant20to50", "instances": 12, "metric_value": 1.0, "depth": 5}
					if obj[9]<=1.0:
						# {"feature": "Time", "instances": 10, "metric_value": 0.971, "depth": 6}
						if obj[1]<=3:
							# {"feature": "Coffeehouse", "instances": 9, "metric_value": 0.9183, "depth": 7}
							if obj[8]<=2.0:
								# {"feature": "Age", "instances": 8, "metric_value": 0.8113, "depth": 8}
								if obj[4]<=3:
									# {"feature": "Distance", "instances": 5, "metric_value": 0.971, "depth": 9}
									if obj[11]>1:
										# {"feature": "Gender", "instances": 4, "metric_value": 0.8113, "depth": 10}
										if obj[3]<=0:
											# {"feature": "Education", "instances": 2, "metric_value": 1.0, "depth": 11}
											if obj[5]<=0:
												# {"feature": "Direction_same", "instances": 2, "metric_value": 1.0, "depth": 12}
												if obj[10]<=0:
													return 'False'
												else: return 'False'
											else: return 'False'
										elif obj[3]>0:
											return 'False'
										else: return 'False'
									elif obj[11]<=1:
										return 'True'
									else: return 'True'
								elif obj[4]>3:
									return 'False'
								else: return 'False'
							elif obj[8]>2.0:
								return 'True'
							else: return 'True'
						elif obj[1]>3:
							return 'True'
						else: return 'True'
					elif obj[9]>1.0:
						return 'True'
					else: return 'True'
				elif obj[7]>2.0:
					return 'False'
				else: return 'False'
			elif obj[6]<=2:
				return 'True'
			else: return 'True'
		elif obj[2]<=0:
			return 'False'
		else: return 'False'
	elif obj[0]>2:
		return 'True'
	else: return 'True'
