def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Education, obj[4]: Occupation, obj[5]: Bar, obj[6]: Restaurant20to50, obj[7]: Direction_same, obj[8]: Distance
	# {"feature": "Distance", "instances": 34, "metric_value": 0.9975, "depth": 1}
	if obj[8]>1:
		# {"feature": "Occupation", "instances": 23, "metric_value": 0.9656, "depth": 2}
		if obj[4]<=13:
			# {"feature": "Bar", "instances": 20, "metric_value": 0.8813, "depth": 3}
			if obj[5]<=1.0:
				# {"feature": "Coupon", "instances": 14, "metric_value": 0.5917, "depth": 4}
				if obj[2]<=2:
					return 'False'
				elif obj[2]>2:
					# {"feature": "Passanger", "instances": 6, "metric_value": 0.9183, "depth": 5}
					if obj[0]<=1:
						return 'False'
					elif obj[0]>1:
						return 'True'
					else: return 'True'
				else: return 'False'
			elif obj[5]>1.0:
				# {"feature": "Time", "instances": 6, "metric_value": 0.9183, "depth": 4}
				if obj[1]>1:
					# {"feature": "Restaurant20to50", "instances": 5, "metric_value": 0.7219, "depth": 5}
					if obj[6]>0.0:
						return 'True'
					elif obj[6]<=0.0:
						return 'False'
					else: return 'False'
				elif obj[1]<=1:
					return 'False'
				else: return 'False'
			else: return 'True'
		elif obj[4]>13:
			return 'True'
		else: return 'True'
	elif obj[8]<=1:
		# {"feature": "Passanger", "instances": 11, "metric_value": 0.684, "depth": 2}
		if obj[0]<=1:
			return 'True'
		elif obj[0]>1:
			# {"feature": "Time", "instances": 4, "metric_value": 1.0, "depth": 3}
			if obj[1]>0:
				# {"feature": "Coupon", "instances": 3, "metric_value": 0.9183, "depth": 4}
				if obj[2]>0:
					return 'True'
				elif obj[2]<=0:
					return 'False'
				else: return 'False'
			elif obj[1]<=0:
				return 'False'
			else: return 'False'
		else: return 'True'
	else: return 'True'
