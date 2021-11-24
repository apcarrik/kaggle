def findDecision(obj): #obj[0]: Passanger, obj[1]: Coupon, obj[2]: Education, obj[3]: Occupation, obj[4]: Restaurant20to50, obj[5]: Distance
	# {"feature": "Occupation", "instances": 23, "metric_value": 0.9986, "depth": 1}
	if obj[3]>1:
		# {"feature": "Education", "instances": 20, "metric_value": 0.971, "depth": 2}
		if obj[2]>0:
			# {"feature": "Passanger", "instances": 11, "metric_value": 0.684, "depth": 3}
			if obj[0]<=1:
				return 'False'
			elif obj[0]>1:
				# {"feature": "Restaurant20to50", "instances": 3, "metric_value": 0.9183, "depth": 4}
				if obj[4]<=2.0:
					return 'True'
				elif obj[4]>2.0:
					return 'False'
				else: return 'False'
			else: return 'True'
		elif obj[2]<=0:
			# {"feature": "Coupon", "instances": 9, "metric_value": 0.9183, "depth": 3}
			if obj[1]>1:
				# {"feature": "Restaurant20to50", "instances": 7, "metric_value": 0.5917, "depth": 4}
				if obj[4]<=1.0:
					return 'True'
				elif obj[4]>1.0:
					# {"feature": "Distance", "instances": 2, "metric_value": 1.0, "depth": 5}
					if obj[5]<=1:
						return 'False'
					elif obj[5]>1:
						return 'True'
					else: return 'True'
				else: return 'False'
			elif obj[1]<=1:
				return 'False'
			else: return 'False'
		else: return 'True'
	elif obj[3]<=1:
		return 'True'
	else: return 'True'
