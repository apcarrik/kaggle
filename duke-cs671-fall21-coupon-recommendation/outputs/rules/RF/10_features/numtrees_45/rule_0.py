def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Education, obj[4]: Occupation, obj[5]: Bar, obj[6]: Coffeehouse, obj[7]: Restaurant20to50, obj[8]: Direction_same, obj[9]: Distance
	# {"feature": "Education", "instances": 23, "metric_value": 0.9877, "depth": 1}
	if obj[3]>1:
		# {"feature": "Coupon", "instances": 12, "metric_value": 0.65, "depth": 2}
		if obj[2]>1:
			return 'True'
		elif obj[2]<=1:
			return 'False'
		else: return 'False'
	elif obj[3]<=1:
		# {"feature": "Occupation", "instances": 11, "metric_value": 0.8454, "depth": 2}
		if obj[4]>7:
			return 'False'
		elif obj[4]<=7:
			# {"feature": "Time", "instances": 5, "metric_value": 0.971, "depth": 3}
			if obj[1]<=1:
				# {"feature": "Passanger", "instances": 3, "metric_value": 0.9183, "depth": 4}
				if obj[0]>0:
					return 'False'
				elif obj[0]<=0:
					return 'True'
				else: return 'True'
			elif obj[1]>1:
				return 'True'
			else: return 'True'
		else: return 'True'
	else: return 'False'
