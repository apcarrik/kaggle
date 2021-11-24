def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Education, obj[4]: Occupation, obj[5]: Bar, obj[6]: Restaurant20to50, obj[7]: Direction_same, obj[8]: Distance
	# {"feature": "Education", "instances": 23, "metric_value": 0.9321, "depth": 1}
	if obj[3]<=1:
		# {"feature": "Distance", "instances": 12, "metric_value": 0.4138, "depth": 2}
		if obj[8]<=2:
			return 'True'
		elif obj[8]>2:
			return 'False'
		else: return 'False'
	elif obj[3]>1:
		# {"feature": "Coupon", "instances": 11, "metric_value": 0.9457, "depth": 2}
		if obj[2]<=3:
			# {"feature": "Passanger", "instances": 8, "metric_value": 1.0, "depth": 3}
			if obj[0]>0:
				# {"feature": "Time", "instances": 7, "metric_value": 0.9852, "depth": 4}
				if obj[1]>1:
					# {"feature": "Occupation", "instances": 5, "metric_value": 0.971, "depth": 5}
					if obj[4]>7:
						# {"feature": "Bar", "instances": 3, "metric_value": 0.9183, "depth": 6}
						if obj[5]>0.0:
							# {"feature": "Restaurant20to50", "instances": 2, "metric_value": 1.0, "depth": 7}
							if obj[6]<=0.0:
								return 'True'
							elif obj[6]>0.0:
								return 'False'
							else: return 'False'
						elif obj[5]<=0.0:
							return 'True'
						else: return 'True'
					elif obj[4]<=7:
						return 'False'
					else: return 'False'
				elif obj[1]<=1:
					return 'True'
				else: return 'True'
			elif obj[0]<=0:
				return 'False'
			else: return 'False'
		elif obj[2]>3:
			return 'False'
		else: return 'False'
	else: return 'False'
