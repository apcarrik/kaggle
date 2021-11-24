def findDecision(obj): #obj[0]: Passanger, obj[1]: Coupon, obj[2]: Education, obj[3]: Occupation, obj[4]: Restaurant20to50, obj[5]: Direction_same, obj[6]: Distance
	# {"feature": "Distance", "instances": 51, "metric_value": 0.9864, "depth": 1}
	if obj[6]<=2:
		# {"feature": "Occupation", "instances": 46, "metric_value": 0.9503, "depth": 2}
		if obj[3]<=12:
			# {"feature": "Education", "instances": 37, "metric_value": 0.8419, "depth": 3}
			if obj[2]<=1:
				# {"feature": "Restaurant20to50", "instances": 21, "metric_value": 0.4537, "depth": 4}
				if obj[4]>-1.0:
					# {"feature": "Coupon", "instances": 20, "metric_value": 0.2864, "depth": 5}
					if obj[1]<=3:
						return 'True'
					elif obj[1]>3:
						# {"feature": "Passanger", "instances": 7, "metric_value": 0.5917, "depth": 6}
						if obj[0]<=1:
							# {"feature": "Direction_same", "instances": 5, "metric_value": 0.7219, "depth": 7}
							if obj[5]<=0:
								return 'True'
							elif obj[5]>0:
								return 'True'
							else: return 'True'
						elif obj[0]>1:
							return 'True'
						else: return 'True'
					else: return 'True'
				elif obj[4]<=-1.0:
					return 'False'
				else: return 'False'
			elif obj[2]>1:
				# {"feature": "Passanger", "instances": 16, "metric_value": 1.0, "depth": 4}
				if obj[0]<=2:
					# {"feature": "Coupon", "instances": 11, "metric_value": 0.9457, "depth": 5}
					if obj[1]<=2:
						# {"feature": "Restaurant20to50", "instances": 6, "metric_value": 0.9183, "depth": 6}
						if obj[4]>0.0:
							# {"feature": "Direction_same", "instances": 4, "metric_value": 1.0, "depth": 7}
							if obj[5]<=0:
								return 'True'
							elif obj[5]>0:
								return 'False'
							else: return 'False'
						elif obj[4]<=0.0:
							return 'True'
						else: return 'True'
					elif obj[1]>2:
						return 'False'
					else: return 'False'
				elif obj[0]>2:
					# {"feature": "Coupon", "instances": 5, "metric_value": 0.7219, "depth": 5}
					if obj[1]>0:
						return 'True'
					elif obj[1]<=0:
						# {"feature": "Restaurant20to50", "instances": 2, "metric_value": 1.0, "depth": 6}
						if obj[4]>1.0:
							return 'True'
						elif obj[4]<=1.0:
							return 'False'
						else: return 'False'
					else: return 'True'
				else: return 'True'
			else: return 'False'
		elif obj[3]>12:
			# {"feature": "Restaurant20to50", "instances": 9, "metric_value": 0.7642, "depth": 3}
			if obj[4]>0.0:
				# {"feature": "Direction_same", "instances": 8, "metric_value": 0.5436, "depth": 4}
				if obj[5]<=0:
					return 'False'
				elif obj[5]>0:
					# {"feature": "Education", "instances": 3, "metric_value": 0.9183, "depth": 5}
					if obj[2]<=0:
						# {"feature": "Passanger", "instances": 2, "metric_value": 1.0, "depth": 6}
						if obj[0]<=1:
							# {"feature": "Coupon", "instances": 2, "metric_value": 1.0, "depth": 7}
							if obj[1]<=2:
								return 'False'
							else: return 'False'
						else: return 'False'
					elif obj[2]>0:
						return 'False'
					else: return 'False'
				else: return 'False'
			elif obj[4]<=0.0:
				return 'True'
			else: return 'True'
		else: return 'False'
	elif obj[6]>2:
		return 'False'
	else: return 'False'
