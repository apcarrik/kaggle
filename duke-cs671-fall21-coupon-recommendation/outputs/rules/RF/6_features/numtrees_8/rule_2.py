def findDecision(obj): #obj[0]: Passanger, obj[1]: Coupon, obj[2]: Education, obj[3]: Occupation, obj[4]: Restaurant20to50, obj[5]: Distance
	# {"feature": "Restaurant20to50", "instances": 127, "metric_value": 0.9838, "depth": 1}
	if obj[4]<=2.0:
		# {"feature": "Passanger", "instances": 115, "metric_value": 0.9956, "depth": 2}
		if obj[0]<=2:
			# {"feature": "Occupation", "instances": 84, "metric_value": 0.9963, "depth": 3}
			if obj[3]<=10:
				# {"feature": "Education", "instances": 60, "metric_value": 0.9968, "depth": 4}
				if obj[2]<=2:
					# {"feature": "Coupon", "instances": 43, "metric_value": 0.9682, "depth": 5}
					if obj[1]<=3:
						# {"feature": "Distance", "instances": 30, "metric_value": 0.9183, "depth": 6}
						if obj[5]<=2:
							return 'True'
						elif obj[5]>2:
							return 'True'
						else: return 'True'
					elif obj[1]>3:
						# {"feature": "Distance", "instances": 13, "metric_value": 0.9957, "depth": 6}
						if obj[5]<=1:
							return 'True'
						elif obj[5]>1:
							return 'False'
						else: return 'False'
					else: return 'False'
				elif obj[2]>2:
					# {"feature": "Distance", "instances": 17, "metric_value": 0.9367, "depth": 5}
					if obj[5]<=2:
						# {"feature": "Coupon", "instances": 14, "metric_value": 0.9852, "depth": 6}
						if obj[1]>1:
							return 'True'
						elif obj[1]<=1:
							return 'False'
						else: return 'False'
					elif obj[5]>2:
						return 'False'
					else: return 'False'
				else: return 'False'
			elif obj[3]>10:
				# {"feature": "Coupon", "instances": 24, "metric_value": 0.8709, "depth": 4}
				if obj[1]>0:
					# {"feature": "Education", "instances": 20, "metric_value": 0.9341, "depth": 5}
					if obj[2]>1:
						# {"feature": "Distance", "instances": 17, "metric_value": 0.9774, "depth": 6}
						if obj[5]<=2:
							return 'False'
						elif obj[5]>2:
							return 'False'
						else: return 'False'
					elif obj[2]<=1:
						return 'False'
					else: return 'False'
				elif obj[1]<=0:
					return 'False'
				else: return 'False'
			else: return 'False'
		elif obj[0]>2:
			# {"feature": "Occupation", "instances": 31, "metric_value": 0.8238, "depth": 3}
			if obj[3]<=11:
				# {"feature": "Coupon", "instances": 20, "metric_value": 0.469, "depth": 4}
				if obj[1]>1:
					# {"feature": "Education", "instances": 17, "metric_value": 0.3228, "depth": 5}
					if obj[2]<=1:
						return 'True'
					elif obj[2]>1:
						# {"feature": "Distance", "instances": 8, "metric_value": 0.5436, "depth": 6}
						if obj[5]>1:
							return 'True'
						elif obj[5]<=1:
							return 'True'
						else: return 'True'
					else: return 'True'
				elif obj[1]<=1:
					# {"feature": "Education", "instances": 3, "metric_value": 0.9183, "depth": 5}
					if obj[2]<=0:
						# {"feature": "Distance", "instances": 2, "metric_value": 1.0, "depth": 6}
						if obj[5]<=2:
							return 'False'
						else: return 'False'
					elif obj[2]>0:
						return 'True'
					else: return 'True'
				else: return 'True'
			elif obj[3]>11:
				# {"feature": "Education", "instances": 11, "metric_value": 0.994, "depth": 4}
				if obj[2]>1:
					# {"feature": "Coupon", "instances": 8, "metric_value": 0.9544, "depth": 5}
					if obj[1]>3:
						# {"feature": "Distance", "instances": 6, "metric_value": 1.0, "depth": 6}
						if obj[5]>1:
							return 'True'
						elif obj[5]<=1:
							return 'True'
						else: return 'True'
					elif obj[1]<=3:
						return 'True'
					else: return 'True'
				elif obj[2]<=1:
					return 'False'
				else: return 'False'
			else: return 'False'
		else: return 'True'
	elif obj[4]>2.0:
		# {"feature": "Passanger", "instances": 12, "metric_value": 0.4138, "depth": 2}
		if obj[0]<=2:
			return 'True'
		elif obj[0]>2:
			# {"feature": "Occupation", "instances": 3, "metric_value": 0.9183, "depth": 3}
			if obj[3]>3:
				return 'True'
			elif obj[3]<=3:
				return 'False'
			else: return 'False'
		else: return 'True'
	else: return 'True'
