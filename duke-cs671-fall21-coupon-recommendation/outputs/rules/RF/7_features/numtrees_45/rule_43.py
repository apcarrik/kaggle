def findDecision(obj): #obj[0]: Passanger, obj[1]: Coupon, obj[2]: Education, obj[3]: Occupation, obj[4]: Restaurant20to50, obj[5]: Direction_same, obj[6]: Distance
	# {"feature": "Passanger", "instances": 23, "metric_value": 0.9321, "depth": 1}
	if obj[0]<=2:
		# {"feature": "Occupation", "instances": 20, "metric_value": 0.8113, "depth": 2}
		if obj[3]>4:
			# {"feature": "Coupon", "instances": 12, "metric_value": 0.4138, "depth": 3}
			if obj[1]>0:
				return 'False'
			elif obj[1]<=0:
				# {"feature": "Education", "instances": 3, "metric_value": 0.9183, "depth": 4}
				if obj[2]<=0:
					# {"feature": "Restaurant20to50", "instances": 2, "metric_value": 1.0, "depth": 5}
					if obj[4]<=2.0:
						# {"feature": "Direction_same", "instances": 2, "metric_value": 1.0, "depth": 6}
						if obj[5]<=1:
							# {"feature": "Distance", "instances": 2, "metric_value": 1.0, "depth": 7}
							if obj[6]<=2:
								return 'False'
							else: return 'False'
						else: return 'False'
					else: return 'False'
				elif obj[2]>0:
					return 'False'
				else: return 'False'
			else: return 'False'
		elif obj[3]<=4:
			# {"feature": "Distance", "instances": 8, "metric_value": 1.0, "depth": 3}
			if obj[6]>1:
				# {"feature": "Education", "instances": 6, "metric_value": 0.9183, "depth": 4}
				if obj[2]>0:
					# {"feature": "Coupon", "instances": 4, "metric_value": 1.0, "depth": 5}
					if obj[1]>0:
						# {"feature": "Restaurant20to50", "instances": 3, "metric_value": 0.9183, "depth": 6}
						if obj[4]<=1.0:
							return 'True'
						elif obj[4]>1.0:
							return 'False'
						else: return 'False'
					elif obj[1]<=0:
						return 'False'
					else: return 'False'
				elif obj[2]<=0:
					return 'False'
				else: return 'False'
			elif obj[6]<=1:
				return 'True'
			else: return 'True'
		else: return 'False'
	elif obj[0]>2:
		return 'True'
	else: return 'True'
