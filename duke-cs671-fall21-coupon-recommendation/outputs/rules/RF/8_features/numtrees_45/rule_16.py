def findDecision(obj): #obj[0]: Passanger, obj[1]: Coupon, obj[2]: Education, obj[3]: Occupation, obj[4]: Bar, obj[5]: Restaurant20to50, obj[6]: Direction_same, obj[7]: Distance
	# {"feature": "Restaurant20to50", "instances": 23, "metric_value": 0.9656, "depth": 1}
	if obj[5]<=2.0:
		# {"feature": "Coupon", "instances": 20, "metric_value": 0.8813, "depth": 2}
		if obj[1]>1:
			# {"feature": "Occupation", "instances": 14, "metric_value": 0.5917, "depth": 3}
			if obj[3]>1:
				# {"feature": "Education", "instances": 13, "metric_value": 0.3912, "depth": 4}
				if obj[2]<=2:
					return 'True'
				elif obj[2]>2:
					# {"feature": "Passanger", "instances": 4, "metric_value": 0.8113, "depth": 5}
					if obj[0]>1:
						return 'True'
					elif obj[0]<=1:
						return 'False'
					else: return 'False'
				else: return 'True'
			elif obj[3]<=1:
				return 'False'
			else: return 'False'
		elif obj[1]<=1:
			# {"feature": "Bar", "instances": 6, "metric_value": 0.9183, "depth": 3}
			if obj[4]<=0.0:
				return 'False'
			elif obj[4]>0.0:
				# {"feature": "Passanger", "instances": 3, "metric_value": 0.9183, "depth": 4}
				if obj[0]>0:
					# {"feature": "Occupation", "instances": 2, "metric_value": 1.0, "depth": 5}
					if obj[3]>6:
						return 'True'
					elif obj[3]<=6:
						return 'False'
					else: return 'False'
				elif obj[0]<=0:
					return 'True'
				else: return 'True'
			else: return 'True'
		else: return 'False'
	elif obj[5]>2.0:
		return 'False'
	else: return 'False'
