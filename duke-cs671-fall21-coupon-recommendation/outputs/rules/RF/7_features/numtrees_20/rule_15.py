def findDecision(obj): #obj[0]: Passanger, obj[1]: Coupon, obj[2]: Education, obj[3]: Occupation, obj[4]: Restaurant20to50, obj[5]: Direction_same, obj[6]: Distance
	# {"feature": "Distance", "instances": 51, "metric_value": 0.9975, "depth": 1}
	if obj[6]>1:
		# {"feature": "Restaurant20to50", "instances": 35, "metric_value": 0.9852, "depth": 2}
		if obj[4]<=2.0:
			# {"feature": "Coupon", "instances": 30, "metric_value": 0.9481, "depth": 3}
			if obj[1]>0:
				# {"feature": "Occupation", "instances": 28, "metric_value": 0.9666, "depth": 4}
				if obj[3]<=7:
					# {"feature": "Passanger", "instances": 17, "metric_value": 0.9975, "depth": 5}
					if obj[0]<=2:
						# {"feature": "Education", "instances": 15, "metric_value": 0.971, "depth": 6}
						if obj[2]<=3:
							# {"feature": "Direction_same", "instances": 14, "metric_value": 0.9403, "depth": 7}
							if obj[5]<=0:
								return 'False'
							elif obj[5]>0:
								return 'False'
							else: return 'False'
						elif obj[2]>3:
							return 'True'
						else: return 'True'
					elif obj[0]>2:
						return 'True'
					else: return 'True'
				elif obj[3]>7:
					# {"feature": "Direction_same", "instances": 11, "metric_value": 0.8454, "depth": 5}
					if obj[5]<=0:
						# {"feature": "Education", "instances": 10, "metric_value": 0.7219, "depth": 6}
						if obj[2]>0:
							# {"feature": "Passanger", "instances": 8, "metric_value": 0.5436, "depth": 7}
							if obj[0]<=1:
								return 'False'
							elif obj[0]>1:
								return 'False'
							else: return 'False'
						elif obj[2]<=0:
							# {"feature": "Passanger", "instances": 2, "metric_value": 1.0, "depth": 7}
							if obj[0]>1:
								return 'True'
							elif obj[0]<=1:
								return 'False'
							else: return 'False'
						else: return 'True'
					elif obj[5]>0:
						return 'True'
					else: return 'True'
				else: return 'False'
			elif obj[1]<=0:
				return 'False'
			else: return 'False'
		elif obj[4]>2.0:
			# {"feature": "Coupon", "instances": 5, "metric_value": 0.7219, "depth": 3}
			if obj[1]>2:
				return 'True'
			elif obj[1]<=2:
				return 'False'
			else: return 'False'
		else: return 'True'
	elif obj[6]<=1:
		# {"feature": "Passanger", "instances": 16, "metric_value": 0.8113, "depth": 2}
		if obj[0]<=1:
			# {"feature": "Education", "instances": 9, "metric_value": 0.9911, "depth": 3}
			if obj[2]>0:
				# {"feature": "Coupon", "instances": 6, "metric_value": 0.9183, "depth": 4}
				if obj[1]>3:
					# {"feature": "Occupation", "instances": 3, "metric_value": 0.9183, "depth": 5}
					if obj[3]>4:
						# {"feature": "Restaurant20to50", "instances": 2, "metric_value": 1.0, "depth": 6}
						if obj[4]<=1.0:
							# {"feature": "Direction_same", "instances": 2, "metric_value": 1.0, "depth": 7}
							if obj[5]<=1:
								return 'True'
							else: return 'True'
						else: return 'True'
					elif obj[3]<=4:
						return 'True'
					else: return 'True'
				elif obj[1]<=3:
					return 'False'
				else: return 'False'
			elif obj[2]<=0:
				return 'True'
			else: return 'True'
		elif obj[0]>1:
			return 'True'
		else: return 'True'
	else: return 'True'
