def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Education, obj[4]: Occupation, obj[5]: Bar, obj[6]: Restaurant20to50, obj[7]: Direction_same, obj[8]: Distance
	# {"feature": "Coupon", "instances": 34, "metric_value": 0.7335, "depth": 1}
	if obj[2]>1:
		# {"feature": "Occupation", "instances": 26, "metric_value": 0.5159, "depth": 2}
		if obj[4]>5:
			# {"feature": "Direction_same", "instances": 14, "metric_value": 0.7496, "depth": 3}
			if obj[7]<=0:
				# {"feature": "Education", "instances": 11, "metric_value": 0.8454, "depth": 4}
				if obj[3]<=1:
					# {"feature": "Passanger", "instances": 8, "metric_value": 0.5436, "depth": 5}
					if obj[0]>1:
						return 'True'
					elif obj[0]<=1:
						# {"feature": "Time", "instances": 3, "metric_value": 0.9183, "depth": 6}
						if obj[1]<=1:
							return 'True'
						elif obj[1]>1:
							return 'False'
						else: return 'False'
					else: return 'True'
				elif obj[3]>1:
					# {"feature": "Time", "instances": 3, "metric_value": 0.9183, "depth": 5}
					if obj[1]<=2:
						return 'False'
					elif obj[1]>2:
						return 'True'
					else: return 'True'
				else: return 'False'
			elif obj[7]>0:
				return 'True'
			else: return 'True'
		elif obj[4]<=5:
			return 'True'
		else: return 'True'
	elif obj[2]<=1:
		# {"feature": "Occupation", "instances": 8, "metric_value": 1.0, "depth": 2}
		if obj[4]<=6:
			# {"feature": "Passanger", "instances": 6, "metric_value": 0.9183, "depth": 3}
			if obj[0]<=1:
				# {"feature": "Bar", "instances": 5, "metric_value": 0.7219, "depth": 4}
				if obj[5]<=1.0:
					return 'True'
				elif obj[5]>1.0:
					# {"feature": "Restaurant20to50", "instances": 2, "metric_value": 1.0, "depth": 5}
					if obj[6]<=1.0:
						return 'True'
					elif obj[6]>1.0:
						return 'False'
					else: return 'False'
				else: return 'True'
			elif obj[0]>1:
				return 'False'
			else: return 'False'
		elif obj[4]>6:
			return 'False'
		else: return 'False'
	else: return 'True'
