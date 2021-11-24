def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Gender, obj[4]: Age, obj[5]: Education, obj[6]: Occupation, obj[7]: Bar, obj[8]: Coffeehouse, obj[9]: Restaurant20to50, obj[10]: Direction_same, obj[11]: Distance
	# {"feature": "Passanger", "instances": 23, "metric_value": 0.9656, "depth": 1}
	if obj[0]<=2:
		# {"feature": "Time", "instances": 14, "metric_value": 0.9403, "depth": 2}
		if obj[1]<=3:
			# {"feature": "Occupation", "instances": 11, "metric_value": 0.684, "depth": 3}
			if obj[6]<=11:
				return 'False'
			elif obj[6]>11:
				# {"feature": "Age", "instances": 4, "metric_value": 1.0, "depth": 4}
				if obj[4]>0:
					return 'True'
				elif obj[4]<=0:
					return 'False'
				else: return 'False'
			else: return 'True'
		elif obj[1]>3:
			return 'True'
		else: return 'True'
	elif obj[0]>2:
		return 'True'
	else: return 'True'
