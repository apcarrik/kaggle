def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Age, obj[4]: Education, obj[5]: Occupation, obj[6]: Bar, obj[7]: Coffeehouse, obj[8]: Restaurant20to50, obj[9]: Direction_same, obj[10]: Distance
	# {"feature": "Age", "instances": 23, "metric_value": 0.9656, "depth": 1}
	if obj[3]>1:
		# {"feature": "Bar", "instances": 14, "metric_value": 0.5917, "depth": 2}
		if obj[6]<=0.0:
			return 'False'
		elif obj[6]>0.0:
			# {"feature": "Education", "instances": 4, "metric_value": 1.0, "depth": 3}
			if obj[4]<=0:
				return 'True'
			elif obj[4]>0:
				return 'False'
			else: return 'False'
		else: return 'True'
	elif obj[3]<=1:
		# {"feature": "Passanger", "instances": 9, "metric_value": 0.7642, "depth": 2}
		if obj[0]>0:
			# {"feature": "Occupation", "instances": 8, "metric_value": 0.5436, "depth": 3}
			if obj[5]>1:
				return 'True'
			elif obj[5]<=1:
				# {"feature": "Time", "instances": 2, "metric_value": 1.0, "depth": 4}
				if obj[1]>0:
					return 'True'
				elif obj[1]<=0:
					return 'False'
				else: return 'False'
			else: return 'True'
		elif obj[0]<=0:
			return 'False'
		else: return 'False'
	else: return 'True'
