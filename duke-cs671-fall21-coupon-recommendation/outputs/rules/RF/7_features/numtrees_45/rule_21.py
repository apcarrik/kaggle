def findDecision(obj): #obj[0]: Passanger, obj[1]: Coupon, obj[2]: Education, obj[3]: Occupation, obj[4]: Restaurant20to50, obj[5]: Direction_same, obj[6]: Distance
	# {"feature": "Coupon", "instances": 23, "metric_value": 0.9656, "depth": 1}
	if obj[1]>1:
		# {"feature": "Restaurant20to50", "instances": 12, "metric_value": 0.4138, "depth": 2}
		if obj[4]<=1.0:
			return 'True'
		elif obj[4]>1.0:
			# {"feature": "Occupation", "instances": 3, "metric_value": 0.9183, "depth": 3}
			if obj[3]<=4:
				return 'True'
			elif obj[3]>4:
				return 'False'
			else: return 'False'
		else: return 'True'
	elif obj[1]<=1:
		# {"feature": "Direction_same", "instances": 11, "metric_value": 0.8454, "depth": 2}
		if obj[5]<=0:
			# {"feature": "Passanger", "instances": 9, "metric_value": 0.5033, "depth": 3}
			if obj[0]<=1:
				return 'False'
			elif obj[0]>1:
				# {"feature": "Education", "instances": 2, "metric_value": 1.0, "depth": 4}
				if obj[2]>3:
					return 'False'
				elif obj[2]<=3:
					return 'True'
				else: return 'True'
			else: return 'False'
		elif obj[5]>0:
			return 'True'
		else: return 'True'
	else: return 'False'
