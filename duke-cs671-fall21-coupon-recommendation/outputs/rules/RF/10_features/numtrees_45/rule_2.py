def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Education, obj[4]: Occupation, obj[5]: Bar, obj[6]: Coffeehouse, obj[7]: Restaurant20to50, obj[8]: Direction_same, obj[9]: Distance
	# {"feature": "Coffeehouse", "instances": 23, "metric_value": 0.9986, "depth": 1}
	if obj[6]<=1.0:
		# {"feature": "Restaurant20to50", "instances": 13, "metric_value": 0.7793, "depth": 2}
		if obj[7]<=1.0:
			return 'False'
		elif obj[7]>1.0:
			# {"feature": "Coupon", "instances": 6, "metric_value": 1.0, "depth": 3}
			if obj[2]>1:
				# {"feature": "Education", "instances": 4, "metric_value": 0.8113, "depth": 4}
				if obj[3]>0:
					return 'True'
				elif obj[3]<=0:
					return 'False'
				else: return 'False'
			elif obj[2]<=1:
				return 'False'
			else: return 'False'
		else: return 'True'
	elif obj[6]>1.0:
		# {"feature": "Occupation", "instances": 10, "metric_value": 0.7219, "depth": 2}
		if obj[4]<=14:
			return 'True'
		elif obj[4]>14:
			# {"feature": "Passanger", "instances": 3, "metric_value": 0.9183, "depth": 3}
			if obj[0]<=1:
				return 'False'
			elif obj[0]>1:
				return 'True'
			else: return 'True'
		else: return 'False'
	else: return 'True'
