def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Education, obj[4]: Occupation, obj[5]: Bar, obj[6]: Coffeehouse, obj[7]: Restaurant20to50, obj[8]: Direction_same, obj[9]: Distance
	# {"feature": "Coupon", "instances": 51, "metric_value": 0.9864, "depth": 1}
	if obj[2]>1:
		# {"feature": "Occupation", "instances": 41, "metric_value": 0.9262, "depth": 2}
		if obj[4]>4:
			# {"feature": "Coffeehouse", "instances": 28, "metric_value": 0.9963, "depth": 3}
			if obj[6]>1.0:
				# {"feature": "Time", "instances": 15, "metric_value": 0.8366, "depth": 4}
				if obj[1]<=1:
					# {"feature": "Education", "instances": 9, "metric_value": 0.9911, "depth": 5}
					if obj[3]<=2:
						# {"feature": "Passanger", "instances": 6, "metric_value": 0.65, "depth": 6}
						if obj[0]>0:
							return 'True'
						elif obj[0]<=0:
							return 'False'
						else: return 'False'
					elif obj[3]>2:
						return 'False'
					else: return 'False'
				elif obj[1]>1:
					return 'True'
				else: return 'True'
			elif obj[6]<=1.0:
				# {"feature": "Time", "instances": 13, "metric_value": 0.8905, "depth": 4}
				if obj[1]<=2:
					# {"feature": "Education", "instances": 10, "metric_value": 0.971, "depth": 5}
					if obj[3]<=2:
						# {"feature": "Direction_same", "instances": 7, "metric_value": 0.9852, "depth": 6}
						if obj[8]<=0:
							# {"feature": "Passanger", "instances": 6, "metric_value": 0.9183, "depth": 7}
							if obj[0]<=1:
								# {"feature": "Bar", "instances": 5, "metric_value": 0.971, "depth": 8}
								if obj[5]<=0.0:
									# {"feature": "Restaurant20to50", "instances": 4, "metric_value": 1.0, "depth": 9}
									if obj[7]>0.0:
										# {"feature": "Distance", "instances": 3, "metric_value": 0.9183, "depth": 10}
										if obj[9]<=1:
											return 'False'
										elif obj[9]>1:
											return 'False'
										else: return 'False'
									elif obj[7]<=0.0:
										return 'True'
									else: return 'True'
								elif obj[5]>0.0:
									return 'True'
								else: return 'True'
							elif obj[0]>1:
								return 'True'
							else: return 'True'
						elif obj[8]>0:
							return 'False'
						else: return 'False'
					elif obj[3]>2:
						return 'False'
					else: return 'False'
				elif obj[1]>2:
					return 'False'
				else: return 'False'
			else: return 'False'
		elif obj[4]<=4:
			# {"feature": "Restaurant20to50", "instances": 13, "metric_value": 0.3912, "depth": 3}
			if obj[7]>0.0:
				return 'True'
			elif obj[7]<=0.0:
				# {"feature": "Time", "instances": 3, "metric_value": 0.9183, "depth": 4}
				if obj[1]<=0:
					return 'True'
				elif obj[1]>0:
					return 'False'
				else: return 'False'
			else: return 'True'
		else: return 'True'
	elif obj[2]<=1:
		# {"feature": "Direction_same", "instances": 10, "metric_value": 0.7219, "depth": 2}
		if obj[8]<=0:
			return 'False'
		elif obj[8]>0:
			# {"feature": "Education", "instances": 3, "metric_value": 0.9183, "depth": 3}
			if obj[3]>2:
				return 'True'
			elif obj[3]<=2:
				return 'False'
			else: return 'False'
		else: return 'True'
	else: return 'False'
