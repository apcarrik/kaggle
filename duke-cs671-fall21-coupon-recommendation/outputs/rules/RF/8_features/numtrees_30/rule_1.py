def findDecision(obj): #obj[0]: Passanger, obj[1]: Coupon, obj[2]: Education, obj[3]: Occupation, obj[4]: Bar, obj[5]: Restaurant20to50, obj[6]: Direction_same, obj[7]: Distance
	# {"feature": "Occupation", "instances": 34, "metric_value": 0.9597, "depth": 1}
	if obj[3]>1:
		# {"feature": "Education", "instances": 27, "metric_value": 0.999, "depth": 2}
		if obj[2]>0:
			# {"feature": "Distance", "instances": 18, "metric_value": 0.9641, "depth": 3}
			if obj[7]>1:
				# {"feature": "Coupon", "instances": 14, "metric_value": 1.0, "depth": 4}
				if obj[1]<=3:
					# {"feature": "Restaurant20to50", "instances": 9, "metric_value": 0.9183, "depth": 5}
					if obj[5]<=1.0:
						# {"feature": "Passanger", "instances": 5, "metric_value": 0.971, "depth": 6}
						if obj[0]<=2:
							# {"feature": "Bar", "instances": 4, "metric_value": 0.8113, "depth": 7}
							if obj[4]<=2.0:
								return 'False'
							elif obj[4]>2.0:
								return 'True'
							else: return 'True'
						elif obj[0]>2:
							return 'True'
						else: return 'True'
					elif obj[5]>1.0:
						return 'True'
					else: return 'True'
				elif obj[1]>3:
					# {"feature": "Bar", "instances": 5, "metric_value": 0.7219, "depth": 5}
					if obj[4]<=1.0:
						return 'False'
					elif obj[4]>1.0:
						# {"feature": "Restaurant20to50", "instances": 2, "metric_value": 1.0, "depth": 6}
						if obj[5]<=1.0:
							return 'True'
						elif obj[5]>1.0:
							return 'False'
						else: return 'False'
					else: return 'True'
				else: return 'False'
			elif obj[7]<=1:
				return 'False'
			else: return 'False'
		elif obj[2]<=0:
			# {"feature": "Passanger", "instances": 9, "metric_value": 0.7642, "depth": 3}
			if obj[0]<=1:
				return 'True'
			elif obj[0]>1:
				# {"feature": "Bar", "instances": 4, "metric_value": 1.0, "depth": 4}
				if obj[4]<=0.0:
					return 'False'
				elif obj[4]>0.0:
					return 'True'
				else: return 'True'
			else: return 'False'
		else: return 'True'
	elif obj[3]<=1:
		return 'True'
	else: return 'True'
