def findDecision(obj): #obj[0]: Passanger, obj[1]: Coupon, obj[2]: Education, obj[3]: Occupation, obj[4]: Restaurant20to50, obj[5]: Direction_same, obj[6]: Distance
	# {"feature": "Direction_same", "instances": 34, "metric_value": 0.99, "depth": 1}
	if obj[5]<=0:
		# {"feature": "Education", "instances": 28, "metric_value": 0.9403, "depth": 2}
		if obj[2]>0:
			# {"feature": "Occupation", "instances": 22, "metric_value": 0.994, "depth": 3}
			if obj[3]>2:
				# {"feature": "Distance", "instances": 17, "metric_value": 0.9367, "depth": 4}
				if obj[6]<=2:
					# {"feature": "Coupon", "instances": 13, "metric_value": 0.7793, "depth": 5}
					if obj[1]<=3:
						return 'True'
					elif obj[1]>3:
						# {"feature": "Restaurant20to50", "instances": 6, "metric_value": 1.0, "depth": 6}
						if obj[4]<=1.0:
							# {"feature": "Passanger", "instances": 4, "metric_value": 0.8113, "depth": 7}
							if obj[0]<=1:
								return 'True'
							else: return 'True'
						elif obj[4]>1.0:
							return 'False'
						else: return 'False'
					else: return 'True'
				elif obj[6]>2:
					# {"feature": "Coupon", "instances": 4, "metric_value": 0.8113, "depth": 5}
					if obj[1]>0:
						return 'False'
					elif obj[1]<=0:
						return 'True'
					else: return 'True'
				else: return 'False'
			elif obj[3]<=2:
				# {"feature": "Distance", "instances": 5, "metric_value": 0.7219, "depth": 4}
				if obj[6]<=2:
					return 'False'
				elif obj[6]>2:
					return 'True'
				else: return 'True'
			else: return 'False'
		elif obj[2]<=0:
			return 'True'
		else: return 'True'
	elif obj[5]>0:
		# {"feature": "Occupation", "instances": 6, "metric_value": 0.65, "depth": 2}
		if obj[3]>7:
			return 'False'
		elif obj[3]<=7:
			return 'True'
		else: return 'True'
	else: return 'False'
