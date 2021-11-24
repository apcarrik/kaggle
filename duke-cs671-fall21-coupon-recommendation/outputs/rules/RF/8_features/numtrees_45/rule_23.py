def findDecision(obj): #obj[0]: Passanger, obj[1]: Coupon, obj[2]: Education, obj[3]: Occupation, obj[4]: Bar, obj[5]: Restaurant20to50, obj[6]: Direction_same, obj[7]: Distance
	# {"feature": "Occupation", "instances": 23, "metric_value": 0.9877, "depth": 1}
	if obj[3]>2:
		# {"feature": "Direction_same", "instances": 17, "metric_value": 0.9774, "depth": 2}
		if obj[6]<=0:
			# {"feature": "Passanger", "instances": 10, "metric_value": 0.469, "depth": 3}
			if obj[0]<=2:
				return 'False'
			elif obj[0]>2:
				# {"feature": "Education", "instances": 2, "metric_value": 1.0, "depth": 4}
				if obj[2]<=2:
					return 'True'
				elif obj[2]>2:
					return 'False'
				else: return 'False'
			else: return 'True'
		elif obj[6]>0:
			# {"feature": "Education", "instances": 7, "metric_value": 0.5917, "depth": 3}
			if obj[2]<=2:
				return 'True'
			elif obj[2]>2:
				return 'False'
			else: return 'False'
		else: return 'True'
	elif obj[3]<=2:
		return 'True'
	else: return 'True'
