def findDecision(obj): #obj[0]: Passanger, obj[1]: Coupon, obj[2]: Education, obj[3]: Occupation, obj[4]: Restaurant20to50, obj[5]: Direction_same, obj[6]: Distance
	# {"feature": "Education", "instances": 51, "metric_value": 0.9183, "depth": 1}
	if obj[2]<=3:
		# {"feature": "Passanger", "instances": 43, "metric_value": 0.9682, "depth": 2}
		if obj[0]<=2:
			# {"feature": "Direction_same", "instances": 34, "metric_value": 0.9975, "depth": 3}
			if obj[5]<=0:
				# {"feature": "Coupon", "instances": 25, "metric_value": 0.971, "depth": 4}
				if obj[1]>0:
					# {"feature": "Occupation", "instances": 21, "metric_value": 0.9984, "depth": 5}
					if obj[3]<=8:
						# {"feature": "Restaurant20to50", "instances": 13, "metric_value": 0.8905, "depth": 6}
						if obj[4]>0.0:
							# {"feature": "Distance", "instances": 10, "metric_value": 0.7219, "depth": 7}
							if obj[6]<=2:
								return 'True'
							elif obj[6]>2:
								return 'True'
							else: return 'True'
						elif obj[4]<=0.0:
							# {"feature": "Distance", "instances": 3, "metric_value": 0.9183, "depth": 7}
							if obj[6]<=2:
								return 'False'
							else: return 'False'
						else: return 'False'
					elif obj[3]>8:
						# {"feature": "Distance", "instances": 8, "metric_value": 0.5436, "depth": 6}
						if obj[6]<=1:
							# {"feature": "Restaurant20to50", "instances": 4, "metric_value": 0.8113, "depth": 7}
							if obj[4]<=1.0:
								return 'False'
							elif obj[4]>1.0:
								return 'False'
							else: return 'False'
						elif obj[6]>1:
							return 'False'
						else: return 'False'
					else: return 'False'
				elif obj[1]<=0:
					return 'False'
				else: return 'False'
			elif obj[5]>0:
				# {"feature": "Restaurant20to50", "instances": 9, "metric_value": 0.5033, "depth": 4}
				if obj[4]<=1.0:
					return 'True'
				elif obj[4]>1.0:
					# {"feature": "Coupon", "instances": 2, "metric_value": 1.0, "depth": 5}
					if obj[1]<=4:
						# {"feature": "Occupation", "instances": 2, "metric_value": 1.0, "depth": 6}
						if obj[3]<=6:
							# {"feature": "Distance", "instances": 2, "metric_value": 1.0, "depth": 7}
							if obj[6]<=1:
								return 'True'
							else: return 'True'
						else: return 'True'
					else: return 'True'
				else: return 'True'
			else: return 'True'
		elif obj[0]>2:
			# {"feature": "Occupation", "instances": 9, "metric_value": 0.5033, "depth": 3}
			if obj[3]<=6:
				return 'True'
			elif obj[3]>6:
				# {"feature": "Coupon", "instances": 3, "metric_value": 0.9183, "depth": 4}
				if obj[1]>2:
					return 'True'
				elif obj[1]<=2:
					return 'False'
				else: return 'False'
			else: return 'True'
		else: return 'True'
	elif obj[2]>3:
		return 'True'
	else: return 'True'
