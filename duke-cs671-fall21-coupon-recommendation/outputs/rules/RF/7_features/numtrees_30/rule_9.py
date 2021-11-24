def findDecision(obj): #obj[0]: Passanger, obj[1]: Coupon, obj[2]: Education, obj[3]: Occupation, obj[4]: Restaurant20to50, obj[5]: Direction_same, obj[6]: Distance
	# {"feature": "Distance", "instances": 34, "metric_value": 0.9975, "depth": 1}
	if obj[6]<=2:
		# {"feature": "Coupon", "instances": 28, "metric_value": 0.9852, "depth": 2}
		if obj[1]<=3:
			# {"feature": "Occupation", "instances": 15, "metric_value": 0.5665, "depth": 3}
			if obj[3]<=12:
				# {"feature": "Education", "instances": 14, "metric_value": 0.3712, "depth": 4}
				if obj[2]<=2:
					return 'True'
				elif obj[2]>2:
					# {"feature": "Restaurant20to50", "instances": 5, "metric_value": 0.7219, "depth": 5}
					if obj[4]<=1.0:
						return 'True'
					elif obj[4]>1.0:
						# {"feature": "Passanger", "instances": 2, "metric_value": 1.0, "depth": 6}
						if obj[0]>1:
							return 'False'
						elif obj[0]<=1:
							return 'True'
						else: return 'True'
					else: return 'False'
				else: return 'True'
			elif obj[3]>12:
				return 'False'
			else: return 'False'
		elif obj[1]>3:
			# {"feature": "Occupation", "instances": 13, "metric_value": 0.7793, "depth": 3}
			if obj[3]>6:
				return 'False'
			elif obj[3]<=6:
				# {"feature": "Passanger", "instances": 6, "metric_value": 1.0, "depth": 4}
				if obj[0]<=1:
					# {"feature": "Restaurant20to50", "instances": 4, "metric_value": 0.8113, "depth": 5}
					if obj[4]>0.0:
						return 'True'
					elif obj[4]<=0.0:
						return 'False'
					else: return 'False'
				elif obj[0]>1:
					return 'False'
				else: return 'False'
			else: return 'False'
		else: return 'False'
	elif obj[6]>2:
		return 'False'
	else: return 'False'
