def findDecision(obj): #obj[0]: Passanger, obj[1]: Coupon, obj[2]: Education, obj[3]: Occupation, obj[4]: Bar, obj[5]: Restaurant20to50, obj[6]: Direction_same, obj[7]: Distance
	# {"feature": "Passanger", "instances": 23, "metric_value": 0.8865, "depth": 1}
	if obj[0]>0:
		# {"feature": "Occupation", "instances": 21, "metric_value": 0.7919, "depth": 2}
		if obj[3]<=20:
			# {"feature": "Bar", "instances": 19, "metric_value": 0.6292, "depth": 3}
			if obj[4]>0.0:
				# {"feature": "Coupon", "instances": 10, "metric_value": 0.8813, "depth": 4}
				if obj[1]<=3:
					# {"feature": "Education", "instances": 8, "metric_value": 0.5436, "depth": 5}
					if obj[2]>0:
						return 'True'
					elif obj[2]<=0:
						# {"feature": "Distance", "instances": 2, "metric_value": 1.0, "depth": 6}
						if obj[7]>1:
							return 'True'
						elif obj[7]<=1:
							return 'False'
						else: return 'False'
					else: return 'True'
				elif obj[1]>3:
					return 'False'
				else: return 'False'
			elif obj[4]<=0.0:
				return 'True'
			else: return 'True'
		elif obj[3]>20:
			return 'False'
		else: return 'False'
	elif obj[0]<=0:
		return 'False'
	else: return 'False'
