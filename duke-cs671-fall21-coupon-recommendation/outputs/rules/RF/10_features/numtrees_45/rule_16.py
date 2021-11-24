def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Education, obj[4]: Occupation, obj[5]: Bar, obj[6]: Coffeehouse, obj[7]: Restaurant20to50, obj[8]: Direction_same, obj[9]: Distance
	# {"feature": "Coupon", "instances": 23, "metric_value": 0.9986, "depth": 1}
	if obj[2]>1:
		# {"feature": "Education", "instances": 14, "metric_value": 0.7496, "depth": 2}
		if obj[3]<=2:
			# {"feature": "Occupation", "instances": 11, "metric_value": 0.4395, "depth": 3}
			if obj[4]<=7:
				return 'True'
			elif obj[4]>7:
				# {"feature": "Passanger", "instances": 2, "metric_value": 1.0, "depth": 4}
				if obj[0]<=1:
					return 'True'
				elif obj[0]>1:
					return 'False'
				else: return 'False'
			else: return 'True'
		elif obj[3]>2:
			# {"feature": "Bar", "instances": 3, "metric_value": 0.9183, "depth": 3}
			if obj[5]>0.0:
				return 'False'
			elif obj[5]<=0.0:
				return 'True'
			else: return 'True'
		else: return 'False'
	elif obj[2]<=1:
		# {"feature": "Passanger", "instances": 9, "metric_value": 0.5033, "depth": 2}
		if obj[0]<=2:
			return 'False'
		elif obj[0]>2:
			return 'True'
		else: return 'True'
	else: return 'False'
