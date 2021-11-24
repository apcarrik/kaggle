def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Age, obj[4]: Education, obj[5]: Occupation, obj[6]: Bar, obj[7]: Coffeehouse, obj[8]: Restaurant20to50, obj[9]: Direction_same, obj[10]: Distance
	# {"feature": "Education", "instances": 23, "metric_value": 0.8281, "depth": 1}
	if obj[4]>1:
		# {"feature": "Time", "instances": 13, "metric_value": 0.9957, "depth": 2}
		if obj[1]>0:
			# {"feature": "Coupon", "instances": 10, "metric_value": 0.971, "depth": 3}
			if obj[2]<=3:
				# {"feature": "Coffeehouse", "instances": 6, "metric_value": 0.9183, "depth": 4}
				if obj[7]<=2.0:
					return 'True'
				elif obj[7]>2.0:
					return 'False'
				else: return 'False'
			elif obj[2]>3:
				return 'False'
			else: return 'False'
		elif obj[1]<=0:
			return 'True'
		else: return 'True'
	elif obj[4]<=1:
		return 'True'
	else: return 'True'
