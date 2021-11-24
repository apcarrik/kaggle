def findDecision(obj): #obj[0]: Coupon, obj[1]: Education, obj[2]: Occupation, obj[3]: Restaurant20to50, obj[4]: Distance
	# {"feature": "Coupon", "instances": 23, "metric_value": 0.9877, "depth": 1}
	if obj[0]>1:
		# {"feature": "Restaurant20to50", "instances": 14, "metric_value": 0.7496, "depth": 2}
		if obj[3]>1.0:
			return 'True'
		elif obj[3]<=1.0:
			# {"feature": "Education", "instances": 7, "metric_value": 0.9852, "depth": 3}
			if obj[1]>0:
				# {"feature": "Occupation", "instances": 5, "metric_value": 0.7219, "depth": 4}
				if obj[2]<=19:
					return 'True'
				elif obj[2]>19:
					return 'False'
				else: return 'False'
			elif obj[1]<=0:
				return 'False'
			else: return 'False'
		else: return 'True'
	elif obj[0]<=1:
		# {"feature": "Education", "instances": 9, "metric_value": 0.7642, "depth": 2}
		if obj[1]<=3:
			# {"feature": "Occupation", "instances": 8, "metric_value": 0.5436, "depth": 3}
			if obj[2]<=9:
				return 'False'
			elif obj[2]>9:
				return 'True'
			else: return 'True'
		elif obj[1]>3:
			return 'True'
		else: return 'True'
	else: return 'False'
