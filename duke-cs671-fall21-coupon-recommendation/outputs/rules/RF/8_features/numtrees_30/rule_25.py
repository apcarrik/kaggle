def findDecision(obj): #obj[0]: Passanger, obj[1]: Coupon, obj[2]: Education, obj[3]: Occupation, obj[4]: Bar, obj[5]: Restaurant20to50, obj[6]: Direction_same, obj[7]: Distance
	# {"feature": "Distance", "instances": 34, "metric_value": 0.9774, "depth": 1}
	if obj[7]<=2:
		# {"feature": "Occupation", "instances": 30, "metric_value": 0.9183, "depth": 2}
		if obj[3]>4:
			# {"feature": "Coupon", "instances": 22, "metric_value": 0.7732, "depth": 3}
			if obj[1]<=3:
				# {"feature": "Passanger", "instances": 16, "metric_value": 0.5436, "depth": 4}
				if obj[0]<=2:
					# {"feature": "Direction_same", "instances": 11, "metric_value": 0.684, "depth": 5}
					if obj[6]<=0:
						# {"feature": "Bar", "instances": 6, "metric_value": 0.9183, "depth": 6}
						if obj[4]>0.0:
							# {"feature": "Restaurant20to50", "instances": 4, "metric_value": 0.8113, "depth": 7}
							if obj[5]>1.0:
								return 'True'
							elif obj[5]<=1.0:
								return 'False'
							else: return 'False'
						elif obj[4]<=0.0:
							# {"feature": "Education", "instances": 2, "metric_value": 1.0, "depth": 7}
							if obj[2]<=0:
								return 'False'
							elif obj[2]>0:
								return 'True'
							else: return 'True'
						else: return 'False'
					elif obj[6]>0:
						return 'True'
					else: return 'True'
				elif obj[0]>2:
					return 'True'
				else: return 'True'
			elif obj[1]>3:
				# {"feature": "Education", "instances": 6, "metric_value": 1.0, "depth": 4}
				if obj[2]>0:
					# {"feature": "Bar", "instances": 4, "metric_value": 0.8113, "depth": 5}
					if obj[4]<=2.0:
						return 'False'
					elif obj[4]>2.0:
						return 'True'
					else: return 'True'
				elif obj[2]<=0:
					return 'True'
				else: return 'True'
			else: return 'False'
		elif obj[3]<=4:
			# {"feature": "Education", "instances": 8, "metric_value": 0.9544, "depth": 3}
			if obj[2]>0:
				# {"feature": "Restaurant20to50", "instances": 6, "metric_value": 1.0, "depth": 4}
				if obj[5]<=1.0:
					# {"feature": "Coupon", "instances": 4, "metric_value": 0.8113, "depth": 5}
					if obj[1]>1:
						# {"feature": "Bar", "instances": 2, "metric_value": 1.0, "depth": 6}
						if obj[4]>1.0:
							return 'False'
						elif obj[4]<=1.0:
							return 'True'
						else: return 'True'
					elif obj[1]<=1:
						return 'False'
					else: return 'False'
				elif obj[5]>1.0:
					return 'True'
				else: return 'True'
			elif obj[2]<=0:
				return 'False'
			else: return 'False'
		else: return 'False'
	elif obj[7]>2:
		return 'False'
	else: return 'False'
