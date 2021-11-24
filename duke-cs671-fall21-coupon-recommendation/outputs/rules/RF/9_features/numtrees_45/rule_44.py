def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Education, obj[4]: Occupation, obj[5]: Bar, obj[6]: Restaurant20to50, obj[7]: Direction_same, obj[8]: Distance
	# {"feature": "Occupation", "instances": 23, "metric_value": 0.9321, "depth": 1}
	if obj[4]<=14:
		# {"feature": "Education", "instances": 20, "metric_value": 0.8113, "depth": 2}
		if obj[3]>0:
			# {"feature": "Coupon", "instances": 14, "metric_value": 0.9403, "depth": 3}
			if obj[2]>0:
				# {"feature": "Time", "instances": 10, "metric_value": 0.7219, "depth": 4}
				if obj[1]<=1:
					return 'True'
				elif obj[1]>1:
					# {"feature": "Restaurant20to50", "instances": 4, "metric_value": 1.0, "depth": 5}
					if obj[6]<=1.0:
						return 'False'
					elif obj[6]>1.0:
						return 'True'
					else: return 'True'
				else: return 'False'
			elif obj[2]<=0:
				# {"feature": "Restaurant20to50", "instances": 4, "metric_value": 0.8113, "depth": 4}
				if obj[6]>0.0:
					return 'False'
				elif obj[6]<=0.0:
					return 'True'
				else: return 'True'
			else: return 'False'
		elif obj[3]<=0:
			return 'True'
		else: return 'True'
	elif obj[4]>14:
		return 'False'
	else: return 'False'
