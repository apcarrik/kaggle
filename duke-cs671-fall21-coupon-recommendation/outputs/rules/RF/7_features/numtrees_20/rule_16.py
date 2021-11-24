def findDecision(obj): #obj[0]: Passanger, obj[1]: Coupon, obj[2]: Education, obj[3]: Occupation, obj[4]: Restaurant20to50, obj[5]: Direction_same, obj[6]: Distance
	# {"feature": "Distance", "instances": 51, "metric_value": 0.9774, "depth": 1}
	if obj[6]<=2:
		# {"feature": "Education", "instances": 47, "metric_value": 0.9441, "depth": 2}
		if obj[2]<=3:
			# {"feature": "Occupation", "instances": 41, "metric_value": 0.9789, "depth": 3}
			if obj[3]<=7:
				# {"feature": "Restaurant20to50", "instances": 28, "metric_value": 0.9059, "depth": 4}
				if obj[4]<=2.0:
					# {"feature": "Coupon", "instances": 27, "metric_value": 0.8767, "depth": 5}
					if obj[1]>0:
						# {"feature": "Passanger", "instances": 22, "metric_value": 0.7732, "depth": 6}
						if obj[0]<=1:
							# {"feature": "Direction_same", "instances": 15, "metric_value": 0.9183, "depth": 7}
							if obj[5]<=0:
								return 'True'
							elif obj[5]>0:
								return 'False'
							else: return 'False'
						elif obj[0]>1:
							return 'True'
						else: return 'True'
					elif obj[1]<=0:
						# {"feature": "Passanger", "instances": 5, "metric_value": 0.971, "depth": 6}
						if obj[0]<=1:
							# {"feature": "Direction_same", "instances": 4, "metric_value": 1.0, "depth": 7}
							if obj[5]<=0:
								return 'True'
							elif obj[5]>0:
								return 'False'
							else: return 'False'
						elif obj[0]>1:
							return 'False'
						else: return 'False'
					else: return 'False'
				elif obj[4]>2.0:
					return 'False'
				else: return 'False'
			elif obj[3]>7:
				# {"feature": "Coupon", "instances": 13, "metric_value": 0.9612, "depth": 4}
				if obj[1]<=3:
					# {"feature": "Restaurant20to50", "instances": 10, "metric_value": 1.0, "depth": 5}
					if obj[4]<=3.0:
						# {"feature": "Passanger", "instances": 9, "metric_value": 0.9911, "depth": 6}
						if obj[0]>1:
							# {"feature": "Direction_same", "instances": 5, "metric_value": 0.971, "depth": 7}
							if obj[5]<=0:
								return 'True'
							else: return 'True'
						elif obj[0]<=1:
							# {"feature": "Direction_same", "instances": 4, "metric_value": 0.8113, "depth": 7}
							if obj[5]<=0:
								return 'False'
							else: return 'False'
						else: return 'False'
					elif obj[4]>3.0:
						return 'True'
					else: return 'True'
				elif obj[1]>3:
					return 'False'
				else: return 'False'
			else: return 'False'
		elif obj[2]>3:
			return 'True'
		else: return 'True'
	elif obj[6]>2:
		return 'False'
	else: return 'False'
