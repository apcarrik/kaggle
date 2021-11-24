def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Education, obj[4]: Occupation, obj[5]: Bar, obj[6]: Coffeehouse, obj[7]: Restaurant20to50, obj[8]: Direction_same, obj[9]: Distance
	# {"feature": "Education", "instances": 51, "metric_value": 0.9931, "depth": 1}
	if obj[3]>0:
		# {"feature": "Coupon", "instances": 35, "metric_value": 0.9947, "depth": 2}
		if obj[2]>1:
			# {"feature": "Coffeehouse", "instances": 27, "metric_value": 0.9911, "depth": 3}
			if obj[6]<=3.0:
				# {"feature": "Occupation", "instances": 23, "metric_value": 0.9321, "depth": 4}
				if obj[4]>2:
					# {"feature": "Restaurant20to50", "instances": 19, "metric_value": 0.9819, "depth": 5}
					if obj[7]>0.0:
						# {"feature": "Time", "instances": 17, "metric_value": 0.9975, "depth": 6}
						if obj[1]<=3:
							# {"feature": "Direction_same", "instances": 16, "metric_value": 1.0, "depth": 7}
							if obj[8]<=0:
								# {"feature": "Bar", "instances": 12, "metric_value": 0.9799, "depth": 8}
								if obj[5]<=2.0:
									# {"feature": "Distance", "instances": 11, "metric_value": 0.9457, "depth": 9}
									if obj[9]<=2:
										# {"feature": "Passanger", "instances": 9, "metric_value": 0.9911, "depth": 10}
										if obj[0]<=2:
											return 'True'
										elif obj[0]>2:
											return 'False'
										else: return 'False'
									elif obj[9]>2:
										return 'False'
									else: return 'False'
								elif obj[5]>2.0:
									return 'True'
								else: return 'True'
							elif obj[8]>0:
								# {"feature": "Bar", "instances": 4, "metric_value": 0.8113, "depth": 8}
								if obj[5]<=2.0:
									return 'True'
								elif obj[5]>2.0:
									return 'False'
								else: return 'False'
							else: return 'True'
						elif obj[1]>3:
							return 'True'
						else: return 'True'
					elif obj[7]<=0.0:
						return 'True'
					else: return 'True'
				elif obj[4]<=2:
					return 'True'
				else: return 'True'
			elif obj[6]>3.0:
				return 'False'
			else: return 'False'
		elif obj[2]<=1:
			# {"feature": "Passanger", "instances": 8, "metric_value": 0.5436, "depth": 3}
			if obj[0]<=1:
				return 'False'
			elif obj[0]>1:
				return 'True'
			else: return 'True'
		else: return 'False'
	elif obj[3]<=0:
		# {"feature": "Time", "instances": 16, "metric_value": 0.8113, "depth": 2}
		if obj[1]<=3:
			# {"feature": "Occupation", "instances": 12, "metric_value": 0.4138, "depth": 3}
			if obj[4]<=10:
				return 'True'
			elif obj[4]>10:
				return 'False'
			else: return 'False'
		elif obj[1]>3:
			# {"feature": "Passanger", "instances": 4, "metric_value": 0.8113, "depth": 3}
			if obj[0]>1:
				return 'False'
			elif obj[0]<=1:
				# {"feature": "Coffeehouse", "instances": 2, "metric_value": 1.0, "depth": 4}
				if obj[6]<=0.0:
					return 'False'
				elif obj[6]>0.0:
					return 'True'
				else: return 'True'
			else: return 'False'
		else: return 'False'
	else: return 'True'
