def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Gender, obj[4]: Age, obj[5]: Children, obj[6]: Education, obj[7]: Occupation, obj[8]: Bar, obj[9]: Coffeehouse, obj[10]: Restaurant20to50, obj[11]: Direction_same, obj[12]: Distance
	# {"feature": "Coupon", "instances": 23, "metric_value": 0.9321, "depth": 1}
	if obj[2]>1:
		# {"feature": "Time", "instances": 15, "metric_value": 0.5665, "depth": 2}
		if obj[1]>0:
			return 'True'
		elif obj[1]<=0:
			# {"feature": "Coffeehouse", "instances": 4, "metric_value": 1.0, "depth": 3}
			if obj[9]<=0.0:
				return 'False'
			elif obj[9]>0.0:
				return 'True'
			else: return 'True'
		else: return 'False'
	elif obj[2]<=1:
		# {"feature": "Time", "instances": 8, "metric_value": 0.8113, "depth": 2}
		if obj[1]>0:
			return 'False'
		elif obj[1]<=0:
			# {"feature": "Education", "instances": 3, "metric_value": 0.9183, "depth": 3}
			if obj[6]>0:
				return 'True'
			elif obj[6]<=0:
				return 'False'
			else: return 'False'
		else: return 'True'
	else: return 'False'
