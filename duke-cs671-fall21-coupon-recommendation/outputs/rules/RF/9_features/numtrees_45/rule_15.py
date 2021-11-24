def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Education, obj[4]: Occupation, obj[5]: Bar, obj[6]: Restaurant20to50, obj[7]: Direction_same, obj[8]: Distance
	# {"feature": "Occupation", "instances": 23, "metric_value": 0.6666, "depth": 1}
	if obj[4]>5:
		return 'True'
	elif obj[4]<=5:
		# {"feature": "Time", "instances": 10, "metric_value": 0.971, "depth": 2}
		if obj[1]<=3:
			# {"feature": "Passanger", "instances": 8, "metric_value": 0.8113, "depth": 3}
			if obj[0]>1:
				return 'True'
			elif obj[0]<=1:
				# {"feature": "Coupon", "instances": 4, "metric_value": 1.0, "depth": 4}
				if obj[2]>2:
					# {"feature": "Education", "instances": 3, "metric_value": 0.9183, "depth": 5}
					if obj[3]>0:
						return 'True'
					elif obj[3]<=0:
						return 'False'
					else: return 'False'
				elif obj[2]<=2:
					return 'False'
				else: return 'False'
			else: return 'True'
		elif obj[1]>3:
			return 'False'
		else: return 'False'
	else: return 'True'
