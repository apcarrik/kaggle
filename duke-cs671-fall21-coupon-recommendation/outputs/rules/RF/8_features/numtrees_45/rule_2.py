def findDecision(obj): #obj[0]: Passanger, obj[1]: Coupon, obj[2]: Education, obj[3]: Occupation, obj[4]: Bar, obj[5]: Restaurant20to50, obj[6]: Direction_same, obj[7]: Distance
	# {"feature": "Education", "instances": 23, "metric_value": 0.9656, "depth": 1}
	if obj[2]<=1:
		# {"feature": "Occupation", "instances": 12, "metric_value": 0.9799, "depth": 2}
		if obj[3]<=6:
			# {"feature": "Restaurant20to50", "instances": 9, "metric_value": 0.9911, "depth": 3}
			if obj[5]<=1.0:
				# {"feature": "Coupon", "instances": 7, "metric_value": 0.9852, "depth": 4}
				if obj[1]>0:
					# {"feature": "Distance", "instances": 5, "metric_value": 0.971, "depth": 5}
					if obj[7]>1:
						return 'True'
					elif obj[7]<=1:
						return 'False'
					else: return 'False'
				elif obj[1]<=0:
					return 'False'
				else: return 'False'
			elif obj[5]>1.0:
				return 'True'
			else: return 'True'
		elif obj[3]>6:
			return 'False'
		else: return 'False'
	elif obj[2]>1:
		# {"feature": "Occupation", "instances": 11, "metric_value": 0.684, "depth": 2}
		if obj[3]<=11:
			return 'True'
		elif obj[3]>11:
			# {"feature": "Bar", "instances": 3, "metric_value": 0.9183, "depth": 3}
			if obj[4]<=2.0:
				return 'False'
			elif obj[4]>2.0:
				return 'True'
			else: return 'True'
		else: return 'False'
	else: return 'True'
