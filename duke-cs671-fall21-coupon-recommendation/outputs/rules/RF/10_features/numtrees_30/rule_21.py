def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Education, obj[4]: Occupation, obj[5]: Bar, obj[6]: Coffeehouse, obj[7]: Restaurant20to50, obj[8]: Direction_same, obj[9]: Distance
	# {"feature": "Coupon", "instances": 34, "metric_value": 0.9367, "depth": 1}
	if obj[2]>1:
		# {"feature": "Coffeehouse", "instances": 26, "metric_value": 0.7793, "depth": 2}
		if obj[6]<=1.0:
			# {"feature": "Occupation", "instances": 17, "metric_value": 0.9367, "depth": 3}
			if obj[4]>1:
				# {"feature": "Time", "instances": 15, "metric_value": 0.8366, "depth": 4}
				if obj[1]<=2:
					# {"feature": "Distance", "instances": 10, "metric_value": 0.469, "depth": 5}
					if obj[9]<=2:
						return 'True'
					elif obj[9]>2:
						return 'False'
					else: return 'False'
				elif obj[1]>2:
					# {"feature": "Education", "instances": 5, "metric_value": 0.971, "depth": 5}
					if obj[3]<=1:
						# {"feature": "Passanger", "instances": 4, "metric_value": 1.0, "depth": 6}
						if obj[0]<=1:
							# {"feature": "Bar", "instances": 3, "metric_value": 0.9183, "depth": 7}
							if obj[5]>0.0:
								return 'False'
							elif obj[5]<=0.0:
								return 'True'
							else: return 'True'
						elif obj[0]>1:
							return 'True'
						else: return 'True'
					elif obj[3]>1:
						return 'False'
					else: return 'False'
				else: return 'False'
			elif obj[4]<=1:
				return 'False'
			else: return 'False'
		elif obj[6]>1.0:
			return 'True'
		else: return 'True'
	elif obj[2]<=1:
		# {"feature": "Education", "instances": 8, "metric_value": 0.8113, "depth": 2}
		if obj[3]>1:
			# {"feature": "Occupation", "instances": 4, "metric_value": 1.0, "depth": 3}
			if obj[4]>4:
				# {"feature": "Bar", "instances": 3, "metric_value": 0.9183, "depth": 4}
				if obj[5]>0.0:
					return 'True'
				elif obj[5]<=0.0:
					return 'False'
				else: return 'False'
			elif obj[4]<=4:
				return 'False'
			else: return 'False'
		elif obj[3]<=1:
			return 'False'
		else: return 'False'
	else: return 'False'
