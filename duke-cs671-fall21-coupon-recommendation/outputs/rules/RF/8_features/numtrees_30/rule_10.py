def findDecision(obj): #obj[0]: Passanger, obj[1]: Coupon, obj[2]: Education, obj[3]: Occupation, obj[4]: Bar, obj[5]: Restaurant20to50, obj[6]: Direction_same, obj[7]: Distance
	# {"feature": "Education", "instances": 34, "metric_value": 0.9774, "depth": 1}
	if obj[2]>0:
		# {"feature": "Direction_same", "instances": 20, "metric_value": 0.971, "depth": 2}
		if obj[6]<=0:
			# {"feature": "Restaurant20to50", "instances": 15, "metric_value": 0.8366, "depth": 3}
			if obj[5]>0.0:
				# {"feature": "Distance", "instances": 14, "metric_value": 0.7496, "depth": 4}
				if obj[7]<=2:
					# {"feature": "Occupation", "instances": 11, "metric_value": 0.8454, "depth": 5}
					if obj[3]<=6:
						# {"feature": "Coupon", "instances": 7, "metric_value": 0.5917, "depth": 6}
						if obj[1]>0:
							return 'False'
						elif obj[1]<=0:
							# {"feature": "Bar", "instances": 2, "metric_value": 1.0, "depth": 7}
							if obj[4]<=0.0:
								return 'False'
							elif obj[4]>0.0:
								return 'True'
							else: return 'True'
						else: return 'False'
					elif obj[3]>6:
						# {"feature": "Coupon", "instances": 4, "metric_value": 1.0, "depth": 6}
						if obj[1]>1:
							# {"feature": "Bar", "instances": 3, "metric_value": 0.9183, "depth": 7}
							if obj[4]<=1.0:
								return 'True'
							elif obj[4]>1.0:
								return 'False'
							else: return 'False'
						elif obj[1]<=1:
							return 'False'
						else: return 'False'
					else: return 'True'
				elif obj[7]>2:
					return 'False'
				else: return 'False'
			elif obj[5]<=0.0:
				return 'True'
			else: return 'True'
		elif obj[6]>0:
			# {"feature": "Restaurant20to50", "instances": 5, "metric_value": 0.7219, "depth": 3}
			if obj[5]<=2.0:
				return 'True'
			elif obj[5]>2.0:
				return 'False'
			else: return 'False'
		else: return 'True'
	elif obj[2]<=0:
		# {"feature": "Coupon", "instances": 14, "metric_value": 0.5917, "depth": 2}
		if obj[1]<=3:
			return 'True'
		elif obj[1]>3:
			# {"feature": "Bar", "instances": 3, "metric_value": 0.9183, "depth": 3}
			if obj[4]<=0.0:
				return 'False'
			elif obj[4]>0.0:
				return 'True'
			else: return 'True'
		else: return 'False'
	else: return 'True'
