def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Gender, obj[4]: Age, obj[5]: Education, obj[6]: Occupation, obj[7]: Bar, obj[8]: Coffeehouse, obj[9]: Restaurant20to50, obj[10]: Direction_same, obj[11]: Distance
	# {"feature": "Restaurant20to50", "instances": 23, "metric_value": 0.9877, "depth": 1}
	if obj[9]<=1.0:
		# {"feature": "Education", "instances": 13, "metric_value": 0.8905, "depth": 2}
		if obj[5]>0:
			# {"feature": "Age", "instances": 10, "metric_value": 0.469, "depth": 3}
			if obj[4]<=4:
				return 'False'
			elif obj[4]>4:
				return 'True'
			else: return 'True'
		elif obj[5]<=0:
			return 'True'
		else: return 'True'
	elif obj[9]>1.0:
		# {"feature": "Passanger", "instances": 10, "metric_value": 0.469, "depth": 2}
		if obj[0]<=1:
			return 'True'
		elif obj[0]>1:
			# {"feature": "Time", "instances": 2, "metric_value": 1.0, "depth": 3}
			if obj[1]<=0:
				return 'True'
			elif obj[1]>0:
				return 'False'
			else: return 'False'
		else: return 'True'
	else: return 'True'
