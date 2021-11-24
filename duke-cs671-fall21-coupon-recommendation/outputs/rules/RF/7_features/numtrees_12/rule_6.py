def findDecision(obj): #obj[0]: Passanger, obj[1]: Coupon, obj[2]: Education, obj[3]: Occupation, obj[4]: Restaurant20to50, obj[5]: Direction_same, obj[6]: Distance
	# {"feature": "Distance", "instances": 85, "metric_value": 0.9975, "depth": 1}
	if obj[6]<=2:
		# {"feature": "Coupon", "instances": 77, "metric_value": 0.9989, "depth": 2}
		if obj[1]<=3:
			# {"feature": "Restaurant20to50", "instances": 44, "metric_value": 0.976, "depth": 3}
			if obj[4]<=1.0:
				# {"feature": "Passanger", "instances": 29, "metric_value": 0.8936, "depth": 4}
				if obj[0]>0:
					# {"feature": "Education", "instances": 25, "metric_value": 0.9427, "depth": 5}
					if obj[2]<=3:
						# {"feature": "Occupation", "instances": 23, "metric_value": 0.8865, "depth": 6}
						if obj[3]<=16:
							# {"feature": "Direction_same", "instances": 20, "metric_value": 0.9341, "depth": 7}
							if obj[5]<=0:
								return 'True'
							elif obj[5]>0:
								return 'False'
							else: return 'False'
						elif obj[3]>16:
							return 'True'
						else: return 'True'
					elif obj[2]>3:
						return 'False'
					else: return 'False'
				elif obj[0]<=0:
					return 'True'
				else: return 'True'
			elif obj[4]>1.0:
				# {"feature": "Education", "instances": 15, "metric_value": 0.971, "depth": 4}
				if obj[2]<=2:
					# {"feature": "Passanger", "instances": 11, "metric_value": 0.994, "depth": 5}
					if obj[0]>0:
						# {"feature": "Occupation", "instances": 9, "metric_value": 0.9183, "depth": 6}
						if obj[3]<=20:
							# {"feature": "Direction_same", "instances": 8, "metric_value": 0.8113, "depth": 7}
							if obj[5]<=0:
								return 'True'
							elif obj[5]>0:
								return 'True'
							else: return 'True'
						elif obj[3]>20:
							return 'False'
						else: return 'False'
					elif obj[0]<=0:
						return 'False'
					else: return 'False'
				elif obj[2]>2:
					return 'False'
				else: return 'False'
			else: return 'False'
		elif obj[1]>3:
			# {"feature": "Occupation", "instances": 33, "metric_value": 0.9834, "depth": 3}
			if obj[3]<=7:
				# {"feature": "Restaurant20to50", "instances": 17, "metric_value": 0.9774, "depth": 4}
				if obj[4]>0.0:
					# {"feature": "Direction_same", "instances": 16, "metric_value": 0.9887, "depth": 5}
					if obj[5]<=0:
						# {"feature": "Passanger", "instances": 15, "metric_value": 0.9968, "depth": 6}
						if obj[0]<=1:
							# {"feature": "Education", "instances": 10, "metric_value": 1.0, "depth": 7}
							if obj[2]<=0:
								return 'True'
							elif obj[2]>0:
								return 'False'
							else: return 'False'
						elif obj[0]>1:
							# {"feature": "Education", "instances": 5, "metric_value": 0.971, "depth": 7}
							if obj[2]<=0:
								return 'True'
							elif obj[2]>0:
								return 'True'
							else: return 'True'
						else: return 'True'
					elif obj[5]>0:
						return 'True'
					else: return 'True'
				elif obj[4]<=0.0:
					return 'True'
				else: return 'True'
			elif obj[3]>7:
				# {"feature": "Restaurant20to50", "instances": 16, "metric_value": 0.8113, "depth": 4}
				if obj[4]>0.0:
					# {"feature": "Passanger", "instances": 13, "metric_value": 0.6194, "depth": 5}
					if obj[0]<=1:
						# {"feature": "Education", "instances": 10, "metric_value": 0.7219, "depth": 6}
						if obj[2]<=2:
							# {"feature": "Direction_same", "instances": 8, "metric_value": 0.5436, "depth": 7}
							if obj[5]<=0:
								return 'False'
							elif obj[5]>0:
								return 'False'
							else: return 'False'
						elif obj[2]>2:
							# {"feature": "Direction_same", "instances": 2, "metric_value": 1.0, "depth": 7}
							if obj[5]<=0:
								return 'False'
							else: return 'False'
						else: return 'False'
					elif obj[0]>1:
						return 'False'
					else: return 'False'
				elif obj[4]<=0.0:
					# {"feature": "Passanger", "instances": 3, "metric_value": 0.9183, "depth": 5}
					if obj[0]<=1:
						# {"feature": "Education", "instances": 2, "metric_value": 1.0, "depth": 6}
						if obj[2]>0:
							return 'False'
						elif obj[2]<=0:
							return 'True'
						else: return 'True'
					elif obj[0]>1:
						return 'True'
					else: return 'True'
				else: return 'True'
			else: return 'False'
		else: return 'False'
	elif obj[6]>2:
		return 'False'
	else: return 'False'
